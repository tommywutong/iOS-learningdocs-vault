---
title: 'init(ciImage:scale:orientation:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/init(ciimage:scale:orientation:)-9gpyn'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/init(ciimage:scale:orientation:)-9gpyn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/init%28ciimage%3Ascale%3Aorientation%3A%29-9gpyn.json'
content_hash: 'sha256:42c8b0a3d12b16b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# init(ciImage:scale:orientation:)

<sub>Initializer</sub>

Initializes and returns an image object with the specified Core Image object and properties.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(ciImage: CIImage, scale: CGFloat, orientation: UIImage.Orientation)
```

## Parameters

- `ciImage` — The Core Image object.

- `scale` — The scale factor to assume when interpreting the image data. Applying a scale factor of 1.0 results in an image whose size matches the pixel-based dimensions of the image. Applying a different scale factor changes the size of the image as reported by the [size](size.md) property.

- `orientation` — The orientation of the image data. You can use this parameter to specify any rotation factors applied to the image.

## Return Value

An initialized `UIImage` object. In Objective-C, this method returns `nil` if the `ciImage` parameter is `nil`.

## See Also

### Creating and initializing image objects

- [- initWithContentsOfFile:](<init(contentsoffile_).md>) — Initializes and returns the image object with the contents of the specified file.
- [- initWithData:](<init(data_).md>) — Initializes and returns the image object with the specified data.
- [- initWithData:scale:](<init(data_scale_).md>) — Initializes and returns the image object with the specified data and scale factor.
- [- initWithCGImage:](<init(cgimage_)-14qlb.md>) — Initializes and returns the image object with the specified Quartz image reference.
- [- initWithCGImage:scale:orientation:](<init(cgimage_scale_orientation_)-2ouhh.md>) — Initializes and returns an image object with the specified scale and orientation factors.
- [- initWithCIImage:](<init(ciimage_)-93vu1.md>) — Initializes and returns an image object with the specified Core Image object.
- [UIImageReader](../uiimagereader-swift.struct.md)
