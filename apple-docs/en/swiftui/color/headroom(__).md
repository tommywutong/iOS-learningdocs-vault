---
title: 'headroom(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/color/headroom(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/color/headroom(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/color/headroom%28_%3A%29.json'
content_hash: 'sha256:8c2a7825bcb7c4c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Color](../color.md)

# headroom(_:)

<sub>Instance Method</sub>

Creates a new color with specified HDR content headroom.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func headroom(_ headroom: Double?) -> Color
```

## Parameters

- `headroom` — The headroom value to associate with the new color.

## Return Value

A new color with the specified content headroom.

## Discussion

High Dynamic Range colors (those with RGB components outside the standard [0, 1] range) should be annotated with their headroom to ensure that they are displayed correctly. Knowing content headroom allows the rendering system to automatically increase display headroom when the color is displayed and to tone map the color when the available display headroom is insufficient to render the color as intended.

For example a custom yellow color whose brightness has been increased by two exposure levels:

```swift
Color(.sRGB, red: 1.83, green: 1.47, blue: 0)
    .headroom(4)
```

note that headroom is a linear quantity, and as such any color adjustments should typically be made in a linear color space.

## See Also

### Modifying a color

- [opacity(_:)](<opacity(__).md>) — Multiplies the opacity of the color by the given amount.
- [gradient](gradient.md) — Returns the standard gradient for the color `self`.
- [mix(with:by:in:)](<mix(with_by_in_).md>) — Returns a version of self mixed with `rhs` by the amount specified by `fraction`.
- [exposureAdjust(_:)](<exposureadjust(__).md>) — Returns a new color with an exposure adjustment applied.
