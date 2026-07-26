---
title: 'imageWithData:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/imagewithdata:'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/imagewithdata:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/imagewithdata%3A.json'
content_hash: 'sha256:5acfec13298e1725'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# imageWithData:

<sub>Type Method</sub>

Creates and returns an image object that uses the specified image data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (UIImage *) imageWithData:(NSData *) data;
```

## Parameters

- `data` — The image data. This can be data from a file or data you create programmatically.

## Return Value

A new image object for the specified data, or `nil` if the method could not initialize the image from the specified data.

## Discussion

This method does not cache the image object.

## See Also

### Creating and initializing image objects

- [imageWithContentsOfFile:](imagewithcontentsoffile_.md) — Creates and returns an image object by loading the image data from the file at the specified path.
- [imageWithData:scale:](imagewithdata_scale_.md) — Creates and returns an image object that uses the specified image data and scale factor.
- [imageWithCGImage:](imagewithcgimage_.md) — Creates and returns an image object representing the specified Quartz image.
- [imageWithCGImage:scale:orientation:](imagewithcgimage_scale_orientation_.md) — Creates and returns an image object with the specified scale and orientation factors.
- [imageWithCIImage:](imagewithciimage_.md) — Creates and returns an image object that contains a Core Image object.
- [imageWithCIImage:scale:orientation:](imagewithciimage_scale_orientation_.md) — Creates and returns an image object based on a Core Image object and the specified attributes.
- [- initWithContentsOfFile:](<init(contentsoffile_).md>) — Initializes and returns the image object with the contents of the specified file.
- [- initWithData:](<init(data_).md>) — Initializes and returns the image object with the specified data.
- [- initWithData:scale:](<init(data_scale_).md>) — Initializes and returns the image object with the specified data and scale factor.
- [- initWithCGImage:](<init(cgimage_)-14qlb.md>) — Initializes and returns the image object with the specified Quartz image reference.
- [- initWithCGImage:scale:orientation:](<init(cgimage_scale_orientation_)-2ouhh.md>) — Initializes and returns an image object with the specified scale and orientation factors.
- [- initWithCIImage:](<init(ciimage_)-93vu1.md>) — Initializes and returns an image object with the specified Core Image object.
- [- initWithCIImage:scale:orientation:](<init(ciimage_scale_orientation_)-9gpyn.md>) — Initializes and returns an image object with the specified Core Image object and properties.
- [UIImageReader](../uiimagereader-c.class.md)
- [UIImageReaderConfiguration](../uiimagereaderconfiguration.md) — The properties that a reader uses to decode images.
