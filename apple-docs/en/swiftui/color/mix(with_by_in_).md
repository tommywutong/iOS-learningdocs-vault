---
title: 'mix(with:by:in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/color/mix(with:by:in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/color/mix(with:by:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/color/mix%28with%3Aby%3Ain%3A%29.json'
content_hash: 'sha256:7026640fa42cb720'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Color](../color.md)

# mix(with:by:in:)

<sub>Instance Method</sub>

Returns a version of self mixed with `rhs` by the amount specified by `fraction`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func mix(with rhs: Color, by fraction: Double, in colorSpace: Gradient.ColorSpace = .perceptual) -> Color
```

## Parameters

- `rhs` — The color to mix `self` with.

- `fraction` — The amount of blending, `0.5` means `self` is mixed in equal parts with `rhs`.

- `colorSpace` — The color space used to mix the colors.

## Return Value

A new `Color` based on `self` and `rhs`.

## See Also

### Modifying a color

- [opacity(_:)](<opacity(__).md>) — Multiplies the opacity of the color by the given amount.
- [gradient](gradient.md) — Returns the standard gradient for the color `self`.
- [exposureAdjust(_:)](<exposureadjust(__).md>) — Returns a new color with an exposure adjustment applied.
- [headroom(_:)](<headroom(__).md>) — Creates a new color with specified HDR content headroom.
