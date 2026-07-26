---
title: isEOFilled
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/fillstyle/iseofilled
source_url: 'https://developer.apple.com/documentation/swiftui/fillstyle/iseofilled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/fillstyle/iseofilled.json'
content_hash: 'sha256:c96518374d462a4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FillStyle](../fillstyle.md)

# isEOFilled

<sub>Instance Property</sub>

A Boolean value that indicates whether to use the even-odd rule when rendering a shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isEOFilled: Bool
```

## Discussion

When `isOEFilled` is `false`, the style uses the non-zero winding number rule.

## See Also

### Setting fill style properties

- [isAntialiased](isantialiased.md) — A Boolean value that indicates whether to apply antialiasing to the edges of a shape.
