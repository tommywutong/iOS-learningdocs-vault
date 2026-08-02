---
title: AttachAScript
apple_id: DTS10003911
resource_type: Sample Code
platform: macOS
topic: Interapplication Communication
technology: Foundation
published: '2011-07-14'
source_url: https://developer.apple.com/library/archive/samplecode/AttachAScript/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:01:13.852153Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AttachAScript](AttachAScript.md)


[Next](main.m.md)[Previous](AttachAScript.md)

# ReadMe.txt

```
AttachAScript
=============

ABOUT:

If your application needs to communicate with other applications or processes, it can use AppleScript as a communication layer. Using the techniques described here, the included scripts handle all of the communication details while your application just makes calls to the scripting machinery. This design allows you to modularize the part of your application concerned with interprocess communication. The scripts are stored in the application's Resources folder and can be tuned in the field for particular needs and requirements, potentially by end users, without needing to recompile the application.

This sample targets the iTunes application, using remote Apple events over a network. The scripts handle all of the details involved in communicating with iTunes, while the program provides the user interface.


BUILDING:

Two additional build phases have been added to this project.  These include a shell script phase that compiles the AppleScripts used in this example using the command:

 osacompile -d -o AttachedScripts.scpt AttachedScripts.applescript

and there is an additional copy files build phase that copies the script text and the compiled script into the application's resources folder.


RUNNING:

This application uses remote apple events to connect to the iTunes application.  Before you run this application you must turn on Remote Apple Events in the Sharing pane of the System Preferences application on the computer running the copy of iTunes you wish to control.

When you run this application the first thing it will do is present a window that you can use to select the remote copy of iTunes.

===========================================================================
BUILD REQUIREMENTS

Xcode 3.2, Mac OS X 10.6 Snow Leopard or later.

===========================================================================
RUNTIME REQUIREMENTS

Mac OS X 10.6 Snow Leopard or later.

===========================================================================
CHANGES FROM PREVIOUS VERSIONS

Version 1.1
- Updated all classes to use properties.
- Improved error handling.
- Project updated for Xcode 4.
Version 1.0
- Initial Version

===========================================================================
Copyright (C) 2006-2011 Apple Inc. All rights reserved.
```

[Next](main.m.md)[Previous](AttachAScript.md)

