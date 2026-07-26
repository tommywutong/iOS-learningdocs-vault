---
title: accessibilityReduceTransparency
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/accessibilityreducetransparency
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityreducetransparency'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/accessibilityreducetransparency.json'
content_hash: 'sha256:76967be24d7afb3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# accessibilityReduceTransparency

<sub>Instance Property</sub>

Whether the system preference for Reduce Transparency is enabled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var accessibilityReduceTransparency: Bool { get }
```

## Discussion

If this property’s value is true, UI (mainly window) backgrounds should not be semi-transparent; they should be opaque.

## See Also

### Improving legibility

- [accessibilityShowButtonShapes](accessibilityshowbuttonshapes.md) — Whether the system preference for Show Button Shapes is enabled. _(deprecated)_
- [legibilityWeight](legibilityweight.md) — The font weight to apply to text.
- [LegibilityWeight](../legibilityweight.md) — The Accessibility Bold Text user setting options.
