---
title: Quartz 2D Transformer
apple_id: DTS10004203
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2010-04-12'
source_url: https://developer.apple.com/library/archive/samplecode/CGRotation/Listings/Readme_txt.html
archived_at: '2026-07-18T03:02:31.581069Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Quartz 2D Transformer](Quartz%202D%20Transformer.md)


[Next](main.m.md)[Previous](Quartz%202D%20Transformer.md)

# Readme.txt

```
Quartz2DTransformer is a Cocoa application that demonstrates how to use the Current Transformation Matrix (CTM) to apply rotation, scaling and transformation to an image for display. It also demonstrates simple usage of ImageIO to load and save images and how to get the pixel data from a CGImageRef into an arbitrary buffer.

Controller.h & Controller.m:
These two files contains all the code that handles the user interface.

ImageView.h & ImageView.m:
These two files contain the declaration and implementation of the ImageView class. This class is a subclass of NSView that lets us display our image.

ImageUtils.h & ImageUtils.c:
The meat of the sample, the utilities that we use to load, save, draw and transform the image that we are displaying. There are 6 functions that are of primary usage

ImageInfo * IICreateImage(CFURLRef url) - Loads an image at the given url, and allocates a structure that holds all the information we need to display it.

bool IISaveImage(ImageInfo * image, CFURLRef url, size_t width, size_t height) - Saves an image that is of the given size using the display parameters from the ImageInfo struct.

void IIDrawImage(ImageInfo * image, CGContextRef context, CGRect bounds) - just draws the given image centered inside of the given bounds.

void IIApplyTransformation(ImageInfo * image, CGContextRef context, CGRect bounds) - applies the same transformations that IIDrawImage does, but doesn't draw the image itself.

void IIDrawImageTransformed(ImageInfo * image, CGContextRef context, CGRect bounds) - similar to calling IIApplyTransformation followed by IIDrawImage, but it preserves the current CTM.

void IIRelease(ImageInfo * image) - deallocates the ImageInfo struct created by IICreateImage.
```

[Next](main.m.md)[Previous](Quartz%202D%20Transformer.md)

