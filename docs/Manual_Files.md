



# Files
  
Módulo para el manejo de archivos  
  
![banner](/docs/imgs/Banner_C:\Users\jmsir\Desktop\RB\Rocketbot\modules\Files.png)
## Howto install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  


# Como usar este modulo




## Description of the commands

### Open Folder
  
Open folder from a file path
|Parameters|Description|example|
| --- | --- | --- |
|File path  ||C:/User/Usuario/Folder/|

### Open File
  
Open file
|Parameters|Description|example|
| --- | --- | --- |
|File path  ||C:/User/Usuario/Folder/File.extension|

### Get file
  
Ask the user to select a file and get the path
|Parameters|Description|example|
| --- | --- | --- |
|Variable where save path  ||Result|

### Get folder
  
Ask the user to select a folder
|Parameters|Description|example|
| --- | --- | --- |
|Variable where save path  ||Result|

### Rename folder
  
Ask the user to select a folder to rename it
|Parameters|Description|example|
| --- | --- | --- |
|Path of the folder to change  ||C:/User/Folder/|
|New name of the folder||New name|

### Read file
  
Read a file and save its content in a variable
|Parameters|Description|example|
| --- | --- | --- |
|File path||C:/Users/User/Desktop/file.txt|
|Separate lines|||
|Assign result to variable||Variable|

### Delete folder
  
Delete a folder with all files
|Parameters|Description|example|
| --- | --- | --- |
|Folder path  ||C:/User/Usuario/Folder/|
|Assign result to variable||Variable|

### Delete file
  
Delete a file indicating its extension and its name or part of the name
|Parameters|Description|example|
| --- | --- | --- |
|Folder path  ||C:/User/Usuario/Folder/file.txt|
|File to delete||name*.pdf|
|Assign result to variable||Variable|

### Create Folder
  
Enter the path with name where you want to create the folder
|Parameters|Description|example|
| --- | --- | --- |
|File path||C:/Users/User/Desktop/folder_test|
|Assign result to variable||Variable|

### Check existence
  
Check if a file o folder exists
|Parameters|Description|example|
| --- | --- | --- |
|File path  ||C:/User/Usuario/Folder/|
|Assign result to variable||Variable|

### List sorted files
  
CList files and select sort
|Parameters|Description|example|
| --- | --- | --- |
|File path  ||C:/User/Usuario/Folder/|
|Sort by|||
|Assign result to variable||Variable|

### Search File
  
Returns a list with matches
|Parameters|Description|example|
| --- | --- | --- |
|File path  ||C:/User/Usuario/Folder/|
|Filter by extension||.pdf|
|Word to search||.fileTest|
|Assign result to variable||Variable|
