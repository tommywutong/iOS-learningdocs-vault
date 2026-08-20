---
title: qtgraphimp.win
apple_id: DTS10000864
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtgraphimp.win/Introduction/Intro.html
archived_at: '2026-07-26T19:52:46.498866Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](README.txt.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# qtgraphimp.win

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Illustrates how to use QuickTime's graphics importer routines to open and display image files. |
| __Build Requirements:__ | N/A |
| __Runtime Requirements:__ | Carbon |

__Important__ This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

This sample code has been updated for QuickTime 5.0 README - QTGRAPHIMP This sample code illustrates how to use QuickTime's graphics importer routines to open and display image files. The graphics importer routines were introduced in QuickTime version 2.5 as a new way to draw still images. The graphics import routines (for example, GetGraphicsImporterForFile) use graphics import components (of component type 'grip') to open and perform other operations on image files. Essentially, you can use the graphics import routines to insulate your application from the nitty gritty details of image file format and compression used in the image. In this sample code, we allow the user to open an image file; then we draw it into a window on the screen. Your application, of course, will probably want to do more interesting things with the image. We also allow the user to save an image using JPEG compression.

[Next](README.txt.md)

