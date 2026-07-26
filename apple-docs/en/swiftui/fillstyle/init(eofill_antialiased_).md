---
title: 'init(eoFill:antialiased:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/fillstyle/init(eofill:antialiased:)'
source_url: 'https://developer.apple.com/documentation/swiftui/fillstyle/init(eofill:antialiased:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/fillstyle/init%28eofill%3Aantialiased%3A%29.json'
content_hash: 'sha256:6fd6321754a2fede'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FillStyle](../fillstyle.md)

# init(eoFill:antialiased:)

<sub>Initializer</sub>

Creates a new fill style with the specified settings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(eoFill: Bool = false, antialiased: Bool = true)
```

## Parameters

- `eoFill` — A Boolean value that indicates whether to use the even-odd rule for rendering a shape. Pass `false` to use the non-zero winding number rule instead.

- `antialiased` — A Boolean value that indicates whether to use antialiasing when rendering the edges of a shape.
