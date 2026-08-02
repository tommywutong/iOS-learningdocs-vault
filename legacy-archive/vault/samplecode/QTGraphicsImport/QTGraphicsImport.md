---
title: QTGraphicsImport
apple_id: DTS10000781
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AppKit
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTGraphicsImport/Introduction/Intro.html
archived_at: '2026-07-18T03:20:52.611699Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# QTGraphicsImport

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Demonstrates how to use the QuickTime Graphics Importer to draw an image into a NSWindow using a NSQuickDrawView. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Mac OS X |

This sample demonstrates how to use the QuickTime graphics importer to draw/manipulate an image in a Cocoa NSWindow using the NSQuickDrawView class. The NSQuickDrawView class provides a single method, -qdport, which gives us a QuickDraw graphics port for use within the NSWindow/NSView. We pass the graphics port returned by this method to QuickTime (specifically, the GraphicsImportSetGWorld function) to specify our drawing environment. Additionally, we override the drawRect method in the NSView/NSQuickDrawView class to perform all our drawing using the Graphics importer routines. The sample will initially draw the image "qtlogo.pct" contained in the application package. However, the user can set a new image by pressing the "Set Image" button. Also, the user may export the image to a different format by pressing the "Export" button.

[Next](main.m.md)

