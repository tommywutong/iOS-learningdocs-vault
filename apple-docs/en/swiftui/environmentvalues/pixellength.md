---
title: pixelLength
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/pixellength
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/pixellength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/pixellength.json'
content_hash: 'sha256:cf92d3b7e46f6feb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# pixelLength

<sub>Instance Property</sub>

The size of a pixel on the screen.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var pixelLength: CGFloat { get }
```

## Discussion

This value is usually equal to `1` divided by [displayScale](displayscale.md).

## See Also

### Reacting to interface characteristics

- [isLuminanceReduced](isluminancereduced.md) — A Boolean value that indicates whether the display or environment currently requires reduced luminance.
- [displayScale](displayscale.md) — The display scale of this environment.
- [horizontalSizeClass](horizontalsizeclass.md) — The horizontal size class of this environment.
- [verticalSizeClass](verticalsizeclass.md) — The vertical size class of this environment.
- [UserInterfaceSizeClass](../userinterfacesizeclass.md) — A set of values that indicate the visual size available to the view.
