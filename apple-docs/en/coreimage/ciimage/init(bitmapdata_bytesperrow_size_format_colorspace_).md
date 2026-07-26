---
title: 'init(bitmapData:bytesPerRow:size:format:colorSpace:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimage/init(bitmapdata:bytesperrow:size:format:colorspace:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/init(bitmapdata:bytesperrow:size:format:colorspace:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/init%28bitmapdata%3Abytesperrow%3Asize%3Aformat%3Acolorspace%3A%29.json'
content_hash: 'sha256:5c72baaf175f724c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# init(bitmapData:bytesPerRow:size:format:colorSpace:)

<sub>Initializer</sub>

Initializes an image object with bitmap data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(bitmapData data: Data, bytesPerRow: Int, size: CGSize, format: CIFormat, colorSpace: CGColorSpace?)
```

## Parameters

- `data` — The bitmap data to use for the image. The data you supply must be premultiplied.

- `bytesPerRow` — The number of bytes per row.

- `size` — The size of the image data.

- `format` — A pixel format constant. See `Pixel Formats`.

- `colorSpace` — The color space that the image is defined in. It must be a Quartz 2D color space ([CGColorSpace](../../coregraphics/cgcolorspace.md)). Pass `nil` for images that don’t contain color data (such as elevation maps, normal vector maps, and sampled function tables).

## Return Value

The initialized image object.

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
- [- initWithBitmapImageRep:](<init(bitmapimagerep_).md>) — Initializes an image object with the specified bitmap image representation.
- [- initWithImageProvider:size::format:colorSpace:options:](<init(imageprovider_size___format_colorspace_options_).md>) — Initializes an image object based on pixels from an image provider object.
- [- initWithDepthData:](<init(depthdata_).md>)
- [- initWithDepthData:options:](<init(depthdata_options_).md>)
- [- initWithPortaitEffectsMatte:](<init(portaiteffectsmatte_).md>)
