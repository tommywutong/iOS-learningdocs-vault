---
title: gradient
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/color/gradient
source_url: 'https://developer.apple.com/documentation/swiftui/color/gradient'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/color/gradient.json'
content_hash: 'sha256:38a12d305fc725dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Color](../color.md)

# gradient

<sub>Instance Property</sub>

Returns the standard gradient for the color `self`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var gradient: AnyGradient { get }
```

## Discussion

For example, filling a rectangle with a gradient derived from the standard blue color:

```swift
Rectangle().fill(.blue.gradient)
```

## See Also

### Modifying a color

- [opacity(_:)](<opacity(__).md>) — Multiplies the opacity of the color by the given amount.
- [mix(with:by:in:)](<mix(with_by_in_).md>) — Returns a version of self mixed with `rhs` by the amount specified by `fraction`.
- [exposureAdjust(_:)](<exposureadjust(__).md>) — Returns a new color with an exposure adjustment applied.
- [headroom(_:)](<headroom(__).md>) — Creates a new color with specified HDR content headroom.
