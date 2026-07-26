---
title: labelReservedIconWidth
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/labelreservediconwidth
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/labelreservediconwidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/labelreservediconwidth.json'
content_hash: 'sha256:fadbad7e94870ed4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# labelReservedIconWidth

<sub>Instance Property</sub>

The width reserved for icons in labels.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var labelReservedIconWidth: CGFloat? { get }
```

## Discussion

The value that should be used for the reserved icon width in labels. To set a different value for labels, use the `labelReservedIconWidth` modifier.

This environment value can be used in custom label styles to allow changing the reserved icon width using the `labelReservedIconWidth` modifier. If the value is `nil`, a default behavior to size the icon should be used instead.
