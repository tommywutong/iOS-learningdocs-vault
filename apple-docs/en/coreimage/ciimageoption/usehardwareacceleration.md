---
title: useHardwareAcceleration
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/coreimage/ciimageoption/usehardwareacceleration
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageoption/usehardwareacceleration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageoption/usehardwareacceleration.json'
content_hash: 'sha256:c9818786abfdd64a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageOption](../ciimageoption.md)

# useHardwareAcceleration

<sub>Type Property</sub>

A Boolean value specifying that using hardware is preferred when decoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let useHardwareAcceleration: CIImageOption
```

## Discussion

If the value for this option is:

- True: The image will be decoded using dedicated hardware if possible.
- False: The image will be decoded using the CPU is possible.
- Not specified: The default behavior is True.

This option is only supported by JPEG and HEIF images formats.

This option is only supported by these APIs:

- `/CIImage/imageWithContentsOfURL:options:`
- `/CIImage/initWithContentsOfURL:options:`
- `/CIImage/imageWithData:options:`
- `/CIImage/initWithData:options:`
- `/CIImage/imageWithCGImageSource:index:options:`
- `/CIImage/initWithCGImageSource:index:options:`

> [!note] Note
> The `kCGImageSourceUseHardwareAcceleration` key can also be used for this purpose.
