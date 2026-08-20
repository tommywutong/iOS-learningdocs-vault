---
title: IconUtilCheck
apple_id: DTS10000583
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/IconUtilCheck/Introduction/Intro.html
archived_at: '2026-07-18T03:12:15.425686Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](IconUtilCheck.c.md)

# IconUtilCheck

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-30 Shows how to determine whether the Icon Utilities are available. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

According to the Tech Note OV - 16, "Inside Macintosh: More Macintosh Toolbox, page 5-7, specifies that the gestaltIconUtilitiesAttr - 'icon' gestalt selector can be used to determine whether the icon utilities are present under System 7.x. Note that this selector is included in the GestaltEqu files. It turns out that this selector is not implemented until System Software v7.1.2. To check for the existence of these utilities, use the TrapAvailable code to check for the _IconDispatch, (0xABC9) trap. The TrapAvailable code is presented in Inside Macintosh VI 3-8, and as sample code in many of the snippets on the Developer CD." This snippet shows how to determine whether the Icon Utilities are available. Requirements: Keywords: Icon, Utils, Utilities

[Next](IconUtilCheck.c.md)

