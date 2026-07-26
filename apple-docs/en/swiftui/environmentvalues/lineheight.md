---
title: lineHeight
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/lineheight
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/lineheight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/lineheight.json'
content_hash: 'sha256:4036992f3ea4950c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# lineHeight

<sub>Instance Property</sub>

The default line height for text influenced by this environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var lineHeight: AttributedString.LineHeight? { get set }
```

## Discussion

The default value is `nil`. In that case, SwiftUI automatically chooses an appropriate line height setting for each context.
