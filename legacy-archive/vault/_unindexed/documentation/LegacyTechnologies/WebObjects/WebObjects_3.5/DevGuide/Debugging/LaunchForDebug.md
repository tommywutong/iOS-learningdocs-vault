---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/Debugging/LaunchForDebug.html
archived_at: '2026-07-15T07:51:20.997419Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DebuggingTOC.md) [!Previous Section](DebuggingTOC.md)

# Launching an Application for Debugging

You debug WebObjects applications using Project Builder, as described in the online book _WebObjects Tools and Techniques_. The executable you launch differs based on which language you used to write the application. This section tells you how to begin a debugging session for WebObjects applications written in each of the three available languages: WebScript, Java, and Objective-C.

## Debugging WebScript

To debug WebScript code, you rely on log messages and trace statements described in the section ["Debugging Techniques"](Techniques.md#apple-guztena).

If you've written an application entirely in WebScript, you typically debug it by running _NeXT_ROOT___/NextLibrary/Executables/WODefaultApp__ from the Project Builder launch panel, as described in _WebObjects Tools and Techniques_. When you do, the output from the debugging and trace statements is displayed in the launch panel.

## Debugging Java

The debugging strategy for Java applications is very similar to the strategy for debugging WebScript applications. Because the WebObjects Java bridge is incompatible with __jdb__, no Java debugger is supported for WebObjects. Instead, you can use the methods described in the section ["Debugging Techniques"](Techniques.md#apple-guztena) as well as __System.out.println__ statements. Build the executable for your project using Project Builder, then launch that executable in the launch panel. Output from the debugging methods appears in the launch panel.

## Debugging Objective-C

If all or part of your application is written in Objective-C, you can use the __gdb__ debugger in Project Builder. For more information on debugging an Objective-C application with Project Builder, see Project Builder's online help.
If your application contains WebScript code as well as Objective-C code, you debug the WebScript portion using __logWithFormat:__ and WOApplication trace statements as described in ["Debugging Techniques"](Techniques.md#apple-guztena).

## Debugging Mixed Applications

When you build a WebObjects application project, the result is a __.woa__ file package inside of the project directory. You may notice that this file package contains all of the application's components (including scripted components), and all other resources need to run the application, as well as the application executable itself.
When you're debugging an application, the executable uses the components from the project directory instead of those in the __.woa__ package, so you can safely ignore the components placed inside of the __.woa__ package. When you need to make a change, change the component in the project directory. When you run an application, it checks to see if its __.woa__ package is inside of a project directory (that is, a directory that contains a file named __PB.project__). If it is, the application takes its scripted components from the project directory. This way, you can make any necessary changes to your scripts in Project Builder, and (once you have saved the scripts) your application automatically picks up your changes without your having to rebuild.

[!Table of Contents](DebuggingTOC.md) [!Next Section](Techniques.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
