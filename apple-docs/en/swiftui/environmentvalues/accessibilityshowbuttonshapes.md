---
title: accessibilityShowButtonShapes
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+（1000.0 起废弃）, iPadOS 14.0+（1000.0 起废弃）, Mac Catalyst 14.0+（1000.0 起废弃）, macOS 11.0+（1000.0 起废弃）, tvOS 14.0+（1000.0 起废弃）, visionOS 1.0+（1000.0 起废弃）, watchOS 7.0+（1000.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/environmentvalues/accessibilityshowbuttonshapes
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityshowbuttonshapes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/accessibilityshowbuttonshapes.json'
content_hash: 'sha256:048af5b4e116fe99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# accessibilityShowButtonShapes

<sub>Instance Property</sub>

Whether the system preference for Show Button Shapes is enabled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var accessibilityShowButtonShapes: Bool { get }
```

## Discussion

If this property’s value is true, interactive custom controls such as buttons should be drawn in such a way that their edges and borders are clearly visible.

## See Also

### Improving legibility

- [accessibilityReduceTransparency](accessibilityreducetransparency.md) — Whether the system preference for Reduce Transparency is enabled.
- [legibilityWeight](legibilityweight.md) — The font weight to apply to text.
- [LegibilityWeight](../legibilityweight.md) — The Accessibility Bold Text user setting options.
