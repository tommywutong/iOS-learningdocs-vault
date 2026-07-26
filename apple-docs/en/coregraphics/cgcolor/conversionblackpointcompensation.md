---
title: conversionBlackPointCompensation
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolor/conversionblackpointcompensation
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolor/conversionblackpointcompensation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolor/conversionblackpointcompensation.json'
content_hash: 'sha256:4d946ad6f388e959'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColor](../cgcolor.md)

# conversionBlackPointCompensation

<sub>Type Property</sub>

An option for whether to apply black point compensation when converting between color profiles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let conversionBlackPointCompensation: CFString
```

## Discussion

ICC profiles specify how to convert the lightest level of white between color spaces, but they do not specify how black should be converted. To account for this, set a value of [true](../../swift/true.md) for this key when creating a color conversion with the [CGColorConversionInfoCreateFromList](../cgcolorconversioninfocreatefromlist.md) function.
