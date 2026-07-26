---
title: subsampleFactor
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/coreimage/ciimageoption/subsamplefactor
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageoption/subsamplefactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageoption/subsamplefactor.json'
content_hash: 'sha256:2d3399b8ba098cd3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageOption](../ciimageoption.md)

# subsampleFactor

<sub>Type Property</sub>

The factor by which to scale down a returned images.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let subsampleFactor: CIImageOption
```

## Discussion

The value of this key should be an `NSNumber` containing the integer value 2, 4, or 8. It can be used to improve performance and reduce memory usage when working with large images.

When you specify this key, the retured image will be scaled down the image data by the specified numerical factor. If the image format doesn’t support the specified scale factor, a larger or full-size normal image is returned.

This option is only supported by JPEG, HEIF, TIFF, PNG and RAW images formats.

This option is only supported by these APIs:

- `/CIImage/imageWithContentsOfURL:options:`
- `/CIImage/initWithContentsOfURL:options:`
- `/CIImage/imageWithData:options:`
- `/CIImage/initWithData:options:`
- `/CIImage/imageWithCGImageSource:index:options:`
- `/CIImage/initWithCGImageSource:index:options:`

> [!note] Note
> The `kCGImageSourceSubsampleFactor` key can also be used for this purpose.
