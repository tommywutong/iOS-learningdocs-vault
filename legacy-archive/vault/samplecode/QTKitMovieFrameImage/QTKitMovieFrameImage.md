---
title: QTKitMovieFrameImage
apple_id: DTS10004452
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QTKit
published: '2007-08-31'
source_url: https://developer.apple.com/library/archive/samplecode/QTKitMovieFrameImage/Introduction/Intro.html
archived_at: '2026-07-18T03:20:55.083206Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# QTKitMovieFrameImage

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2007-08-31 Using the QTMovie frameImageAtTime: withAttributes: method to get an image for the frame at a given time in a QTMovie. |
| __Build Requirements:__ | Xcode 3.0 |
| __Runtime Requirements:__ | Mac OS X Leopard, QuickTime 7.2.1 or better |

This sample shows how to use the QTMovie frameImageAtTime: method to get an NSImage for the frame at a given time in a QTMovie.

Mac OS X Leopard contains a new version of this method that gives the ability to pass a dictionary of attributes describing exactly the kind of image you want:

- (NSImage \*)frameImageAtTime:(QTTime)time withAttributes:(NSDictionary \*)attributes error: (NSError \*\*)errorPtr;

Previously, you always got back an NSImage of the current movie size from this method, even if this was not what was desired. This required a lot of post-processing of the returned image.

Now, you can specify the following attributes when calling this method:

QTMovieFrameImageSize

QTMovieFrameImageType

QTMovieFrameImageRepresentationsType

QTMovieFrameImageOpenGLContext

QTMovieFrameImagePixelFormat

QTMovieFrameImageInterlaced

QTMovieFrameImageHighQuality

QTMovieFrameImageSingleField

(See QTMovie.h for more details)

These give the developer much more control over the type of image that is returned.

[Next](main.m.md)

