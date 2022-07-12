"""Tests for FilesServices.py file."""

import os
import sys
sys.path.append(os.getcwd())
import pytest
from libs.FilesServices import FilesService
from datetime import datetime
from time import sleep

basepath = os.getcwd()
created_time = ""

def test_create_folder():
    """Test create folder."""
    FilesService.create_folder(".", "test_folder")
    assert os.path.exists("test_folder")

def test_create_folder_on_unexisting_folder():
    """Test create folder in unexisting folder."""
    with pytest.raises(FileNotFoundError):
        FilesService.create_folder("unexisting_folder", "test_folder")

def test_create_existing_folder():
    """Test create existing folder."""
    with pytest.raises(FileExistsError):
        FilesService.create_folder(".", "test_folder")

def test_create_text_file():
    """Test create text file."""
    global created_time
    FilesService.create_text_file("test_folder/test_file.txt", "test")
    assert os.path.exists("test_folder/test_file.txt")
    created_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("test_folder/test_file.txt", "r") as f:
        assert f.read() == "test"

def test_read_file():
    """Test read file."""
    assert FilesService.read_file("test_folder/test_file.txt") == "test"

def test_copy_file():
    """Test copy file."""
    FilesService.copy_file("test_folder/test_file.txt", "test_folder/a_test_file_copy.env")
    assert os.path.exists("test_folder/a_test_file_copy.env")
    with open("test_folder/a_test_file_copy.env", "r") as f:
        assert f.read() == "test"

def test_list_files():
    """Test list files."""
    assert FilesService.list_files("test_folder") == [
        os.path.join(basepath, "test_folder",file) for file in ["a_test_file_copy.env", "test_file.txt"]
        ]

def test_list_files_order_by_dates_and_only_names():
    assert FilesService.list_files("test_folder", order_by="date", only_names=True) == ["test_file.txt", "a_test_file_copy.env"]

def test_list_files_order_by_names_and_only_names():
    assert FilesService.list_files("test_folder", order_by="name", only_names=True) == ["a_test_file_copy.env","test_file.txt"]

def test_list_files_order_by_created_and_only_names():
    assert FilesService.list_files("test_folder", order_by="created", only_names=True) == ["test_file.txt", "a_test_file_copy.env"]

def test_list_files_order_by_types():
    assert FilesService.list_files("test_folder", order_by="type") == [
        os.path.join(basepath, "test_folder",file) for file in ["a_test_file_copy.env", "test_file.txt"]
        ]

def test_search_file():
    """Test search file."""
    assert FilesService.search_files("test_folder") == ["a_test_file_copy.env", "test_file.txt"]

def test_get_file_metadata():
    """Test get file metadata."""
    assert FilesService.get_file_metadata("test_folder/test_file.txt") == {
        "name": "test_file.txt",
        "path": os.path.join(basepath, "test_folder", "test_file.txt"),
        "size": 4,
        "created": created_time,
        "modified": created_time
        }

def test_delete_file():
    """Test delete file."""
    FilesService.delete_file("test_folder/test_file.txt")
    assert not os.path.exists("test_file.txt")


def test_delete_folder():
    """Test delete folder."""
    FilesService.delete_folder("test_folder")
    assert not os.path.exists("test_folder")

def test_delete_unexisting_folder():
    """Test delete unexisting folder."""
    with pytest.raises(FileNotFoundError):
        FilesService.delete_folder("unexisting_folder")

    