---
title: 'opacity(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/color/opacity(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/color/opacity(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/color/opacity%28_%3A%29.json'
content_hash: 'sha256:0f1b5eaab299713d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Color](../color.md)

# opacity(_:)

<sub>Instance Method</sub>

Multiplies the opacity of the color by the given amount.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func opacity(_ opacity: Double) -> Color
```

## Parameters

- `opacity` — The amount by which to multiply the opacity of the color.

## Return Value

A view with modified opacity.

## See Also

### Modifying a color

- [gradient](gradient.md) — Returns the standard gradient for the color `self`.
- [mix(with:by:in:)](<mix(with_by_in_).md>) — Returns a version of self mixed with `rhs` by the amount specified by `fraction`.
- [exposureAdjust(_:)](<exposureadjust(__).md>) — Returns a new color with an exposure adjustment applied.
- [headroom(_:)](<headroom(__).md>) — Creates a new color with specified HDR content headroom.
