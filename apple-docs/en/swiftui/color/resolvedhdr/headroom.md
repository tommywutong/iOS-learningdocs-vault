---
title: headroom
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/color/resolvedhdr/headroom
source_url: 'https://developer.apple.com/documentation/swiftui/color/resolvedhdr/headroom'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/color/resolvedhdr/headroom.json'
content_hash: 'sha256:048f505bebd713e5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [Color](../../color.md) · [ResolvedHDR](../resolvedhdr.md)

# headroom

<sub>Instance Property</sub>

The content headroom of the color.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) var headroom: Float? { get set }
```

## Discussion

This is the ratio of nominal peak luminance (“peak white”) to nominal diffuse luminance (“reference white” or “diffuse white”). Headroom is a linear quantity, i.e. there is no gamma function applied to it.

## See Also

### Getting color properties

- [red](red.md) — The amount of red in the color in the extended sRGB color space.
- [green](green.md) — The amount of green in the color in the extended sRGB color space.
- [blue](blue.md) — The amount of blue in the color in the extended sRGB color space.
- [linearRed](linearred.md) — The amount of red in the color in the extended sRGB color space variant with linear gamma.
- [linearGreen](lineargreen.md) — The amount of green in the color in the extended sRGB color space variant with linear gamma.
- [linearBlue](linearblue.md) — The amount of blue in the color in the extended sRGB color space variant with linear gamma.
- [opacity](opacity.md) — The opacity of the color, in the range `0` to `1`.
