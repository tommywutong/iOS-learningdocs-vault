---
title: qtmultiimage
apple_id: DTS10000871
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtmultiimage/Introduction/Intro.html
archived_at: '2026-07-26T19:52:46.716092Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](QTMultiImage.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# qtmultiimage

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Illustrates determining whether an image file contains more than one image and displaying any image. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

__Important__ This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

This sample code has been updated for QuickTime 5.0 README - QTMultiImage This file contains code that illustrates how to determine whether an image file contains more than one image and how to display any of those images. This is useful for working with FlashPix files (which contain multiple resolutions of an image) and PhotoShop files (which store layers as separate images), among others. The key new functions to use are GraphicsImportGetImageCount and GraphicsImportSetImageIndex. The rest of the image-handling is done using graphics importer routines that have previously been available. This file defines a single function that prompts the user for an image file, determines how many images are contained in that file, and then displays each such image for a short period of time (2 seconds). Your application, of course, will probably want to do more interesting things with the image.

[Next](QTMultiImage.c.md)

