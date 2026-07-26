---
title: 'imageWithCVImageBuffer:options:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimage/imagewithcvimagebuffer:options:'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/imagewithcvimagebuffer:options:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/imagewithcvimagebuffer%3Aoptions%3A.json'
content_hash: 'sha256:d9b5d5c75def8c57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# imageWithCVImageBuffer:options:

<sub>Type Method</sub>

Creates and returns an image object from the contents of  `CVImageBuffer` object, using the specified options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (CIImage *) imageWithCVImageBuffer:(CVImageBufferRef) imageBuffer options:(NSDictionary<NSString *,id> *) options;
```

## Parameters

- `imageBuffer` — A  `CVImageBuffer` object. For more information, see [Core Video](../../corevideo.md).

- `options` — A dictionary specifying image options. (See `Image Dictionary Keys`.)

## Return Value

An image object initialized with the contents of the image buffer object and set up with the specified options.

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
