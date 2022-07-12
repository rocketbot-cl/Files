"""Library to manage files and directories."""

__author__ = "Danilo Toro"
__version__ = "1.0.0"

import glob
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
try:
    from win32com import client
except ImportError:
    pass
convert_units_functions = {
    "KB": lambda x: x / 1024,
    "MB": lambda x: x / (1024*1024),
    "GB": lambda x: x / (1024*1024*1024),
}



class FilesService:
    """Abstract class to manage files and directories.

    Static methods:

    """

    @staticmethod
    def get_opened_folders():
        if sys.platform == "win32":
            shell = client.Dispatch("Shell.Application")
            return [window.LocationURL.replace("file:///", "") for window in shell.Windows()]
        
        raise NotImplementedError("Not implemented on this platform")
                

    @staticmethod
    def open_folder(path: str):
        """Open folder with terminal line command."""
        if sys.platform == "win32":
            return subprocess.call(["explorer", path.replace("/", os.sep)])
        if sys.platform == "darwin":
            return subprocess.check_call(["open", "--", path])
        if sys.platform == "linux":
            return subprocess.check_call(["xdg-open", path])

        raise NotImplementedError(
            "Platform not supported: {}".format(sys.platform))

    @staticmethod
    def open_file(path: str):
        """Open file with terminal line command."""
        if sys.platform in ['darwin', 'linux']:
            return subprocess.check_call(["open", path])

        return os.startfile(os.path.realpath(path))

    @staticmethod
    def create_folder(path: str, folder_name: str):
        """Create folder."""
        if not os.path.exists(path):
            raise FileNotFoundError("Path not found: {}".format(path))

        os.makedirs(os.path.join(path, folder_name))


    @staticmethod
    def delete_folder(path: str):
        """Delete folder."""
        if not os.path.exists(path):
            raise FileNotFoundError("Path not found: {}".format(path))

        shutil.rmtree(path, ignore_errors=False)

    @staticmethod
    def delete_file(file_path: str = None, folder_path: str = None, file_name: str = "*"):
        """Delete file."""
        if file_path is not None:
            os.remove(file_path)

        if folder_path is not None:
            for zippath in glob.iglob(os.path.join(folder_path, file_name)):
                os.remove(zippath)
    
    @staticmethod
    def copy_file(source_path: str, destination_path: str):
        """Copy file."""
        shutil.copy(source_path, destination_path)

    @staticmethod
    def create_text_file(path: str, text: str):
        """Create text file."""
        with open(os.path.join(path), "w") as f:
            f.write(text)

    @staticmethod
    def read_file(path: str, encoding: str = "utf-8", split_lines: bool = False):
        """Read file."""
        with open(path, "r", encoding=encoding) as file:
            if split_lines:
                return file.readlines()
            return file.read()


    @staticmethod
    def list_files(path: str, order_by: str = None, only_names: bool = False):
        """List files in folder sorted by name, extension, date or type.

        path: str - Path to folder.
        order_by: str - Order by name, extension, date or type.
        """
        order_by_options = {
            "date": os.path.getmtime,
            "type": lambda x: os.path.splitext(x)[::-1],
            "created": os.path.getctime,
        }
        files = sorted(Path(path).iterdir(),
                       key=order_by_options.get(order_by, lambda x: x))
        if only_names:
            return [file.name for file in files]
        return [str(file.absolute()) for file in files]

    @staticmethod
    def search_files(path: str, extension: str = None, contain: str = None):
        """Search files in folder by extension or contain.

        path: str - Path to folder.
        extension: str - Extension to search.
        contain: str - Text to search.
        """
        filter_ = "*"
        if extension is not None:
            filter_ *= "." + extension
            filter_ = filter_.replace("..", ".")
        if contain is not None:
            filter_ = "*" + contain + filter_
        
        return [file.replace(path+os.sep, "") for file in glob.glob(os.path.join(path, filter_))]

    @staticmethod
    def get_file_metadata(path: str):
        """Get metadata of file."""
        return {
            "name": FilesService.get_filename_from_path(path),
            "path": os.path.abspath(path),
            "size": FilesService.get_file_size(path),
            "modified": FilesService.get_file_modified_date(path, True),
            "created": FilesService.get_file_created_date(path, True),
        }

    @staticmethod
    def get_metadata_from_list_of_files(files: list):
        """Get metadata from list of files."""
        return [FilesService.get_file_metadata(file) for file in files]

    @staticmethod
    def get_file_size(path: str):
        """Get file size."""
        return os.path.getsize(path)

    @staticmethod
    def get_filename_from_path(path: str):
        """Get filename from path."""
        return os.path.basename(path)

    @staticmethod
    def get_file_modified_date(path: str, as_string:bool=False):
        """Get file modified date."""
        date = datetime.fromtimestamp(os.path.getmtime(path))
        if as_string:
            return date.strftime("%d/%m/%Y %H:%M:%S")
        return date

    @staticmethod
    def get_file_created_date(path: str, as_string:bool=False):
        """Get file created date."""
        date = datetime.fromtimestamp(os.path.getctime(path))
        if as_string:
            return date.strftime("%d/%m/%Y %H:%M:%S")
        return date