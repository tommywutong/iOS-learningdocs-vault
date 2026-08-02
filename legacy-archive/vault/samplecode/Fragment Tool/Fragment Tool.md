---
title: Fragment Tool
apple_id: DTS10000572
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/Fragment_Tool/Introduction/Intro.html
archived_at: '2026-07-18T03:08:54.433610Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](AppleEventStuff.c.md)

# Fragment Tool

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-30 Demonstrates manipulation of code fragments; combining and separating; viewing and editing information associated with each. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

"Fragment Tool" is a simple application designed to allow basic manipulation of code fragments. It allows you to combine or separate several code fragments, and view and edit various pieces of information associated with each code fragment. It demonstrates several Toolbox Managers and several common, and some not so common, features of these Managers: \* Code Fragment Manager -Loading and preparing a code fragment from the data fork of a file. -Retrieving a list of exported symbols from a prepared code fragment. -Interpreting and manipulating the 'cfrg' resource. \* Drag Manager -Creating an application specific file when content is dragged to the Finder. -Using drag data which makes sense only to your own application. -Dragable lists. \* List Manager -Both 68K and PowerPC native click loop procedures (there's a gotcha with a native click loop procedure). -Non standard text styles in lists. -Dragable lists. (Okay, I've mentioned that already, but I couldn't decide what heading it under.) -Using lists in document windows. \* Resource Manager -Opening resource forks without loading all preloaded resources. This is particularly important when opening application resource forks that may contain preloaded 'CODE' resources. \* Dialog Manager -Non standard text styles in a dialog, including popup menus and editable text items. -Support a number of moveable modal dialogs in an application. It also demonstrates: -How to properly support the standard event loop, including basic support for multiple monitors. -How to safely check if a system feature is available in a native PowerPC application (Gestalt isn't always enough). -A stream 'class' that allows you to stream data elements into a memory block, and then retrieve the elements later. -An example of using function pointers for your own purposes. -How to get access to the Temporary Items Folder and use it to keep temporary files. This is not intended to be a definitive 'document' on how to implement these features, but illustrates one approach you can take. Keywords: CFM, Code Fragment Manager

[Next](AppleEventStuff.c.md)

