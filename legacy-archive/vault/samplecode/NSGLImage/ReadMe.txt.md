---
title: NSGLImage
apple_id: DTS10003451
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2004-12-01'
source_url: https://developer.apple.com/library/archive/samplecode/NSGLImage/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:16:46.765205Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [NSGLImage](NSGLImage.md)


[Next](main.m.md)[Previous](NSGLImage.md)

# ReadMe.txt

```
This sample demonstrates how to use an NSImage and NSBitmapImageRep to get texture data into OpenGL. It will display an image on a polygon that is scaled to the appropriate dimensions for that texture. Help information is available on the primary display. This is essentially the Cocoa OpenGL Window sample with an added class for drawing the NSBitmapImageRep in OpenGL. A few changes have been made to the BasicOpenGLView class to allow it to use the NSGLImage class (contained in the file(s) GLImage.h/.m). Mouse tracking and clicking behavior was also changed from the default implementation to be more useful with flat, 2D polygon. 

To see the changes, simply search the project for the string 'GLImage:'. Note that the help string changes and such are NOT labeled as per the following. This applies only to changes to the view class that allow for the operation of the sample.

Note that this sample will fail when trying to load an image larger than 2560 x 2560. It does, however, fail somewhat gracefully and informs the user of this problem.
```

[Next](main.m.md)[Previous](NSGLImage.md)

