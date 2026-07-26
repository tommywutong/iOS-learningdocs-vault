---
title: default
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/font/default
source_url: 'https://developer.apple.com/documentation/swiftui/font/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/font/default.json'
content_hash: 'sha256:5ccc472de0e6a122'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Font](../font.md)

# default

<sub>Type Property</sub>

The effective SwiftUI font used in any given environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var `default`: Font { get }
```

## Discussion

The font specified by environment, preferring first any developer specified font, via [font](../environmentvalues/font.md), then any framework specified font, and finally the default SwiftUI font.
