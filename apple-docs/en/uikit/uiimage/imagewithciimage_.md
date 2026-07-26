---
title: 'imageWithCIImage:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/imagewithciimage:'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/imagewithciimage:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/imagewithciimage%3A.json'
content_hash: 'sha256:af80be0458c1789a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# imageWithCIImage:

<sub>Type Method</sub>

Creates and returns an image object that contains a Core Image object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```objc
+ (UIImage *) imageWithCIImage:(CIImage *) ciImage;
```

## Parameters

- `ciImage` — The Core Image object to encapsulate.

## Return Value

A new image object.

## See Also

### Creating and initializing image objects

- [imageWithContentsOfFile:](imagewithcontentsoffile_.md) — Creates and returns an image object by loading the image data from the file at the specified path.
- [imageWithData:](imagewithdata_.md) — Creates and returns an image object that uses the specified image data.
- [imageWithData:scale:](imagewithdata_scale_.md) — Creates and returns an image object that uses the specified image data and scale factor.
- [imageWithCGImage:](imagewithcgimage_.md) — Creates and returns an image object representing the specified Quartz image.
- [imageWithCGImage:scale:orientation:](imagewithcgimage_scale_orientation_.md) — Creates and returns an image object with the specified scale and orientation factors.
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
