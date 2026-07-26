---
title: UIImageReaderConfiguration
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagereaderconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uiimagereaderconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagereaderconfiguration.json'
content_hash: 'sha256:9312b7d77e161925'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIImageReaderConfiguration

<sub>Class</sub>

The properties that a reader uses to decode images.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface UIImageReaderConfiguration : NSObject
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [NSCopying](../foundation/nscopying.md)

## Topics

### Configuration properties

- [prefersHighDynamicRange](uiimagereaderconfiguration/prefershighdynamicrange.md) — A Boolean value that indicates whether the image reader should decode the image as HDR when the type is capable of decoding in either SDR or HDR.
- [preferredThumbnailSize](uiimagereaderconfiguration/preferredthumbnailsize.md) — The thumbnail size in pixels that the image reader makes the image.
- [preparesImagesForDisplay](uiimagereaderconfiguration/preparesimagesfordisplay.md) — A Boolean value that indicates whether the image reader prepares the image for display.
- [pixelsPerInch](uiimagereaderconfiguration/pixelsperinch.md) — The integral scale that the image reader applies to the image.

## See Also

### Creating and initializing image objects

- [imageWithContentsOfFile:](uiimage/imagewithcontentsoffile_.md) — Creates and returns an image object by loading the image data from the file at the specified path.
- [imageWithData:](uiimage/imagewithdata_.md) — Creates and returns an image object that uses the specified image data.
- [imageWithData:scale:](uiimage/imagewithdata_scale_.md) — Creates and returns an image object that uses the specified image data and scale factor.
- [imageWithCGImage:](uiimage/imagewithcgimage_.md) — Creates and returns an image object representing the specified Quartz image.
- [imageWithCGImage:scale:orientation:](uiimage/imagewithcgimage_scale_orientation_.md) — Creates and returns an image object with the specified scale and orientation factors.
- [imageWithCIImage:](uiimage/imagewithciimage_.md) — Creates and returns an image object that contains a Core Image object.
- [imageWithCIImage:scale:orientation:](uiimage/imagewithciimage_scale_orientation_.md) — Creates and returns an image object based on a Core Image object and the specified attributes.
- [- initWithContentsOfFile:](<uiimage/init(contentsoffile_).md>) — Initializes and returns the image object with the contents of the specified file.
- [- initWithData:](<uiimage/init(data_).md>) — Initializes and returns the image object with the specified data.
- [- initWithData:scale:](<uiimage/init(data_scale_).md>) — Initializes and returns the image object with the specified data and scale factor.
- [- initWithCGImage:](<uiimage/init(cgimage_)-14qlb.md>) — Initializes and returns the image object with the specified Quartz image reference.
- [- initWithCGImage:scale:orientation:](<uiimage/init(cgimage_scale_orientation_)-2ouhh.md>) — Initializes and returns an image object with the specified scale and orientation factors.
- [- initWithCIImage:](<uiimage/init(ciimage_)-93vu1.md>) — Initializes and returns an image object with the specified Core Image object.
- [- initWithCIImage:scale:orientation:](<uiimage/init(ciimage_scale_orientation_)-9gpyn.md>) — Initializes and returns an image object with the specified Core Image object and properties.
- [UIImageReader](uiimagereader-c.class.md)
