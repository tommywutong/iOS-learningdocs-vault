---
title: UIImageReader
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagereader-c.class
source_url: 'https://developer.apple.com/documentation/uikit/uiimagereader-c.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagereader-c.class.json'
content_hash: 'sha256:3d86c48883d1e958'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIImageReader

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface UIImageReader : NSObject
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

## Topics

### Instance Properties

- [configuration](uiimagereader-c.class/configuration.md)

### Instance Methods

- [imageWithContentsOfFileURL:](uiimagereader-c.class/imagewithcontentsoffileurl_.md) — Synchronously generate an image from the given file URL. If an image could not be generated, returns nil.
- [imageWithContentsOfFileURL:completion:](uiimagereader-c.class/imagewithcontentsoffileurl_completion_.md) — Asynchronously generate an image from the given file URL. If an image could not be generated, the completion will be called with nil.
- [imageWithData:](uiimagereader-c.class/imagewithdata_.md) — Synchronously generate an image from the given data. If an image could not be generated, returns nil.
- [imageWithData:completion:](uiimagereader-c.class/imagewithdata_completion_.md) — Asynchronously generate an image from the given data. If an image could not be generated, the completion will be called with nil.

### Type Properties

- [defaultReader](uiimagereader-c.class/defaultreader.md) — Returns a reader that uses the default configuration options. This method is thread safe.

### Type Methods

- [readerWithConfiguration:](uiimagereader-c.class/readerwithconfiguration_.md) — Returns a loader of the given configuration. Loaders are thread safe and sharable.

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
- [UIImageReaderConfiguration](uiimagereaderconfiguration.md) — The properties that a reader uses to decode images.
