---
title: Quartz2DBasics
apple_id: DTS10003975
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2006-09-11'
source_url: https://developer.apple.com/library/archive/samplecode/Quartz2DBasics/Listings/Readme_txt.html
archived_at: '2026-07-18T03:21:25.945337Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Quartz2DBasics](Quartz2DBasics.md)


[Next](CommonCode-AppDrawing.c.md)[Previous](Quartz2DBasics.md)

# Readme.txt

```
This sample code introduces some of the concepts and features of Quartz. It contains code that:

* fills then strokes a rectangle and strokes then fills a rectangle
* creates a CGPath object and then paints that path with varying degrees of alpha transparency
* draws the contents of a TIFF file using Quartz
* draws the contents of a TIFF file using Quartz clipped by an elliptical shape
* caches content using a CGLayer object and then draws using that cache
* exports any of the above drawing to a PDF file
* exports any of the above drawing as a PNG file

This code sample contains a Carbon and Cocoa project that each have equivalent functionality. They share common drawing code in the "CommonCode" folder. The BasicDrawing.cocoa folder contains an Xcode project and source files specific to the Cocoa version of the project. The BasicDrawing.carbon folder contains an Xcode project and source files specific to the Carbon version of the project. Both projects support printing.

The file AppDrawing.c in the CommonCode folder contains the code that is not specific to either the Carbon or Cocoa framework and which performs the Quartz drawing and data exports described above. This is pure C code and provides an example of incorporating existing C code in a Cocoa application.
```

[Next](CommonCode-AppDrawing.c.md)[Previous](Quartz2DBasics.md)

