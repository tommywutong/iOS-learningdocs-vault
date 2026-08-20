---
title: QuickTime Visual Context - Setting the kQTVisualContextOutputColorSpaceKey
  Attribute
apple_id: DTS10004454
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2007-09-28'
source_url: https://developer.apple.com/library/archive/qa/qa1550/_index.html
archived_at: '2026-07-18T02:32:16.012977Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1550

# QuickTime Visual Context - Setting the kQTVisualContextOutputColorSpaceKey Attribute

## Q:  How do I set the output color space attribute when creating a QuickTime OpenGL Texture Visual Context?

A: How do I set the output color space attribute when creating a QuickTime OpenGL Texture Visual Context?

Both QuickTime Visual Context creation APIs, `QTOpenGLTextureContextCreate` and `QTPixelBufferContextCreate` take a dictionary of key-value paired attributes that influence aspects of the created context. Single attributes may also be set after creation by calling `QTVisualContextSetAttribute`. A full list of visual context attributes can be found in `ImageCompression.h`.

Two of these attributes are the working color space (`kQTVisualContextWorkingColorSpaceKey`) and the output color space (`kQTVisualContextOutputColorSpaceKey`). Setting one or both of these color space attributes allows developers to influence how QuickTime interprets color information during rendering.


```
Key: kQTVisualContextWorkingColorSpaceKey  Value: CGColorSpaceRef  Description:  The color space in which QuickTime will perform image processing. If this attribute is not set, images will be processed in the output color space.
```



```
Key: kQTVisualContextOutputColorSpaceKey  Value: CGColorSpaceRef  Description:  The color space of images produced by this visual context. If this attribute is not set, images may be in any color space.
```

To set the output color space attribute, first create an attributes dictionary containing a `CGColorSpaceRef` paired with the `kQTVisualContextOutputColorSpaceKey` key, then pass this attributes dictionary to `QTOpenGLTextureContextCreate` as shown in listing 1. Listing 2 demonstrates how to create a `CGColorSpaceRef` from the display profile.

__Listing 1__  Visual Context creation with attributes.

```
QTVisualContextRef  theVisualContext;  ...  NSDictionary *attributes = [NSDictionary dictionaryWithObjectsAndKeys:                                          [self displayColorSpace], kQTVisualContextOutputColorSpaceKey, nil];  error = QTOpenGLTextureContextCreate(kCFAllocatorDefault, (CGLContextObj)[[self openGLContext] CGLContextObj],                                     (CGLPixelFormatObj)[[self pixelFormat] CGLPixelFormatObj],                                     (CFDictionaryRef)attributes,                                     &theVisualContext); if (noErr == error) {     [self setVisualContext:theVisualContext]; } ...  ...
```


__Listing 2__  Creating a display color space.

```
...  // return currently set display color space - (CGColorSpaceRef)displayColorSpace {     return mDisplayColorSpace; }  // set the display color space, this function in null safe - (void)setDisplayColorSpace:(CGColorSpaceRef)inDisplayColorSpace {     CGColorSpaceRetain(inDisplayColorSpace);     CGColorSpaceRelease(mDisplayColorSpace);      mDisplayColorSpace = inDisplayColorSpace; }  // update the display color space - (void)updateDisplayColorSpace:(CGDirectDisplayID)inDisplayID {     CMProfileRef profile;      if (noErr == CMGetProfileByAVID((CMDisplayIDType)inDisplayID, &profile)) {         CGColorSpaceRef theDisplayColorSpace = CGColorSpaceCreateWithPlatformColorSpace(profile);          [self setDisplayColorSpace:theDisplayColorSpace];          CGColorSpaceRelease(theDisplayColorSpace);          CMCloseProfile(profile);     } else {         [self setDisplayColorSpace:NULL];     }      if (NULL != [self visualContext]) {         QTVisualContextSetAttribute(qtVisualContext,                                     kQTVisualContextOutputColorSpaceKey,                                     [self displayColorSpace]);     } }  ...
```


- [Color Management Overview](https://developer.apple.com/documentation/GraphicsImaging/Conceptual/csintro/index.html)
- [Color and Color Spaces](https://developer.apple.com/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/dq_color/chapter_5_section_1.html)
- [CGColorSpace Reference](https://developer.apple.com/documentation/GraphicsImaging/Reference/CGColorSpace/Reference/reference.html)
- [Technical Q&A QA1396, 'Creating color spaces that ensure color matching.'](https://developer.apple.com/qa/qa2004/qa1396.html)
- [Sample Code 'CIVideoDemoGL'](https://developer.apple.com/samplecode/CIVideoDemoGL/index.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-09-28 | New document that describes how to configure a QuickTime OpenGL Texture Visual Context with the kQTVisualContextOutputColorSpaceKey attribute. |

