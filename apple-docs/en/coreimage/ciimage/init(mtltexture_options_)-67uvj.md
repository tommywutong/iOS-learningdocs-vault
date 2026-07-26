---
title: 'init(mtlTexture:options:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimage/init(mtltexture:options:)-67uvj'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/init(mtltexture:options:)-67uvj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/init%28mtltexture%3Aoptions%3A%29-67uvj.json'
content_hash: 'sha256:68a8530676997d5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# init(mtlTexture:options:)

<sub>Initializer</sub>

Initializes an image object with data supplied by a Metal texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init?(mtlTexture texture: any MTLTexture, options: [CIImageOption : Any]? = nil)
```

## Parameters

- `texture` — The Metal texture from which to use image data.

- `options` — A dictionary specifying image options. (See `Image Dictionary Keys`.)

## Return Value

The initialized image object, or `nil` if the image could not be initialized.

## Discussion

To render the image using Metal, use this image with a Metal-based [CIContext](../cicontext.md) object created with the [+ contextWithMTLDevice:](<../cicontext/init(mtldevice_)-swey.md>) method, and call the [- render:toMTLTexture:commandBuffer:bounds:colorSpace:](<../cicontext/render(__to_commandbuffer_bounds_colorspace_).md>) method to create an output image in another Metal texture object.

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
