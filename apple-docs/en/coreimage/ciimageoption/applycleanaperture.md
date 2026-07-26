---
title: applyCleanAperture
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimageoption/applycleanaperture
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageoption/applycleanaperture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageoption/applycleanaperture.json'
content_hash: 'sha256:882b8db40e658a6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageOption](../ciimageoption.md)

# applyCleanAperture

<sub>Type Property</sub>

A Boolean value to control whether an image created with a CVPixelBuffer or an IOSurface should be cropped and offset according clean aperture attachments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let applyCleanAperture: CIImageOption
```

## Discussion

For a `CVPixelBuffer` this will use `kCVImageBufferPreferredCleanApertureKey` or `kCVImageBufferCleanApertureKey`.

If the value for this option is:

- True: then image will be cropped and offset to the clean aperture.
- False: then the full image is returned.
- [CIVector](../civector.md) : then use it as a `CGRect` to crop and offset.
- Not specified : then it will behave as if False was specified.
