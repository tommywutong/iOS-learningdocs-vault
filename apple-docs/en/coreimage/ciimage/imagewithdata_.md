---
title: 'imageWithData:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimage/imagewithdata:'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/imagewithdata:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/imagewithdata%3A.json'
content_hash: 'sha256:f07a59f4a643c4f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# imageWithData:

<sub>Type Method</sub>

Creates and returns an image object initialized with the supplied image data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (CIImage *) imageWithData:(NSData *) data;
```

## Parameters

- `data` — The data object that holds the contents of an image file (such as TIFF, GIF, JPG, or whatever else the system supports). The image data must be premultiplied.

## Return Value

An image object initialized with the supplied data, or `nil` if the method cannot create an image representation from the contents of the supplied data object.

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
- [- initWithData:](<init(data_).md>) — Initializes an image object with the supplied image data.
- [imageWithData:options:](imagewithdata_options_.md) — Creates and returns an image object initialized with the supplied image data, using the specified options.
