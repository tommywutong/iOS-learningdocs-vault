---
title: accessibilityReduceHighlightingEffects
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, tvOS 26.4+, visionOS 26.4+, watchOS 26.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/accessibilityreducehighlightingeffects
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityreducehighlightingeffects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/accessibilityreducehighlightingeffects.json'
content_hash: 'sha256:dd73662a6997bdaf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# accessibilityReduceHighlightingEffects

<sub>Instance Property</sub>

Whether the system preference for Reduce Bright Effects is enabled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var accessibilityReduceHighlightingEffects: Bool { get }
```

## Discussion

If this property’s value is true, controls, such as buttons, should be drawn in such a way that minimizes highlighting and flashing of onscreen elements.
