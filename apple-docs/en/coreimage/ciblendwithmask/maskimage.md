---
title: maskImage
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciblendwithmask/maskimage
source_url: 'https://developer.apple.com/documentation/coreimage/ciblendwithmask/maskimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciblendwithmask/maskimage.json'
content_hash: 'sha256:4b952950337f46e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIBlendWithMask](../ciblendwithmask.md)

# maskImage

<sub>Instance Property</sub>

A grayscale mask that defines the blend.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maskImage: CIImage? { get set }
```

## Discussion

When a mask value is 0.0, the result is the background. When the mask value is 1.0, the result is the image.

## See Also

### Instance Properties

- [backgroundImage](backgroundimage.md) — The image to use as a background image.
- [inputImage](inputimage.md) — The image to use as a foreground image.
