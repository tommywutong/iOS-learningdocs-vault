---
title: 'imageWithBitmapData:bytesPerRow:size:format:colorSpace:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimage/imagewithbitmapdata:bytesperrow:size:format:colorspace:'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/imagewithbitmapdata:bytesperrow:size:format:colorspace:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/imagewithbitmapdata%3Abytesperrow%3Asize%3Aformat%3Acolorspace%3A.json'
content_hash: 'sha256:75e875f21b4e02dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# imageWithBitmapData:bytesPerRow:size:format:colorSpace:

<sub>Type Method</sub>

Creates and returns an image object from bitmap data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (CIImage *) imageWithBitmapData:(NSData *) data bytesPerRow:(size_t) bytesPerRow size:(CGSize) size format:(CIFormat) format colorSpace:(CGColorSpaceRef) colorSpace;
```

## Parameters

- `data` — The bitmap data for the image. This data must be premultiplied.

- `bytesPerRow` — The number of bytes per row.

- `size` — The dimensions of the image.

- `format` — The format and size of each pixel. You must supply a pixel format constant. See `Pixel Formats`.

- `colorSpace` — The color space that the image is defined in. If this value is `nil`, the image is not color matched. Pass `nil` for images that don’t contain color data (such as elevation maps, normal vector maps, and sampled function tables).

## Return Value

An image object.

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
