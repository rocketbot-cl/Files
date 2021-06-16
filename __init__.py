# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import sys
import time
import os
from pathlib import Path
import shutil
import subprocess
import glob


"""
    Obtengo el modulo que fueron invocados
"""

# FUNCTIONS

if sys.platform == 'darwin':
    def openFolder(path):
        subprocess.check_call(['open', '--', path])
elif sys.platform == 'linux':
    def openFolder(path):
        subprocess.check_call(['xdg-open', path])
elif sys.platform == 'win32':
    def openFolder(path):
        try:
            subprocess.check_call(['explorer', path])
        except:
            pass


def getfile():
    global tk, filedialog
    file_path = ""
    if _platform == 'darwin':
        alert_ = """osascript -e 'set aa to choose file'"""
        p = subprocess.Popen(alert_, stdout=subprocess.PIPE, shell=True)
        output, err = p.communicate()
        file_path = str(output).replace(str(output).split(":")[0], "").replace(":", "/").replace("\\n", "")
        if file_path.endswith("'"):
            file_path = file_path[:-1]
    else:
        root = tk.Tk()
        root.title("Rocketbot - Seleccione un archivo")
        root.after(5000, lambda: root.focus_force())
        root.focus()
        root.wm_attributes("-topmost", 1)
        w = 300
        h = 400
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        root.geometry("300x0+%d+%d" % (x, y))
        root.update()
        file_path = filedialog.askopenfilename(parent=root, title='Rocketbot - Seleccione un archivo')
        root.destroy()
        sleep(1)
    return file_path


def get_folder():
    file_path = ""
    try:
        print(sys.platform)
        if sys.platform == 'darwin':
            alert_ = """osascript -e 'set aa to choose folder name'"""
            p = subprocess.Popen(alert_, stdout=subprocess.PIPE, shell=True)
            output, err = p.communicate()
            file_path = str(output).replace(str(output).split(":")[0], "").replace(":", "/").replace("\\n", "")
            if file_path.endswith("'"):
                file_path = file_path[:-1]
        elif sys.platform == "win32" or sys.platform == "win64":
            scr = """
              Dim strPath

strPath = SelectFolder( "" )
If strPath = vbNull Then
    WScript.WScript.StdOut.Write("")
Else
    WScript.StdOut.Write(strPath)
End If


Function SelectFolder( myStartFolder )
' This function opens a "Select Folder" dialog and will
' return the fully qualified path of the selected folder
'
' Argument:
'     myStartFolder    [string]    the root folder where you can start browsing;
'                                  if an empty string is used, browsing starts
'                                  on the local computer
'
' Returns:
' A string containing the fully qualified path of the selected folder
'
' Written by Rob van der Woude
' http://www.robvanderwoude.com

    ' Standard housekeeping
    Dim objFolder, objItem, objShell
    
    ' Custom error handling
    On Error Resume Next
    SelectFolder = vbNull

    ' Create a dialog object
    Set objShell  = CreateObject( "Shell.Application" )
    Set objFolder = objShell.BrowseForFolder( 0, "Select Folder", 0, myStartFolder )

    ' Return the path of the selected folder
    If IsObject( objfolder ) Then SelectFolder = objFolder.Self.Path

    ' Standard housekeeping
    Set objFolder = Nothing
    Set objshell  = Nothing
    On Error Goto 0
End Function"""
            with open("tmp.vbs", "w") as f:
                print(scr)
                f.write(scr)
                f.close()
                con = subprocess.Popen('cscript tmp.vbs //Nologo', shell=True, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
                a = con.communicate()
                print("> ",a)
                file_path = str(a[0].decode()).replace("\\", "/")
        else:
            root = tk.Tk()
            root.title("Rocketbot - Seleccione una carpeta")
            root.after(5000, lambda: root.focus_force())
            root.focus()
            root.wm_attributes("-topmost", 1)
            w = 300
            h = 400
            ws = root.winfo_screenwidth()
            hs = root.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            root.geometry("300x0+%d+%d" % (x, y))
            root.update()
            file_path = filedialog.askdirectory(parent=root, title='Rocketbot - Seleccione una carpeta')
            root.destroy()
            time.sleep(1)

    except Exception as e:
        print(e)

    return file_path


module = GetParams("module")

if module == "openFolder":
    path = GetParams("path").replace("/", os.sep)

    try:
        if os.path.isdir(path):
            openFolder(path)
        elif os.path.isfile(path):
            path = os.sep.join(path.split(os.sep)[:-1])
            openFolder(path)
    except Exception as e:
        PrintException()
        raise e

if module == "openFile":
    path = GetParams("path")

    try:
        if sys.platform == 'darwin' or sys.platform == 'linux':
            subprocess.call(["open", path])
        else:
            path = os.path.realpath(path)
            os.startfile(path)
    except Exception as e:
        PrintException()
        raise e

if module == "getFile":
    result = GetParams("result")

    try:
        path = getfile()
        SetVar(result, path)
    except Exception as e:
        PrintException()
        raise e

if module == "getFolder":
    result = GetParams("result")

    try:
        path = get_folder()
        SetVar(result, path)
    except Exception as e:
        PrintException()
        raise e

if module == "delete":
    path = GetParams("path")

    try:
        shutil.rmtree(path, ignore_errors=False)
        # os.rmdir(path)
    except Exception as e:
        PrintException()
        raise e

if module == "deleteFile":
    path = GetParams('path')
    name = GetParams('name')

    try:
        for zippath in glob.iglob(os.path.join(path, name)):
            os.remove(zippath)
    except Exception as e:
        PrintException()
        raise e

if module == "readFile":
    file_ = GetParams('file_')
    split = GetParams("split")
    var_ = GetParams('var_')

    try:
        if split is not None:
            split = eval(split)
        with open(file_, 'r', encoding="latin-1") as f:
            if split:
                output = f.readlines()
            else:
                output = f.read()
            
        SetVar(var_, output)

    except Exception as e:
        PrintException()
        raise e


if module == "createFolder":

    folder = GetParams('path')

    try:
         os.stat(folder)
    except:
         os.makedirs(folder)

if module == "exists":
    path  = GetParams("path")
    result = GetParams("var_")

    try:
        exist = os.path.exists(path)

        if result:
            SetVar(result, exist)
    except Exception as e:
        PrintException()
        raise e

if module == "renameFolder":

    # Just tested in Linux
    # After test in Windows, change the json data for compatibility
    # Problem in Windows: Do not split well. Uses '/' and not '\'. So, cannot split it with so.sep
    # Dunno why. Investigate
    
    ## Tested in Windows, it works well. See comments for more information about separation

    # It take the path where the folder is contain
    path = GetParams('path')

    #It gets splited
    # Use os.sep [change separator for os.sep ( e.g.: pathSplited = path.slpit(separator) => pathSpliter = path.split(os.sep))] only if does not take from choosing the folder
    # because choosing the folder it gets in linux os.sep ('/'). It uses python, so, it gets that way.
    # pathSplited = path.split(os.sep)
    separator = "/"
    pathSplited = path.split(separator)

    # Gets the new folder's name
    newFoldersName = GetParams('newFoldersName')

    # Change the last item of the array (path splited) and in the last position, replace the old name with the new one
    pathSplited[(len(pathSplited)-1)] = newFoldersName

    # It gets join into one path
    pathWithNewFolder = separator.join(pathSplited)

    try:

        #os.chdir(path) Rompe rockect :S
        
        # Method to rename the folder
        os.rename(path, pathWithNewFolder)

    except Exception as e:
        PrintException()
        raise e

if module == "listFiles":
    path = GetParams("path")
    var_ = GetParams("result")
    option = GetParams("option")

    def ext(x):
        return os.path.splitext(x)[::-1]
    try:
        if option == "date":
            files = sorted(Path(path).iterdir(), key=os.path.getmtime)
            paths = [file.name for file in files]
        elif option == "type":
            files = sorted(Path(path).iterdir(), key=ext)
            paths = [file.name for file in files]
        else:
            paths = os.listdir(path)

        SetVar(var_, paths)
    except Exception as e:
        PrintException()
        raise e


if module == "search_match":

    path = GetParams('path')
    ext_ = GetParams('ext_')
    match = GetParams('match')
    result_ = GetParams('result_')

    try:
        list_ext = []

        if ext_:
            for file in os.listdir(path):
                if file.endswith(ext_):
                    list_ext.append(file)
        else:
            list_ext = list_ext = os.listdir(path)

        res = []
        for ele in list_ext:
            if match in ele:
                res.append(ele)

        SetVar(result_, res)

    except Exception as e:
       PrintException()
       raise e
