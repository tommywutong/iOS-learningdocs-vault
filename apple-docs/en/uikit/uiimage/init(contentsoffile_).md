---
title: 'init(contentsOfFile:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/init(contentsoffile:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/init(contentsoffile:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/init%28contentsoffile%3A%29.json'
content_hash: 'sha256:c85eb935bb80031f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# init(contentsOfFile:)

<sub>Initializer</sub>

Initializes and returns the image object with the contents of the specified file.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init?(contentsOfFile path: String)
```

## Parameters

- `path` — The path to the file. This path should include the filename extension that identifies the type of the image data.

## Return Value

An initialized `UIImage` object, or `nil` if the method could not find the file or initialize the image from its contents.

## Discussion

This method loads the image data into memory and marks it as purgeable. If the data is purged and needs to be reloaded, the image object loads that data again from the specified path.

## See Also

### Creating and initializing image objects

- [- initWithData:](<init(data_).md>) — Initializes and returns the image object with the specified data.
- [- initWithData:scale:](<init(data_scale_).md>) — Initializes and returns the image object with the specified data and scale factor.
- [- initWithCGImage:](<init(cgimage_)-14qlb.md>) — Initializes and returns the image object with the specified Quartz image reference.
- [- initWithCGImage:scale:orientation:](<init(cgimage_scale_orientation_)-2ouhh.md>) — Initializes and returns an image object with the specified scale and orientation factors.
- [- initWithCIImage:](<init(ciimage_)-93vu1.md>) — Initializes and returns an image object with the specified Core Image object.
- [- initWithCIImage:scale:orientation:](<init(ciimage_scale_orientation_)-9gpyn.md>) — Initializes and returns an image object with the specified Core Image object and properties.
- [UIImageReader](../uiimagereader-swift.struct.md)
