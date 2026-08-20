---
title: Mac Automation Scripting Guide
apple_id: TP40016239
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/ReadandWriteFiles.html
archived_at: '2026-07-15T07:46:07.598112Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Mac Automation Scripting Guide](index.md)



## Reading and Writing Files

Scripts are often designed to write data to files such as logs or backups. The Standard Additions scripting addition contains a number of commands that make it possible to read and write files.

### Writing to a File

The handlers in Listing 16-1 and Listing 16-2 safely write data to disk, creating a new file if the targeted file doesn’t already exist. Provide the text to write, a target file path, and indicate whether to overwrite existing content. If you choose not to overwrite existing content, then the text provided is appended to any existing content.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=on%20writeTextToFile%28theText%2C%20theFile%2C%20overwriteExistingContent%29%0A%20%20%20%20try%0A%0A%20%20%20%20%20%20%20%20--%20Convert%20the%20file%20to%20a%20string%0A%20%20%20%20%20%20%20%20set%20theFile%20to%20theFile%20as%20string%0A%0A%20%20%20%20%20%20%20%20--%20Open%20the%20file%20for%20writing%0A%20%20%20%20%20%20%20%20set%20theOpenedFile%20to%20open%20for%20access%20file%20theFile%20with%20write%20permission%0A%0A%20%20%20%20%20%20%20%20--%20Clear%20the%20file%20if%20content%20should%20be%20overwritten%0A%20%20%20%20%20%20%20%20if%20overwriteExistingContent%20is%20true%20then%20set%20eof%20of%20theOpenedFile%20to%200%0A%0A%20%20%20%20%20%20%20%20--%20Write%20the%20new%20content%20to%20the%20file%0A%20%20%20%20%20%20%20%20write%20theText%20to%20theOpenedFile%20starting%20at%20eof%0A%0A%20%20%20%20%20%20%20%20--%20Close%20the%20file%0A%20%20%20%20%20%20%20%20close%20access%20theOpenedFile%0A%0A%20%20%20%20%20%20%20%20--%20Return%20a%20boolean%20indicating%20that%20writing%20was%20successful%0A%20%20%20%20%20%20%20%20return%20true%0A%0A%20%20%20%20%20%20%20%20--%20Handle%20a%20write%20error%0A%20%20%20%20on%20error%0A%0A%20%20%20%20%20%20%20%20--%20Close%20the%20file%0A%20%20%20%20%20%20%20%20try%0A%20%20%20%20%20%20%20%20%20%20%20%20close%20access%20file%20theFile%0A%20%20%20%20%20%20%20%20end%20try%0A%0A%20%20%20%20%20%20%20%20--%20Return%20a%20boolean%20indicating%20that%20writing%20failed%0A%20%20%20%20%20%20%20%20return%20false%0A%20%20%20%20end%20try%0Aend%20writeTextToFile)

__Listing 16-1__AppleScript: Handler that writes text to a file

1. `on writeTextToFile(theText, theFile, overwriteExistingContent)`
2. `try`
4. `-- Convert the file to a string`
5. `set theFile to theFile as string`
7. `-- Open the file for writing`
8. `set theOpenedFile to open for access file theFile with write permission`
10. `-- Clear the file if content should be overwritten`
11. `if overwriteExistingContent is true then set eof of theOpenedFile to 0`
13. `-- Write the new content to the file`
14. `write theText to theOpenedFile starting at eof`
16. `-- Close the file`
17. `close access theOpenedFile`
19. `-- Return a boolean indicating that writing was successful`
20. `return true`
22. `-- Handle a write error`
23. `on error`
25. `-- Close the file`
26. `try`
27. `close access file theFile`
28. `end try`
30. `-- Return a boolean indicating that writing failed`
31. `return false`
32. `end try`
33. `end writeTextToFile`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20app%20%3D%20Application.currentApplication%28%29%0Aapp.includeStandardAdditions%20%3D%20true%0A%0Afunction%20writeTextToFile%28text%2C%20file%2C%20overwriteExistingContent%29%20%7B%0A%20%20%20%20try%20%7B%0A%0A%20%20%20%20%20%20%20%20%2F%2F%20Convert%20the%20file%20to%20a%20string%0A%20%20%20%20%20%20%20%20var%20fileString%20%3D%20file.toString%28%29%0A%0A%20%20%20%20%20%20%20%20%2F%2F%20Open%20the%20file%20for%20writing%0A%20%20%20%20%20%20%20%20var%20openedFile%20%3D%20app.openForAccess%28Path%28fileString%29%2C%20%7B%20writePermission%3A%20true%20%7D%29%0A%0A%20%20%20%20%20%20%20%20%2F%2F%20Clear%20the%20file%20if%20content%20should%20be%20overwritten%0A%20%20%20%20%20%20%20%20if%20%28overwriteExistingContent%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20app.setEof%28openedFile%2C%20%7B%20to%3A%200%20%7D%29%0A%20%20%20%20%20%20%20%20%7D%0A%0A%20%20%20%20%20%20%20%20%2F%2F%20Write%20the%20new%20content%20to%20the%20file%0A%20%20%20%20%20%20%20%20app.write%28text%2C%20%7B%20to%3A%20openedFile%2C%20startingAt%3A%20app.getEof%28openedFile%29%20%7D%29%0A%0A%20%20%20%20%20%20%20%20%2F%2F%20Close%20the%20file%0A%20%20%20%20%20%20%20%20app.closeAccess%28openedFile%29%0A%0A%20%20%20%20%20%20%20%20%2F%2F%20Return%20a%20boolean%20indicating%20that%20writing%20was%20successful%0A%20%20%20%20%20%20%20%20return%20true%0A%20%20%20%20%7D%0A%20%20%20%20%C5%93%20%28error%29%20%7B%0A%0A%20%20%20%20%20%20%20%20try%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%2F%2F%20Close%20the%20file%0A%20%20%20%20%20%20%20%20%20%20%20%20app.closeAccess%28file%29%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20catch%28error%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%2F%2F%20Report%20the%20error%20is%20closing%20failed%0A%20%20%20%20%20%20%20%20%20%20%20%20console.log%28%60Couldn%27t%20close%20file%3A%20%24%7Berror%7D%60%29%0A%20%20%20%20%20%20%20%20%7D%0A%0A%20%20%20%20%20%20%20%20%2F%2F%20Return%20a%20boolean%20indicating%20that%20writing%20was%20successful%0A%20%20%20%20%20%20%20%20return%20false%0A%20%20%20%20%7D%0A%7D)

__Listing 16-2__JavaScript: Function that writes text to a file

1. `var app = Application.currentApplication()`
2. `app.includeStandardAdditions = true`
4. `function writeTextToFile(text, file, overwriteExistingContent) {`
5. `try {`
7. `// Convert the file to a string`
8. `var fileString = file.toString()`
10. `// Open the file for writing`
11. `var openedFile = app.openForAccess(Path(fileString), { writePermission: true })`
13. `// Clear the file if content should be overwritten`
14. `if (overwriteExistingContent) {`
15. `app.setEof(openedFile, { to: 0 })`
16. `}`
18. `// Write the new content to the file`
19. `app.write(text, { to: openedFile, startingAt: app.getEof(openedFile) })`
21. `// Close the file`
22. `app.closeAccess(openedFile)`
24. `// Return a boolean indicating that writing was successful`
25. `return true`
26. `}`
27. `catch(error) {`
29. `try {`
30. `// Close the file`
31. `app.closeAccess(file)`
32. `}`
33. `catch(error) {`
34. `// Report the error is closing failed`
35. `` console.log(`Couldn't close file: ${error}`) ``
36. `}`
38. `// Return a boolean indicating that writing was successful`
39. `return false`
40. `}`
41. `}`

Listing 16-3 and Listing 16-4 show how to call the handlers in Listing 16-1 and Listing 16-2 to write text content to a file on the Desktop, replacing any existing content in the file.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20this_story%20to%20%22Once%20upon%20a%20time%20in%20Silicon%20Valley...%22%0Aset%20theFile%20to%20%28%28%28path%20to%20desktop%20folder%29%20as%20string%29%20%26%20%22MY%20STORY.txt%22%29%0AwriteTextToFile%28this_story%2C%20theFile%2C%20true%29)

__Listing 16-3__AppleScript: Calling a handler to write text to a file

1. `set this_story to "Once upon a time in Silicon Valley..."`
2. `set theFile to (((path to desktop folder) as string) & "MY STORY.txt")`
3. `writeTextToFile(this_story, theFile, true)`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20story%20%3D%20%22Once%20upon%20a%20time%20in%20Silicon%20Valley...%22%0Avar%20desktopString%20%3D%20app.pathTo%28%22desktop%22%29.toString%28%29%0Avar%20file%20%3D%20%60%24%7BdesktopString%7D%2FMY%20STORY.txt%60%0AwriteTextToFile%28story%2C%20file%2C%20true%29)

__Listing 16-4__JavaScript: Calling a function to write text to a file

1. `var story = "Once upon a time in Silicon Valley..."`
2. `var desktopString = app.pathTo("desktop").toString()`
3. `` var file = `${desktopString}/MY STORY.txt` ``
4. `writeTextToFile(story, file, true)`

Listing 16-5 and Listing 16-6 show how Listing 16-1 and Listing 16-2 could be called to insert dated log entries into a log file.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theText%20to%20%28%28current%20date%29%20as%20string%29%20%26%20space%20%26%20%22STATUS%20OK%22%20%26%20return%0Aset%20theFile%20to%20%28%28%28path%20to%20desktop%20folder%29%20as%20string%29%20%26%20%22MY%20LOG%20FILE.log%22%29%0AwriteTextToFile%28theText%2C%20theFile%2C%20false%29)

__Listing 16-5__AppleScript: Calling a handler to write an entry to a log file

1. `set theText to ((current date) as string) & space & "STATUS OK" & return`
2. `set theFile to (((path to desktop folder) as string) & "MY LOG FILE.log")`
3. `writeTextToFile(theText, theFile, false)`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20dateString%20%3D%20Date%28%29.toString%28%29%0Avar%20desktopString%20%3D%20app.pathTo%28%22desktop%22%29.toString%28%29%0Avar%20text%20%3D%20%60%24%7BdateString%7D%20STATUS%20OK%5Cn%5Cn%60%0Avar%20file%20%3D%20%60%24%7BdesktopString%7D%2FMY%20LOG%20FILE.log%60%0AwriteTextToFile%28text%2C%20file%2C%20false%29)

__Listing 16-6__JavaScript: Calling a function to write an entry to a log file

1. `var dateString = Date().toString()`
2. `var desktopString = app.pathTo("desktop").toString()`
3. `` var text = `${dateString} STATUS OK\n\n` ``
4. `` var file = `${desktopString}/MY LOG FILE.log` ``
5. `writeTextToFile(text, file, false)`

In practice, this technique could be used to maintain a log when script errors occur. Listing 16-7 and Listing 16-8 are try statements, which can be wrapped around custom script code in order to log any script errors to a file in the `~/Library/Logs/` folder of the current user’s home directory.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=try%0A%20%20%20%20--%20Your%20custom%20script%20code%20goes%20here%0Aon%20error%20theErrorMessage%20number%20theErrorNumber%0A%20%20%20%20set%20theError%20to%20%22Error%3A%20%22%20%26%20theErrorNumber%20%26%20%22.%20%22%20%26%20theErrorMessage%20%26%20return%0A%20%20%20%20set%20theLogFile%20to%20%28%28path%20to%20library%20folder%20from%20user%20domain%29%20as%20string%29%20%26%20%22Logs%3AScript%20Error%20Log.log%22%0A%20%20%20%20my%20writeTextToFile%28theError%2C%20theLogFile%2C%20false%29%0Aend%20try)

__Listing 16-7__AppleScript: Example of a try statement that writes an entry to a log file when an error occurs

1. `try`
2. `-- Your custom script code goes here`
3. `on error theErrorMessage number theErrorNumber`
4. `set theError to "Error: " & theErrorNumber & ". " & theErrorMessage & return`
5. `set theLogFile to ((path to library folder from user domain) as string) & "Logs:Script Error Log.log"`
6. `my writeTextToFile(theError, theLogFile, false)`
7. `end try`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=try%20%7B%0A%20%20%20%20%2F%2F%20Your%20custom%20script%20code%20goes%20here%0A%7D%0Acatch%20%28error%29%20%7B%0A%20%20%20%20var%20errorString%20%3D%20%60Error%3A%20%24%7Berror.message%7D%5Cn%5Cn%60%0A%20%20%20%20var%20logFile%20%3D%20app.pathTo%28%22library%20folder%22%2C%20%7B%20from%3A%20%22user%20domain%22%20%7D%29.toString%28%29%20%2B%20%22%2FLogs%2FScript%20Error%20Log.log%22%0A%20%20%20%20writeTextToFile%28errorString%2C%20logFile%2C%20false%29%0A%7D)

__Listing 16-8__JavaScript: Example of a try statement that writes an entry to a log file when an error occurs

1. `try {`
2. `// Your custom script code goes here`
3. `}`
4. `catch (error) {`
5. `` var errorString = `Error: ${error.message}\n\n` ``
6. `var logFile = app.pathTo("library folder", { from: "user domain" }).toString() + "/Logs/Script Error Log.log"`
7. `writeTextToFile(errorString, logFile, false)`
8. `}`

### Reading a File

The handlers in Listing 16-9 and Listing 16-10 read the contents of a specified file.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=on%20readFile%28theFile%29%0A%20%20%20%20--%20Convert%20the%20file%20to%20a%20string%0A%20%20%20%20set%20theFile%20to%20theFile%20as%20string%0A%0A%20%20%20%20--%20Read%20the%20file%20and%20return%20its%20contents%0A%20%20%20%20return%20read%20file%20theFile%0Aend%20readFile)

__Listing 16-9__AppleScript: Handler that reads the contents of a file

1. `on readFile(theFile)`
2. `-- Convert the file to a string`
3. `set theFile to theFile as string`
5. `-- Read the file and return its contents`
6. `return read file theFile`
7. `end readFile`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20app%20%3D%20Application.currentApplication%28%29%0Aapp.includeStandardAdditions%20%3D%20true%0A%0Afunction%20readFile%28file%29%20%7B%0A%20%20%20%20%2F%2F%20Convert%20the%20file%20to%20a%20string%0A%20%20%20%20var%20fileString%20%3D%20file.toString%28%29%0A%0A%20%20%20%20%2F%2F%20Read%20the%20file%20and%20return%20its%20contents%0A%20%20%20%20return%20app.read%28Path%28fileString%29%29%0A%7D)

__Listing 16-10__JavaScript: Function that reads the contents of a file

1. `var app = Application.currentApplication()`
2. `app.includeStandardAdditions = true`
4. `function readFile(file) {`
5. `// Convert the file to a string`
6. `var fileString = file.toString()`
8. `// Read the file and return its contents`
9. `return app.read(Path(fileString))`
10. `}`

Listing 16-11 and Listing 16-12 show how to call the handlers in Listing 16-9 and Listing 16-10 to read a specified text file.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theFile%20to%20choose%20file%20of%20type%20%22txt%22%20with%20prompt%20%22Please%20select%20a%20text%20file%20to%20read%3A%22%0AreadFile%28theFile%29)

__Listing 16-11__AppleScript: Calling a handler to read the contents of a file

1. `set theFile to choose file of type "txt" with prompt "Please select a text file to read:"`
2. `readFile(theFile)`
3. `--> Result: "Contents of the chosen file."`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20file%20%3D%20app.chooseFile%28%7B%0A%20%20%20%20ofType%3A%20%22txt%22%2C%0A%20%20%20%20withPrompt%3A%20%22Please%20select%20a%20text%20file%20to%20read%3A%22%0A%7D%29%0A%0AreadFile%28file%29)

__Listing 16-12__JavaScript: Calling a function to read the contents of a file

1. `var file = app.chooseFile({`
2. `ofType: "txt",`
3. `withPrompt: "Please select a text file to read:"`
4. `})`
6. `readFile(file)`
7. `// Result: "Contents of the chosen file."`

### Reading and Splitting a File

The handlers in Listing 16-13 and Listing 16-14 read the contents of a specified text file, using a delimiter to split it into a list.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=on%20readAndSplitFile%28theFile%2C%20theDelimiter%29%0A%20%20%20%20--%20Convert%20the%20file%20to%20a%20string%0A%20%20%20%20set%20theFile%20to%20theFile%20as%20string%0A%0A%20%20%20%20--%20Read%20the%20file%20using%20a%20specific%20delimiter%20and%20return%20the%20results%0A%20%20%20%20return%20read%20file%20theFile%20using%20delimiter%20%7BtheDelimiter%7D%0Aend%20readAndSplitFile)

__Listing 16-13__AppleScript: Handler for reading and splitting the contents of a file based on a delimiter

1. `on readAndSplitFile(theFile, theDelimiter)`
2. `-- Convert the file to a string`
3. `set theFile to theFile as string`
5. `-- Read the file using a specific delimiter and return the results`
6. `return read file theFile using delimiter {theDelimiter}`
7. `end readAndSplitFile`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20app%20%3D%20Application.currentApplication%28%29%0Aapp.includeStandardAdditions%20%3D%20true%0A%0Afunction%20readAndSplitFile%28file%2C%20delimiter%29%20%7B%0A%20%20%20%20%2F%2F%20Convert%20the%20file%20to%20a%20string%0A%20%20%20%20var%20fileString%20%3D%20file.toString%28%29%0A%0A%20%20%20%20%2F%2F%20Read%20the%20file%20using%20a%20specific%20delimiter%20and%20return%20the%20results%0A%20%20%20%20return%20app.read%28Path%28fileString%29%2C%20%7B%20usingDelimiter%3A%20delimiter%20%7D%29%0A%7D)

__Listing 16-14__JavaScript: Function for reading and splitting the contents of a file based on a delimiter

1. `var app = Application.currentApplication()`
2. `app.includeStandardAdditions = true`
4. `function readAndSplitFile(file, delimiter) {`
5. `// Convert the file to a string`
6. `var fileString = file.toString()`
8. `// Read the file using a specific delimiter and return the results`
9. `return app.read(Path(fileString), { usingDelimiter: delimiter })`
10. `}`

Listing 16-15 and Listing 16-16 shows how to call the handlers in Listing 16-13 and Listing 16-14 to read the paragraphs of a chosen log file.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theFile%20to%20choose%20file%20of%20type%20%22log%22%20with%20prompt%20%22Please%20select%20a%20log%20file%3A%22%0AreadAndSplitFile%28theFile%2C%20return%29)

__Listing 16-15__AppleScript: Calling a handler to read and split the contents of a file based on a delimiter

1. `set theFile to choose file of type "log" with prompt "Please select a log file:"`
2. `readAndSplitFile(theFile, return)`
3. `--> Result: {"Log entry 1", "Log entry 2", ... }`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20file%20%3D%20app.chooseFile%28%7B%0A%20%20%20%20ofType%3A%20%22log%22%2C%0A%20%20%20%20withPrompt%3A%20%22Please%20select%20a%20log%20file%3A%22%0A%7D%29%0AreadAndSplitFile%28file%2C%20%22%5Cn%22%29)

__Listing 16-16__JavaScript: Calling a function to read and split the contents of a file based on a delimiter

1. `var file = app.chooseFile({`
2. `ofType: "log",`
3. `withPrompt: "Please select a log file:"`
4. `})`
5. `readAndSplitFile(file, "\n")`
6. `// Result: ["Log entry 1", "Log entry 2", ...]`

[Referencing Files and Folders](ReferenceFilesandFolders.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqmzufvjvomi)

[Processing Dropped Files and Folders](ProcessDroppedFilesandFolders.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqnjtfvjvomi)
