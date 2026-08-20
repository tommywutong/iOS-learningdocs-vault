---
title: vrmakepano.win
apple_id: DTS10001029
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/vrmakepano.win/Listings/README_txt.html
archived_at: '2026-07-26T19:52:59.451883Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [vrmakepano.win](vrmakepano.win.md)


[Next](Application%20Files-ComApplication.c.md)[Previous](vrmakepano.win.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# README.txt

```
README - VRMakePano

VRMakePano is a simple application that converts a panoramic image into a QuickTime VR panoramic movie. The panoramic image must be rotated 90 counterclockwise from its normal orientation, so that the image is taller than it is wide. The QuickTime VR movie created by VRMakePano is either a version 2.0 QTVR movie or a version 1.0 QTVR movie; you select the version using the Test menu.

VRMakePano can also construct a QuickTime VR movie from the six faces of a cube, so that the movie can be viewed using the cubic projection engine introduced in QuickTime VR version X.Y.

VRMakePano is distributed as sample code. It uses the graphics importer routines introduced in QuickTime 2.5 to open any available image file. Then it builds the QTVR file according to the documented file format. As an added bonus, VRMakePano shows the tile of the picture it's currently compressing as it churns through the image. (You can get rid of that behavior by setting a compile flag.)

The essential code is found in the file VRMakePano.c. This code compiles and runs on both MacOS and Windows platforms.

Enjoy,
QuickTime Team
```

[Next](Application%20Files-ComApplication.c.md)[Previous](vrmakepano.win.md)

