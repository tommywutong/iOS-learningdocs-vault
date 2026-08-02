---
title: Quartz2DBasics
apple_id: DTS10003975
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2006-09-11'
source_url: https://developer.apple.com/library/archive/samplecode/Quartz2DBasics/Introduction/Intro.html
archived_at: '2026-07-18T03:21:24.926729Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Readme.txt.md)

# Quartz2DBasics

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.01, 2006-09-11 Now avoids use of floats where unnecessary. Where floating point constants are necessary avoids explicit use (now uses 10.0 instead of 10.0f). These changes make the code more readable while preserving efficiency and make the code ready for conversion to 64 bit. |
| __Build Requirements:__ | Xcode 2.3 or greater, Mac OS X 10.4 Universal SDK |
| __Runtime Requirements:__ | Mac OS X 10.4.7 or greater. |

This sample code introduces some of the concepts and features of Quartz. It contains code that:
\* fills then strokes a rectangle and strokes then fills a rectangle
\* creates a CGPath object and then paints that path with varying degrees of alpha transparency
\* draws the contents of a TIFF file using Quartz
\*Â draws the contents of a TIFF file using Quartz clipped by an elliptical shape
\* caches content using a CGLayer object and then draws using that cache
\* exports any of the above drawing to a PDF file
\* exports any of the above drawing as a PNG file
This code sample contains a Carbon and Cocoa project that each have equivalent functionality.

[Next](Readme.txt.md)

