---
title: SimpleScriptingPlugin
apple_id: DTS40008783
resource_type: Sample Code
platform: macOS
topic: Interapplication Communication
technology: Foundation
published: '2009-05-11'
source_url: https://developer.apple.com/library/archive/samplecode/SimpleScriptingPlugin/Introduction/Intro.html
archived_at: '2026-07-18T03:24:08.278547Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# SimpleScriptingPlugin

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2009-05-11 Illustrates how to add a scripting plugin to a scriptabile application. |
| __Build Requirements:__ | Xcode 3.1 or later, Mac OS X v10.5 or later |
| __Runtime Requirements:__ | Mac OS X v10.5 or later |

This sample is a follow-on to the SimpleScriptingObjects sample, and it uses many of the techniques from the SimpleScriptingVerbs sample. After completing the steps defined in the SimpleScriptingObjects sample to set up and create a scriptable application, you can continue with the steps in this sample to add both scripting plugin capabilities to the application and an example scripting plugin.

The techniques presented here illustrate a number of interesting things you can do with a scripting plugin. These include:

(a) adding new scripting classes

(b) extending existing scripting classes

(c) adding new scripting commands

Briefly said, once an application is scriptable, allowing for scripting plugins is easy work. The modifications to the host application are minimal and very generic. No special code needs to be added to the existing scripting classes to allow for plugins. And, creating the scripting plugins is no more difficult than adding some additional scripting to the application. The scripting plugin itself is a simple Cocoa Loadable Bundle that contains one or more .sdef files describing its scripting functionality.

[Next](ReadMe.txt.md)

