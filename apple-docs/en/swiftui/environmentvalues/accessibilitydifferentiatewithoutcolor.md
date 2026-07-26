---
title: accessibilityDifferentiateWithoutColor
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/accessibilitydifferentiatewithoutcolor
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilitydifferentiatewithoutcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/accessibilitydifferentiatewithoutcolor.json'
content_hash: 'sha256:1b8bb267904d9543'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# accessibilityDifferentiateWithoutColor

<sub>Instance Property</sub>

Whether the system preference for Differentiate without Color is enabled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var accessibilityDifferentiateWithoutColor: Bool { get }
```

## Discussion

If this is true, UI should not convey information using color alone and instead should use shapes or glyphs to convey information.

## See Also

### Managing color

- [accessibilityIgnoresInvertColors(_:)](<../view/accessibilityignoresinvertcolors(__).md>) — Sets whether this view should ignore the system Smart Invert setting.
- [accessibilityInvertColors](accessibilityinvertcolors.md) — Whether the system preference for Invert Colors is enabled.
