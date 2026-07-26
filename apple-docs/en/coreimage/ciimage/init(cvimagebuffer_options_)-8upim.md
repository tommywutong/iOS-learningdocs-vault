---
title: 'init(cvImageBuffer:options:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimage/init(cvimagebuffer:options:)-8upim'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/init(cvimagebuffer:options:)-8upim'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/init%28cvimagebuffer%3Aoptions%3A%29-8upim.json'
content_hash: 'sha256:faeeaf5897ccf22c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# init(cvImageBuffer:options:)

<sub>Initializer</sub>

Initializes an image object from the contents of a Core Video image buffer, using the specified options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(cvImageBuffer imageBuffer: CVImageBuffer, options: [CIImageOption : Any]? = nil)
```

## Parameters

- `imageBuffer` — A  `CVImageBuffer` object in a supported pixel format constant. For more information, see [Core Video](../../corevideo.md).

- `options` — A dictionary that contains options for creating an image object. (See `Image Dictionary Keys`.) The pixel format is supplied by the `CVImageBuffer` object.)

## Return Value

The initialized image object.

## Discussion

The `imageBuffer` parameter must be in one of the following formats:

- [kCVPixelFormatType_32ARGB](../../corevideo/kcvpixelformattype_32argb.md)
- [kCVPixelFormatType_422YpCbCr8](../../corevideo/kcvpixelformattype_422ypcbcr8.md)
- [kCVPixelFormatType_32BGRA](../../corevideo/kcvpixelformattype_32bgra.md)

## See Also

### Creating an Image

- [+ emptyImage](<empty().md>) — Creates and returns an empty image object.
- [- initWithImage:](<init(image_).md>) — Initializes an image object with the specified UIKit image object.
- [- initWithImage:options:](<init(image_options_).md>) — Initializes an image object with the specified UIKit image object, using the specified options.
- [- initWithContentsOfURL:](<init(contentsof_).md>) — Initializes an image object by reading an image from a URL.
- [- initWithContentsOfURL:options:](<init(contentsof_options_).md>) — Initializes an image object by reading an image from a URL, using the specified options.
- [- initWithCGImage:](<init(cgimage_)-2kvvb.md>) — Initializes an image object with a Quartz 2D image.
- [- initWithCGImage:options:](<init(cgimage_options_)-8663h.md>) — Initializes an image object with a Quartz 2D image, using the specified options.
- [- initWithCGImageSource:index:options:](<init(cgimagesource_index_options_)-e2bz.md>)
- [- initWithData:](<init(data_).md>) — Initializes an image object with the supplied image data.
- [- initWithData:options:](<init(data_options_).md>) — Initializes an image object with the supplied image data, using the specified options.
- [- initWithBitmapData:bytesPerRow:size:format:colorSpace:](<init(bitmapdata_bytesperrow_size_format_colorspace_).md>) — Initializes an image object with bitmap data.
- [- initWithBitmapImageRep:](<init(bitmapimagerep_).md>) — Initializes an image object with the specified bitmap image representation.
- [- initWithImageProvider:size::format:colorSpace:options:](<init(imageprovider_size___format_colorspace_options_).md>) — Initializes an image object based on pixels from an image provider object.
- [- initWithDepthData:](<init(depthdata_).md>)
- [- initWithDepthData:options:](<init(depthdata_options_).md>)
