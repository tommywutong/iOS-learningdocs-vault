---
title: 'imageWithMTLTexture:options:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimage/imagewithmtltexture:options:'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/imagewithmtltexture:options:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/imagewithmtltexture%3Aoptions%3A.json'
content_hash: 'sha256:1f35f45ca12c61c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# imageWithMTLTexture:options:

<sub>Type Method</sub>

Creates and returns an image object with data supplied by a Metal texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (CIImage *) imageWithMTLTexture:(id<MTLTexture>) texture options:(NSDictionary<NSString *,id> *) options;
```

## Parameters

- `texture` — The Metal texture from which to use image data.

- `options` — A dictionary specifying image options. (See `Image Dictionary Keys`.)

## Return Value

An image object initialized with the texture data.

## Discussion

To also render using Metal, use this image with a Metal-based [CIContext](../cicontext.md) object created with the [+ contextWithMTLDevice:](<../cicontext/init(mtldevice_)-swey.md>) method, and call the [- render:toMTLTexture:commandBuffer:bounds:colorSpace:](<../cicontext/render(__to_commandbuffer_bounds_colorspace_).md>) method to create an output image in another Metal texture object.

## See Also

### Creating an Image

- [+ emptyImage](<empty().md>) — Creates and returns an empty image object.
- [- initWithImage:](<init(image_).md>) — Initializes an image object with the specified UIKit image object.
- [- initWithImage:options:](<init(image_options_).md>) — Initializes an image object with the specified UIKit image object, using the specified options.
- [- initWithContentsOfURL:](<init(contentsof_).md>) — Initializes an image object by reading an image from a URL.
- [imageWithContentsOfURL:](imagewithcontentsofurl_.md) — Creates and returns an image object from the contents of a file.
- [- initWithContentsOfURL:options:](<init(contentsof_options_).md>) — Initializes an image object by reading an image from a URL, using the specified options.
- [imageWithContentsOfURL:options:](imagewithcontentsofurl_options_.md) — Creates and returns an image object from the contents of a file, using the specified options.
- [imageWithCGImage:](imagewithcgimage_.md) — Creates and returns an image object from a Quartz 2D image.
- [- initWithCGImage:](<init(cgimage_)-2kvvb.md>) — Initializes an image object with a Quartz 2D image.
- [imageWithCGImage:options:](imagewithcgimage_options_.md) — Creates and returns an image object from a Quartz 2D image using the specified options.
- [- initWithCGImage:options:](<init(cgimage_options_)-8663h.md>) — Initializes an image object with a Quartz 2D image, using the specified options.
- [imageWithCGImageSource:index:options:](imagewithcgimagesource_index_options_.md)
- [- initWithCGImageSource:index:options:](<init(cgimagesource_index_options_)-e2bz.md>)
- [imageWithData:](imagewithdata_.md) — Creates and returns an image object initialized with the supplied image data.
- [- initWithData:](<init(data_).md>) — Initializes an image object with the supplied image data.
