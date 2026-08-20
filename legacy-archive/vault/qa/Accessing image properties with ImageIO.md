---
title: Accessing image properties with ImageIO
apple_id: DTS40010280
resource_type: QA
platform: watchOS|iOS|macOS
topic: Graphics & Animation
technology: Quartz
published: '2010-08-31'
source_url: https://developer.apple.com/library/archive/qa/qa1654/_index.html
archived_at: '2026-07-18T02:33:17.454868Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1654

# Accessing image properties with ImageIO

## Q:  How can I access image properties, such as image height and width, DPI, EXIF data, etc., of an image?

A: How can I access image properties, such as image height and width, DPI, EXIF data, etc., of an image?

The ImageIO framework, which was introduced on the Mac in Mac OS X 10.4 and on iOS in iOS4, provides the capabilities to access image properties such as size, DPI, EXIF data, etc. from an image.

To access the image properties you:

1. create a [CGImageSourceRef](https://developer.apple.com/mac/library/documentation/GraphicsImaging/Reference/CGImageSource/Reference/reference.html) for your image.
2. get a copy of the image properties dictionary by calling [CGImageSourceCopyPropertiesAtIndex](https://developer.apple.com/documentation/imageio/1465363-cgimagesourcecopypropertiesatind).
3. access the values in the dictionary by calling CFDictionaryGetValue with the property key that you are interested in. The available keys are located in the [CGImageProperties Reference](https://developer.apple.com/mac/library/documentation/GraphicsImaging/Reference/CGImageProperties_Reference/Reference/reference.html).

Below is an example of how to access the width and height of an image.

__Listing 1__  Accessing image width and height.

```
CFURLRef url = CFURLCreateFromFileSystemRepresentation (kCFAllocatorDefault, (const UInt8 *)inputFileName, strlen(inputFileName), false);  if (!url) {    printf ("* * Bad input file path\n");  }  CGImageSourceRef myImageSource;  myImageSource = CGImageSourceCreateWithURL(url, NULL);  CFDictionaryRef imagePropertiesDictionary;  imagePropertiesDictionary = CGImageSourceCopyPropertiesAtIndex(myImageSource,0, NULL);  CFNumberRef imageWidth = (CFNumberRef)CFDictionaryGetValue(imagePropertiesDictionary, kCGImagePropertyPixelWidth); CFNumberRef imageHeight = (CFNumberRef)CFDictionaryGetValue(imagePropertiesDictionary, kCGImagePropertyPixelHeight);  int w = 0; int h = 0;  CFNumberGetValue(imageWidth, kCFNumberIntType, &w); CFNumberGetValue(imageHeight, kCFNumberIntType, &h);  CFRelease(imagePropertiesDictionary); CFRelease(myImageSource);  printf("Image Width: %d\n",w); printf("Image Height: %d\n",h);
```

For more information about using the ImageIO Framework, please see [Using the ImageIO Framework.](https://developer.apple.com/graphicsimaging/workingwithimageio.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-08-31 | New document that describes how to use the ImageIO framework to access image properties. |

