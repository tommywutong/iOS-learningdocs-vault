---
title: Basic Drawing and Event Handling
apple_id: DTS40007956
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2012-07-12'
source_url: https://developer.apple.com/library/archive/samplecode/Squiggles/Introduction/Intro.html
archived_at: '2026-07-18T03:25:30.394641Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# Basic Drawing and Event Handling

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2012-07-12 1) Updated to use ARC and modern Objective-C syntax (including use of properties and autosynthesis). 2) Refactored drawing code into ASCSquiggle. 3) Converted document-based application to a window-based application. 4) Updated \*.nib to \*.xib 5) Updated comments, and also reformatted some of the comments. 6) Added logical pragma marks to separate different parts of the code. 7) Each class now has ASC (Apple Sample Code) prefixes. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojvgywvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Mac OS X 10.8 or later, Xcode 4.5 or later |
| __Runtime Requirements:__ | Mac OS X 10.7 or later |

"Squiggles" is a Cocoa application that shows how you can perform custom drawing and event-handling in a subclass of NSView. The sample illustrates: \* Use of NSView's -drawRect: to implement custom drawing. \* Use of NSView's -mouseDown: and -mouseDragged: to handle user events. \* Use of NSBezierPath to draw lines.

[Next](ReadMe.txt.md)

