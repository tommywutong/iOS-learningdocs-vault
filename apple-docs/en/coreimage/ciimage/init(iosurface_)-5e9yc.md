---
title: 'init(ioSurface:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimage/init(iosurface:)-5e9yc'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/init(iosurface:)-5e9yc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/init%28iosurface%3A%29-5e9yc.json'
content_hash: 'sha256:c91e2db0aadf74de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# init(ioSurface:)

<sub>Initializer</sub>

Initializes an image with the contents of an IOSurface.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(ioSurface surface: IOSurfaceRef)
```

## Parameters

- `surface` — An IOSurface object.

## Return Value

An image object initialized with the data from the IOSurface object.

## Discussion

An IOSurface object is a framebuffer object that is suitable for sharing across process boundaries. You can use it to allow your app to move complex image decompression and drawing logic into a separate process for the purpose of increasing security.

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
