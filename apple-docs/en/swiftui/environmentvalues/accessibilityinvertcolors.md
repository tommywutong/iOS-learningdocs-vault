---
title: accessibilityInvertColors
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/accessibilityinvertcolors
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityinvertcolors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/accessibilityinvertcolors.json'
content_hash: 'sha256:1d2b727d23df9dd7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# accessibilityInvertColors

<sub>Instance Property</sub>

Whether the system preference for Invert Colors is enabled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var accessibilityInvertColors: Bool { get }
```

## Discussion

If this property’s value is true then the display will be inverted. In these cases it may be needed for UI drawing to be adjusted to in order to display optimally when inverted.

## See Also

### Managing color

- [accessibilityIgnoresInvertColors(_:)](<../view/accessibilityignoresinvertcolors(__).md>) — Sets whether this view should ignore the system Smart Invert setting.
- [accessibilityDifferentiateWithoutColor](accessibilitydifferentiatewithoutcolor.md) — Whether the system preference for Differentiate without Color is enabled.
