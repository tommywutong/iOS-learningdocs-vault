---
title: 'init(data:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/init(data:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/init(data:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/init%28data%3A%29.json'
content_hash: 'sha256:7838fb6d165c4c3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# init(data:)

<sub>Initializer</sub>

Initializes and returns the image object with the specified data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init?(data: Data)
```

## Parameters

- `data` — The data object containing the image data.

## Return Value

An initialized `UIImage` object, or `nil` if the method could not initialize the image from the specified data.

## Discussion

The data in the `data` parameter must be formatted to match the file format of one of the system’s supported image types.

## See Also

### Creating and initializing image objects

- [- initWithContentsOfFile:](<init(contentsoffile_).md>) — Initializes and returns the image object with the contents of the specified file.
- [- initWithData:scale:](<init(data_scale_).md>) — Initializes and returns the image object with the specified data and scale factor.
- [- initWithCGImage:](<init(cgimage_)-14qlb.md>) — Initializes and returns the image object with the specified Quartz image reference.
- [- initWithCGImage:scale:orientation:](<init(cgimage_scale_orientation_)-2ouhh.md>) — Initializes and returns an image object with the specified scale and orientation factors.
- [- initWithCIImage:](<init(ciimage_)-93vu1.md>) — Initializes and returns an image object with the specified Core Image object.
- [- initWithCIImage:scale:orientation:](<init(ciimage_scale_orientation_)-9gpyn.md>) — Initializes and returns an image object with the specified Core Image object and properties.
- [UIImageReader](../uiimagereader-swift.struct.md)
