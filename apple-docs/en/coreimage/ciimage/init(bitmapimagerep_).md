---
title: 'init(bitmapImageRep:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimage/init(bitmapimagerep:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/init(bitmapimagerep:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/init%28bitmapimagerep%3A%29.json'
content_hash: 'sha256:94b661f862ebefb4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# init(bitmapImageRep:)

<sub>Initializer</sub>

Initializes an image object with the specified bitmap image representation.

<sub>macOS</sub>

```swift
init?(bitmapImageRep: NSBitmapImageRep)
```

## Parameters

- `bitmapImageRep` — An image representation object containing the bitmap data.

## Return Value

The initialized image object, or `nil` if the object could not be initialized.

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
- [- initWithImageProvider:size::format:colorSpace:options:](<init(imageprovider_size___format_colorspace_options_).md>) — Initializes an image object based on pixels from an image provider object.
- [- initWithDepthData:](<init(depthdata_).md>)
- [- initWithDepthData:options:](<init(depthdata_options_).md>)
- [- initWithPortaitEffectsMatte:](<init(portaiteffectsmatte_).md>)
