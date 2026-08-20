---
title: DropDraw
apple_id: DTS10003339
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2005-08-01'
source_url: https://developer.apple.com/library/archive/samplecode/DropDraw/Introduction/Intro.html
archived_at: '2026-07-18T03:07:20.342578Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.c.md)

# DropDraw

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.3, 2005-08-01 Added missing XCode 2.1 project file |
| __Build Requirements:__ | XCode 2.1, XCode 2.0 |
| __Runtime Requirements:__ | Mac OS X 10.4.x or Mac OS X 10.3 (Panther) or later with QuickTime 6.4 or later |

DropDraw demonstrates automatic ColorSync color-matching when drawing with QuickTime graphics importers in Panther
This sample code has been updated to include a project that produces a universal binary. No code changes were required for it to run correctly on the Developer Transition Systems.
The QuickTime Graphics Importers that ship with Panther draw (via GraphicsImportDraw) using ColorSync color-matching by default. On pre-Panther systems, you had to write your own custom ColorSync code to perform color-matching.
Developers wishing to opt-out of this default color-matching must call GraphicsImportSetFlags as follows:
GraphicsImportSetFlags( gi, kGraphicsImporterDontUseColorMatching );
This sample demonstrates how to draw various images both color-matched and non color-matched by toggling this flag.
Sample images provided by the ColorSync team can be found in the
"Images with Trick Profiles"
folder. These sample images make it easy to determine whether ColorSync color-matching is being performed when the image is drawn (simply look at the message drawn with each image).

[Next](main.c.md)

