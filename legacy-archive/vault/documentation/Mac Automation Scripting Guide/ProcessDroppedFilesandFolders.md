---
title: Mac Automation Scripting Guide
apple_id: TP40016239
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/ProcessDroppedFilesandFolders.html
archived_at: '2026-07-15T07:45:59.813148Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Mac Automation Scripting Guide](index.md)



## Processing Dropped Files and Folders

Droplets are applets configured to process dropped files and folders. A droplet is distinguishable from a normal applet because its icon includes a downward pointing arrow, as shown in Figure 17-1.

__Figure 17-1__A script droplet icon
![image: ../Art/icon_droplet_2x.png](attachments/Art/icon_droplet_2x.png)

To create an AppleScript droplet, include an `open` event handler in your script and save the script as an application. To create a JavaScript droplet, include an `openDocuments` function in your script and save the script as an application. The presence of this handler or function automatically renders the saved application as a droplet, allowing it to accept dropped files and folders in the Finder. The `open` handler and `openDocuments` function accept a single parameter—a list of dropped files or folders—which are passed to the handler when the script is activated by dropping something onto it. In AppleScript, these dropped files and folders are `alias` objects. In JavaScript, they’re `Path` objects. For more information about these types of objects, see [Referencing Files and Folders](ReferenceFilesandFolders.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqmzufvjvomi).

An AppleScript `open` handler is formatted as shown in Listing 17-1.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=on%20open%20theDroppedItems%0A%20%20%20%20--%20Process%20the%20dropped%20items%20here%0Aend%20open)

__Listing 17-1__AppleScript: Structure of an `open` handler

1. `on open theDroppedItems`
2. `-- Process the dropped items here`
3. `end open`

A JavaScript `openDocuments` function is formatted as shown in Listing 17-2.

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=function%20openDocuments%28droppedItems%29%20%7B%0A%20%20%20%20%2F%2F%20Process%20the%20dropped%20items%20here%0A%7D)

__Listing 17-2__JavaScript: Structure of an `openDocuments` function

1. `function openDocuments(droppedItems) {`
2. `// Process the dropped items here`
3. `}`

Typically, a droplet loops through items dropped onto it, processing them individually, as in Listing 17-3 and Listing 17-4.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=on%20open%20theDroppedItems%0A%20%20%20%20repeat%20with%20a%20from%201%20to%20length%20of%20theDroppedItems%0A%20%20%20%20%20%20%20%20set%20theCurrentDroppedItem%20to%20item%20a%20of%20theDroppedItems%0A%20%20%20%20%20%20%20%20--%20Process%20each%20dropped%20item%20here%0A%20%20%20%20end%20repeat%0Aend%20open)

__Listing 17-3__AppleScript: An `open` handler that loops through dropped items

1. `on open theDroppedItems`
2. `repeat with a from 1 to length of theDroppedItems`
3. `set theCurrentDroppedItem to item a of theDroppedItems`
4. `-- Process each dropped item here`
5. `end repeat`
6. `end open`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=function%20openDocuments%28droppedItems%29%20%7B%0A%20%20%20%20for%20%28var%20item%20of%20droppedItems%29%20%7B%0A%20%20%20%20%20%20%20%20%2F%2F%20Process%20each%20dropped%20item%20here%0A%20%20%20%20%7D%0A%7D)

__Listing 17-4__JavaScript: An `openDocuments` function that loops through dropped items

1. `function openDocuments(droppedItems) {`
2. `for (var item of droppedItems) {`
3. `// Process each dropped item here`
4. `}`
5. `}`

To run a droplet, drop files or folders onto it in the Finder. To test a droplet in Script Editor, add the following line(s) of code to the root level—the `run` handler portion—of the script. Listing 17-5 and Listing 17-6 prompt you to select a file and then passes it to the `open` handler or `openDocuments` function.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=open%20%7Bchoose%20file%7D)

__Listing 17-5__AppleScript: Calling the `open` handler to test a droplet within Script Editor

1. `open {choose file}`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20app%20%3D%20Application.currentApplication%28%29%0Aapp.includeStandardAdditions%20%3D%20true%0Avar%20file%20%3D%20app.chooseFile%28%29%0AopenDocuments%28%5Bfile%5D%29)

__Listing 17-6__JavaScript: Calling the `openDocuments` handler to test a droplet within Script Editor

1. `var app = Application.currentApplication()`
2. `app.includeStandardAdditions = true`
3. `var file = app.chooseFile()`
4. `openDocuments([file])`

### Creating an AppleScript Droplet from a Script Editor Template

Script Editor includes several preconfigured AppleScript droplet templates, which solve the majority of droplet use cases.

> [!NOTE]
> 

__To create a droplet from a Script Editor template__

1. Launch Script Editor from `/Applications/Utilities/`.
2. Select File > New from Template > Droplets.
3. Choose a droplet template.

   Options include:

   - __Droplet with Settable Properties__—This template processes dropped files based on file type, extension, or type identifier. It also demonstrates how to include a user-configurable setting, which affects the behavior of the script.
   - __Recursive File Processing Droplet__—This template processes dropped files based on file type, extension, or type identifier. It is configured to detect files within dropped folders and their subfolders.
   - __Recursive Image File Processing Droplet__—This template processes image files matching specific file types, extensions, or type identifiers. It is configured to detect images within dropped folders and their subfolders.

   All of these templates are designed to serve as starting points for creating a droplet, and can be customized, as needed.

### Creating a Droplet to Process Files

In Listing 17-7 and Listing 17-8, the `open` handler and `openDocuments` function process dropped files based on file type, extension, or type identifier. The file types, extensions, and type identifiers supported by the handler are configurable in properties at the top of the script. If a dropped file matches the criteria you configure, then the file is passed to the `processItem()` handler, where you can add custom file processing code. These examples are not configured to process dropped folders.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=property%20theFileTypesToProcess%20%3A%20%7B%7D%20--%20For%20example%3A%20%7B%22PICT%22%2C%20%22JPEG%22%2C%20%22TIFF%22%2C%20%22GIFf%22%7D%0Aproperty%20theExtensionsToProcess%20%3A%20%7B%7D%20--%20For%20example%3A%20%7B%22txt%22%2C%20%22text%22%2C%20%22jpg%22%2C%20%22jpeg%22%7D%2C%20NOT%3A%20%7B%22.txt%22%2C%20%22.text%22%2C%20%22.jpg%22%2C%20%22.jpeg%22%7D%0Aproperty%20theTypeIdentifiersToProcess%20%3A%20%7B%7D%20--%20For%20example%3A%20%7B%22public.jpeg%22%2C%20%22public.tiff%22%2C%20%22public.png%22%7D%0A%0Aon%20open%20theDroppedItems%0A%20%20%20%20repeat%20with%20a%20from%201%20to%20count%20of%20theDroppedItems%0A%20%20%20%20%20%20%20%20set%20theCurrentItem%20to%20item%20a%20of%20theDroppedItems%0A%20%20%20%20%20%20%20%20tell%20application%20%22System%20Events%22%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20theExtension%20to%20name%20extension%20of%20theCurrentItem%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20theFileType%20to%20file%20type%20of%20theCurrentItem%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20theTypeIdentifier%20to%20type%20identifier%20of%20theCurrentItem%0A%20%20%20%20%20%20%20%20end%20tell%0A%20%20%20%20%20%20%20%20if%20%28%28theFileTypesToProcess%20contains%20theFileType%29%20or%20%28theExtensionsToProcess%20contains%20theExtension%29%20or%20%28theTypeIdentifiersToProcess%20contains%20theTypeIdentifier%29%29%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20processItem%28theCurrentItem%29%0A%20%20%20%20%20%20%20%20end%20if%0A%20%20%20%20end%20repeat%0Aend%20open%0A%0Aon%20processItem%28theItem%29%0A%20%20%20%20--%20NOTE%3A%20The%20variable%20theItem%20is%20a%20file%20reference%20in%20AppleScript%20alias%20format%0A%20%20%20%20--%20Add%20item%20processing%20code%20here%0Aend%20processItem)

__Listing 17-7__Handler that processes dropped files matching specific file types, extensions, or type identifiers

1. `property theFileTypesToProcess : {} -- For example: {"PICT", "JPEG", "TIFF", "GIFf"}`
2. `property theExtensionsToProcess : {} -- For example: {"txt", "text", "jpg", "jpeg"}, NOT: {".txt", ".text", ".jpg", ".jpeg"}`
3. `property theTypeIdentifiersToProcess : {} -- For example: {"public.jpeg", "public.tiff", "public.png"}`
5. `on open theDroppedItems`
6. `repeat with a from 1 to count of theDroppedItems`
7. `set theCurrentItem to item a of theDroppedItems`
8. `tell application "System Events"`
9. `set theExtension to name extension of theCurrentItem`
10. `set theFileType to file type of theCurrentItem`
11. `set theTypeIdentifier to type identifier of theCurrentItem`
12. `end tell`
13. `if ((theFileTypesToProcess contains theFileType) or (theExtensionsToProcess contains theExtension) or (theTypeIdentifiersToProcess contains theTypeIdentifier)) then`
14. `processItem(theCurrentItem)`
15. `end if`
16. `end repeat`
17. `end open`
19. `on processItem(theItem)`
20. `-- NOTE: The variable theItem is a file reference in AppleScript alias format`
21. `-- Add item processing code here`
22. `end processItem`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20SystemEvents%20%3D%20Application%28%22System%20Events%22%29%0Avar%20fileTypesToProcess%20%3D%20%5B%5D%20%2F%2F%20For%20example%3A%20%7B%22PICT%22%2C%20%22JPEG%22%2C%20%22TIFF%22%2C%20%22GIFf%22%7D%0Avar%20extensionsToProcess%20%3D%20%5B%5D%20%2F%2F%20For%20example%3A%20%7B%22txt%22%2C%20%22text%22%2C%20%22jpg%22%2C%20%22jpeg%22%7D%2C%20NOT%3A%20%7B%22.txt%22%2C%20%22.text%22%2C%20%22.jpg%22%2C%20%22.jpeg%22%7D%0Avar%20typeIdentifiersToProcess%20%3D%20%5B%5D%20%2F%2F%20For%20example%3A%20%7B%22public.jpeg%22%2C%20%22public.tiff%22%2C%20%22public.png%22%7D%0A%0Afunction%20openDocuments%28droppedItems%29%20%7B%0A%20%20%20%20for%20%28var%20item%20of%20droppedItems%29%20%7B%0A%20%20%20%20%20%20%20%20var%20alias%20%3D%20SystemEvents.aliases.byName%28item.toString%28%29%29%0A%20%20%20%20%20%20%20%20var%20extension%20%3D%20alias.nameExtension%28%29%0A%20%20%20%20%20%20%20%20var%20fileType%20%3D%20alias.fileType%28%29%0A%20%20%20%20%20%20%20%20var%20typeIdentifier%20%3D%20alias.typeIdentifier%28%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20%28fileTypesToProcess.includes%28fileType%29%20%7C%7C%20extensionsToProcess.includes%28extension%29%20%7C%7C%20typeIdentifiersToProcess.includes%28typeIdentifier%29%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20processItem%28item%29%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%7D%0A%0Afunction%20processItem%28item%29%20%7B%0A%20%20%20%20%2F%2F%20NOTE%3A%20The%20variable%20item%20is%20an%20instance%20of%20the%20Path%20object%0A%20%20%20%20%2F%2F%20Add%20item%20processing%20code%20here%0A%7D)

__Listing 17-8__Function that processes dropped files matching specific file types, extensions, or type identifiers

1. `var SystemEvents = Application("System Events")`
2. `var fileTypesToProcess = [] // For example: {"PICT", "JPEG", "TIFF", "GIFf"}`
3. `var extensionsToProcess = [] // For example: {"txt", "text", "jpg", "jpeg"}, NOT: {".txt", ".text", ".jpg", ".jpeg"}`
4. `var typeIdentifiersToProcess = [] // For example: {"public.jpeg", "public.tiff", "public.png"}`
6. `function openDocuments(droppedItems) {`
7. `for (var item of droppedItems) {`
8. `var alias = SystemEvents.aliases.byName(item.toString())`
9. `var extension = alias.nameExtension()`
10. `var fileType = alias.fileType()`
11. `var typeIdentifier = alias.typeIdentifier()`
12. `if (fileTypesToProcess.includes(fileType) || extensionsToProcess.includes(extension) || typeIdentifiersToProcess.includes(typeIdentifier)) {`
13. `processItem(item)`
14. `}`
15. `}`
16. `}`
18. `function processItem(item) {`
19. `// NOTE: The variable item is an instance of the Path object`
20. `// Add item processing code here`
21. `}`

### Creating a Droplet to Process Files and Folders

In Listing 17-9 and Listing 17-10, the `open` handler and `openDocuments` function loop through any dropped files and folders.

For each dropped file, the script calls the `processFile()` handler, which determines whether the file matches specific file types, extensions, and type identifiers. The file types, extensions, and type identifiers supported by the handler are configurable in properties at the top of the script. If there’s a match, then any custom file processing code you add runs.

The script passes each dropped folder to the `processFolder()`, which retrieves a list of files and subfolders within the dropped folder. The `processFolder()` handler recursively calls itself to process any additional subfolders. It calls the `processFile()` handler to process any detected files. If necessary, you can add custom folder processing code to the `processFolder()` handler.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=property%20theFileTypesToProcess%20%3A%20%7B%7D%20--%20I.e.%20%7B%22PICT%22%2C%20%22JPEG%22%2C%20%22TIFF%22%2C%20%22GIFf%22%7D%0Aproperty%20theExtensionsToProcess%20%3A%20%7B%7D%20--%20I.e.%20%7B%22txt%22%2C%20%22text%22%2C%20%22jpg%22%2C%20%22jpeg%22%7D%2C%20NOT%3A%20%7B%22.txt%22%2C%20%22.text%22%2C%20%22.jpg%22%2C%20%22.jpeg%22%7D%0Aproperty%20theTypeIdentifiersToProcess%20%3A%20%7B%7D%20--%20I.e.%20%7B%22public.jpeg%22%2C%20%22public.tiff%22%2C%20%22public.png%22%7D%0A%0Aon%20open%20theDroppedItems%0A%20%20%20%20repeat%20with%20a%20from%201%20to%20count%20of%20theDroppedItems%0A%20%20%20%20%20%20%20%20set%20theCurrentItem%20to%20item%20a%20of%20theDroppedItems%0A%20%20%20%20%20%20%20%20tell%20application%20%22Finder%22%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20isFolder%20to%20folder%20%28theCurrentItem%20as%20string%29%20exists%0A%20%20%20%20%20%20%20%20end%20tell%0A%0A%20%20%20%20%20%20%20--%20Process%20a%20dropped%20folder%0A%20%20%20%20%20%20%20if%20isFolder%20%3D%20true%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20processFolder%28theCurrentItem%29%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20--%20Process%20a%20dropped%20file%0A%20%20%20%20%20%20%20else%0A%20%20%20%20%20%20%20%20%20%20%20%20processFile%28theCurrentItem%29%0A%20%20%20%20%20%20%20end%20if%0A%20%20%20%20end%20repeat%0Aend%20open%0A%0Aon%20processFolder%28theFolder%29%0A%20%20%20%20--%20NOTE%3A%20The%20variable%20theFolder%20is%20a%20folder%20reference%20in%20AppleScript%20alias%20format%0A%20%20%20%20--%20Retrieve%20a%20list%20of%20any%20visible%20items%20in%20the%20folder%0A%20%20%20%20set%20theFolderItems%20to%20list%20folder%20theFolder%20without%20invisibles%0A%0A%20%20%20%20--%20Loop%20through%20the%20visible%20folder%20items%0A%20%20%20%20repeat%20with%20a%20from%201%20to%20count%20of%20theFolderItems%0A%20%20%20%20%20%20%20%20set%20theCurrentItem%20to%20%28%28theFolder%20as%20string%29%20%26%20%28item%20a%20of%20theFolderItems%29%29%20as%20alias%0A%20%20%20%20%20%20%20%20open%20%7BtheCurrentItem%7D%0A%20%20%20%20end%20repeat%0A%20%20%20%20--%20Add%20additional%20folder%20processing%20code%20here%0Aend%20processFolder%0A%0Aon%20processFile%28theItem%29%0A%20%20%20%20--%20NOTE%3A%20variable%20theItem%20is%20a%20file%20reference%20in%20AppleScript%20alias%20format%0A%20%20%20%20tell%20application%20%22System%20Events%22%0A%20%20%20%20%20%20%20%20set%20theExtension%20to%20name%20extension%20of%20theItem%0A%20%20%20%20%20%20%20%20set%20theFileType%20to%20file%20type%20of%20theItem%0A%20%20%20%20%20%20%20%20set%20theTypeIdentifier%20to%20type%20identifier%20of%20theItem%0A%20%20%20%20end%20tell%0A%20%20%20%20if%20%28%28theFileTypesToProcess%20contains%20theFileType%29%20or%20%28theExtensionsToProcess%20contains%20theExtension%29%20or%20%28theTypeIdentifiersToProcess%20contains%20theTypeIdentifier%29%29%20then%0A%20%20%20%20%20%20%20%20--%20Add%20file%20processing%20code%20here%0A%20%20%20%20%20%20%20%20display%20dialog%20theItem%20as%20string%0A%20%20%20%20end%20if%0Aend%20processFile)

__Listing 17-9__Handler that processes dropped folders and files

1. `property theFileTypesToProcess : {} -- I.e. {"PICT", "JPEG", "TIFF", "GIFf"}`
2. `property theExtensionsToProcess : {} -- I.e. {"txt", "text", "jpg", "jpeg"}, NOT: {".txt", ".text", ".jpg", ".jpeg"}`
3. `property theTypeIdentifiersToProcess : {} -- I.e. {"public.jpeg", "public.tiff", "public.png"}`
5. `on open theDroppedItems`
6. `repeat with a from 1 to count of theDroppedItems`
7. `set theCurrentItem to item a of theDroppedItems`
8. `tell application "Finder"`
9. `set isFolder to folder (theCurrentItem as string) exists`
10. `end tell`
12. `-- Process a dropped folder`
13. `if isFolder = true then`
14. `processFolder(theCurrentItem)`
16. `-- Process a dropped file`
17. `else`
18. `processFile(theCurrentItem)`
19. `end if`
20. `end repeat`
21. `end open`
23. `on processFolder(theFolder)`
24. `-- NOTE: The variable theFolder is a folder reference in AppleScript alias format`
25. `-- Retrieve a list of any visible items in the folder`
26. `set theFolderItems to list folder theFolder without invisibles`
28. `-- Loop through the visible folder items`
29. `repeat with a from 1 to count of theFolderItems`
30. `set theCurrentItem to ((theFolder as string) & (item a of theFolderItems)) as alias`
31. `open {theCurrentItem}`
32. `end repeat`
33. `-- Add additional folder processing code here`
34. `end processFolder`
36. `on processFile(theItem)`
37. `-- NOTE: variable theItem is a file reference in AppleScript alias format`
38. `tell application "System Events"`
39. `set theExtension to name extension of theItem`
40. `set theFileType to file type of theItem`
41. `set theTypeIdentifier to type identifier of theItem`
42. `end tell`
43. `if ((theFileTypesToProcess contains theFileType) or (theExtensionsToProcess contains theExtension) or (theTypeIdentifiersToProcess contains theTypeIdentifier)) then`
44. `-- Add file processing code here`
45. `display dialog theItem as string`
46. `end if`
47. `end processFile`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20SystemEvents%20%3D%20Application%28%22System%20Events%22%29%0Avar%20fileManager%20%3D%20%24.NSFileManager.defaultManager%0Avar%20currentApp%20%3D%20Application.currentApplication%28%29%0AcurrentApp.includeStandardAdditions%20%3D%20true%0A%0Avar%20fileTypesToProcess%20%3D%20%5B%5D%20%2F%2F%20For%20example%3A%20%7B%22PICT%22%2C%20%22JPEG%22%2C%20%22TIFF%22%2C%20%22GIFf%22%7D%0Avar%20extensionsToProcess%20%3D%20%5B%5D%20%2F%2F%20For%20example%3A%20%7B%22txt%22%2C%20%22text%22%2C%20%22jpg%22%2C%20%22jpeg%22%7D%2C%20NOT%3A%20%7B%22.txt%22%2C%20%22.text%22%2C%20%22.jpg%22%2C%20%22.jpeg%22%7D%0Avar%20typeIdentifiersToProcess%20%3D%20%5B%5D%20%2F%2F%20For%20example%3A%20%7B%22public.jpeg%22%2C%20%22public.tiff%22%2C%20%22public.png%22%7D%0A%0Afunction%20openDocuments%28droppedItems%29%20%7B%0A%20%20%20%20for%20%28var%20item%20of%20droppedItems%29%20%7B%0A%20%20%20%20%20%20%20%20var%20isDir%20%3D%20Ref%28%29%0A%20%20%20%20%20%20%20%20if%20%28fileManager.fileExistsAtPathIsDirectory%28item.toString%28%29%2C%20isDir%29%20%26%26%20isDir%5B0%5D%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20processFolder%28item%29%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20else%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20processFile%28item%29%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%7D%0A%0Afunction%20processFolder%28folder%29%20%7B%0A%20%20%20%20%2F%2F%20NOTE%3A%20The%20variable%20folder%20is%20an%20instance%20of%20the%20Path%20object%0A%20%20%20%20var%20folderString%20%3D%20folder.toString%28%29%0A%0A%20%20%20%20%2F%2F%20Retrieve%20a%20list%20of%20any%20visible%20items%20in%20the%20folder%0A%20%20%20%20var%20folderItems%20%3D%20currentApp.listFolder%28folder%2C%20%7B%20invisibles%3A%20false%20%7D%29%0A%0A%20%20%20%20%2F%2F%20Loop%20through%20the%20visible%20folder%20items%0A%20%20%20%20for%20%28var%20item%20of%20folderItems%29%20%7B%0A%20%20%20%20%20%20%20%20var%20currentItem%20%3D%20%60%24%7BfolderString%7D%2F%24%7Bitem%7D%60%0A%20%20%20%20%20%20%20%20openDocuments%28%5BcurrentItem%5D%29%0A%20%20%20%20%7D%0A%20%20%20%20%2F%2F%20Add%20additional%20folder%20processing%20code%20here%0A%7D%0A%0Afunction%20processFile%28file%29%20%7B%0A%20%20%20%20%2F%2F%20NOTE%3A%20The%20variable%20file%20is%20an%20instance%20of%20the%20Path%20object%0A%20%20%20%20var%20fileString%20%3D%20file.toString%28%29%0A%20%20%20%20var%20alias%20%3D%20SystemEvents.aliases.byName%28fileString%29%0A%20%20%20%20var%20extension%20%3D%20alias.nameExtension%28%29%0A%20%20%20%20var%20fileType%20%3D%20alias.fileType%28%29%0A%20%20%20%20var%20typeIdentifier%20%3D%20alias.typeIdentifier%28%29%0A%20%20%20%20if%20%28fileTypesToProcess.includes%28fileType%29%20%7C%7C%20extensionsToProcess.includes%28extension%29%20%7C%7C%20typeIdentifiersToProcess.includes%28typeIdentifier%29%29%20%7B%0A%20%20%20%20%20%20%20%20%2F%2F%20Add%20file%20processing%20code%20here%0A%20%20%20%20%7D%0A%7D%0A)

__Listing 17-10__Function that processes dropped folders and files

1. `var SystemEvents = Application("System Events")`
2. `var fileManager = $.NSFileManager.defaultManager`
3. `var currentApp = Application.currentApplication()`
4. `currentApp.includeStandardAdditions = true`
6. `var fileTypesToProcess = [] // For example: {"PICT", "JPEG", "TIFF", "GIFf"}`
7. `var extensionsToProcess = [] // For example: {"txt", "text", "jpg", "jpeg"}, NOT: {".txt", ".text", ".jpg", ".jpeg"}`
8. `var typeIdentifiersToProcess = [] // For example: {"public.jpeg", "public.tiff", "public.png"}`
10. `function openDocuments(droppedItems) {`
11. `for (var item of droppedItems) {`
12. `var isDir = Ref()`
13. `if (fileManager.fileExistsAtPathIsDirectory(item.toString(), isDir) && isDir[0]) {`
14. `processFolder(item)`
15. `}`
16. `else {`
17. `processFile(item)`
18. `}`
19. `}`
20. `}`
22. `function processFolder(folder) {`
23. `// NOTE: The variable folder is an instance of the Path object`
24. `var folderString = folder.toString()`
26. `// Retrieve a list of any visible items in the folder`
27. `var folderItems = currentApp.listFolder(folder, { invisibles: false })`
29. `// Loop through the visible folder items`
30. `for (var item of folderItems) {`
31. `` var currentItem = `${folderString}/${item}` ``
32. `openDocuments([currentItem])`
33. `}`
34. `// Add additional folder processing code here`
35. `}`
37. `function processFile(file) {`
38. `// NOTE: The variable file is an instance of the Path object`
39. `var fileString = file.toString()`
40. `var alias = SystemEvents.aliases.byName(fileString)`
41. `var extension = alias.nameExtension()`
42. `var fileType = alias.fileType()`
43. `var typeIdentifier = alias.typeIdentifier()`
44. `if (fileTypesToProcess.includes(fileType) || extensionsToProcess.includes(extension) || typeIdentifiersToProcess.includes(typeIdentifier)) {`
45. `// Add file processing code here`
46. `}`
47. `}`

[Reading and Writing Files](ReadandWriteFiles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqnjyfvjvomi)

[Watching Folders](WatchFolders.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqmzzfvjvomi)
