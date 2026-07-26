---
title: ColorRenderingMode.nonLinear
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/colorrenderingmode/nonlinear
source_url: 'https://developer.apple.com/documentation/swiftui/colorrenderingmode/nonlinear'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/colorrenderingmode/nonlinear.json'
content_hash: 'sha256:87829fc8c30f69fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ColorRenderingMode](../colorrenderingmode.md)

# ColorRenderingMode.nonLinear

<sub>Case</sub>

The non-linear sRGB working color space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case nonLinear
```

## Discussion

Color component values outside the range `[0, 1]` produce undefined results. This color space is gamma corrected.

## See Also

### Getting rendering modes

- [ColorRenderingMode.extendedLinear](extendedlinear.md) — The extended linear sRGB working color space.
- [ColorRenderingMode.linear](linear.md) — The linear sRGB working color space.
