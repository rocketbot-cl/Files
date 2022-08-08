



# Files
  
Módulo para el manejo de archivos  
  
![banner](C:\Users\jmsir\Desktop\RB\Rocketbot\modules\Files\docs\imgs\Banner_Files.png)
## Howto install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  


# Como usar este modulo




## Description of the commands

### Open Folder
  
Open folder from a file path
|Parameters|Description|example|
| --- | --- | --- |
|File path  |Open the folder from the specified path|C:/User/Usuario/Folder/|

### Open File
  
Open file
|Parameters|Description|example|
| --- | --- | --- |
|File path  |Open the file from the specified path|C:/User/Usuario/Folder/File.extension|

### Get file
  
Ask the user to select a file and get the path
|Parameters|Description|example|
| --- | --- | --- |
|Variable where save path  |When you execute it, or the file explorer opens so that we can select the file, once selected, it provides us with or direct where it is located.|Result|

### Get folder
  
Ask the user to select a folder
|Parameters|Description|example|
| --- | --- | --- |
|Variable where save path  |When executed, the file explorer opens so that we can select the folder we want, once selected, it returns the path where it is located|Result|

### Rename folder
  
Ask the user to select a folder to rename it
|Parameters|Description|example|
| --- | --- | --- |
|Path of the folder to rename  |When executing, the folder that we have specified is renamed|C:/User/Folder/|
|New name of the folder||New name|

### Read file
  
Read a file and save its content in a variable
|Parameters|Description|example|
| --- | --- | --- |
|File path||C:/Users/User/Desktop/file.txt|
|Separate lines|Returns the content of a file and stores it in a variable, if the separate lines option is checked, it returns the content of the file within a list and each line is an element within the list||
|Assign result to variable|Variable where the obtained value will be stored|Variable|

### Delete folder
  
Delete a folder with all files
|Parameters|Description|example|
| --- | --- | --- |
|File path  |Slect path of the folder to delete|C:/User/Usuario/Folder/|
|Assign result to variable||Variable|

### Delete file
  
Delete a file indicating its extension and its name or part of the name
|Parameters|Description|example|
| --- | --- | --- |
|File path  |Path of the file to delete|C:/User/Usuario/Folder/|
|Type of file to delete|Name and extension of the file to delete|name*.pdf|
|Assign result to variable||Variable|

### Create Folder
  
Enter the path with name where you want to create the folder
|Parameters|Description|example|
| --- | --- | --- |
|File path|Path where folder are be created|C:/Users/User/Desktop/folder_test|
|Assign result to variable||Variable|

### Check existence
  
Check if a file o folder exists
|Parameters|Description|example|
| --- | --- | --- |
|File path  |Address of the folder you want to check for existence|C:/User/Usuario/Folder/|
|Assign result to variable||Variable|

### List sorted files
  
CList files and select sort
|Parameters|Description|example|
| --- | --- | --- |
|File path  |Path of the folder from which you want to list the files|C:/User/Usuario/Folder/|
|Sort by|Options to order, Name, Date and Type||
|Assign result to variable|Variable where the list of items in the folder is stored|Variable|

### Search File
  
Returns a list with matches
|Parameters|Description|example|
| --- | --- | --- |
|File path  |Address where the file will be searched|C:/User/Usuario/Folder/|
|Filter by extension|Filter by extension looking for all files with the specified extension|.pdf|
|Word to search|Word to search for in the file name|.fileTest|
|Assign result to variable|Variable where the names of the files will be stored|Variable|

### Get Metadata
  
Obtains file metadata such as: Name, modification date, creation date and file weight.
|Parameters|Description|example|
| --- | --- | --- |
|File path  |Address where the desired files will be searched|C:/User/Usuario/Folder/|
|Select Metadata|Options to get all or a certain metadata||
|Select unit|Returns the weight of the file in the specified measure|KB, MB or GB|
|Filter by name|Word we want to search for in the file name|.fileTest|
|Filter by extension|Extension that we want to look for in the files|.pdf|
|Assign result to variable|Variable where the found files will be stored|Variable|
