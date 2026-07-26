---
title: 'exposureAdjust(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/color/exposureadjust(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/color/exposureadjust(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/color/exposureadjust%28_%3A%29.json'
content_hash: 'sha256:fb9db6bdea4681cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Color](../color.md)

# exposureAdjust(_:)

<sub>Instance Method</sub>

Returns a new color with an exposure adjustment applied.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) func exposureAdjust(_ stops: Double) -> Color
```

## Parameters

- `stops` — The number of exposure levels to adjust by.

## Return Value

A new color with the exposure adjustment applied.

## Discussion

This function adjusts the exposure of a color by multipling its linear-light representation by `pow(2, stops)` and adjusting its HDR content headroom.

For example the system yellow color could have its brightness increased by two exposure levels:

```swift
Color.yellow.exposureAdjust(2)
```

## See Also

### Modifying a color

- [opacity(_:)](<opacity(__).md>) — Multiplies the opacity of the color by the given amount.
- [gradient](gradient.md) — Returns the standard gradient for the color `self`.
- [mix(with:by:in:)](<mix(with_by_in_).md>) — Returns a version of self mixed with `rhs` by the amount specified by `fraction`.
- [headroom(_:)](<headroom(__).md>) — Creates a new color with specified HDR content headroom.
