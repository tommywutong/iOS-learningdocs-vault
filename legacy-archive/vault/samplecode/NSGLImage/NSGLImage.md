---
title: NSGLImage
apple_id: DTS10003451
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2004-12-01'
source_url: https://developer.apple.com/library/archive/samplecode/NSGLImage/Introduction/Intro.html
archived_at: '2026-07-18T03:16:46.099595Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# NSGLImage

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2004-12-01 Minor changes and updates. Removed an erroneous section of the help string (the part about 'c' for capabilities), rebuilt the packaged executable and cleaned some comments out of the source files. |
| __Build Requirements:__ | Xcode 1.5 or later |
| __Runtime Requirements:__ | Mac OS X 10.3 or later |

This sample demonstrates how to use an NSImage and NSBitmapImageRep to get texture data into OpenGL. It will display an image on a polygon that is scaled to the appropriate dimensions for that texture. Help information is available on the primary display. This is essentially the Cocoa OpenGL Window sample with an added class for drawing the NSBitmapImageRep in OpenGL. A few changes have been made to the BasicOpenGLView class to allow it to use the GLImage class (contained in the file(s) GLImage.h/.m). Mouse tracking and clicking behavior was also changed from the default implementation to be more useful with flat, 2D polygon.
To see the changes, simply search the project for the string 'GLImage:'. Note that the help string changes and such are NOT labeled as per the following. This applies only to changes to the view class that allow for the operation of the sample.

[Next](ReadMe.txt.md)

