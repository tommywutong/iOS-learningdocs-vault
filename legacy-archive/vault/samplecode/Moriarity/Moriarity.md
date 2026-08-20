---
title: Moriarity
apple_id: DTS10000396
resource_type: Sample Code
platform: macOS
topic: Interapplication Communication
technology: Foundation
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Moriarity/Introduction/Intro.html
archived_at: '2026-07-18T03:15:59.566215Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# Moriarity

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Implementing a Cocoa GUI that wraps command-line functionality, calling a UNIX task and presenting the results in a GUI. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon Project Builder 1.1 or higher, Mac OS X version 10.0 or higher |

This sample shows how to implement a Cocoa GUI that wraps command-line functionality, calling out to a UNIX task and presenting the results in the GUI to the user. The Process class used for task interaction is intended to be general purpose - feel free to use/adapt it to your own applications. The command-line functionality demonstrated in this case is 'locate' - a command that builds a database of files on the system for searching, a la Sherlock. One interesting thing to note is that locate matches a given string anywhere in a path to a file, not just in the name of a file. Requirements: Project Builder 1.1 or higher, Mac OS X version 10.0 or higher Keywords: NSTask nstask UNIX process fork cocoa

[Next](main.m.md)

