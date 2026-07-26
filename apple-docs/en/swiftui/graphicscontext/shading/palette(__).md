---
title: 'palette(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/shading/palette(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/shading/palette(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/shading/palette%28_%3A%29.json'
content_hash: 'sha256:a76bd025376650e4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [Shading](../shading.md)

# palette(_:)

<sub>Type Method</sub>

Returns a multilevel shading instance constructed from an array of shading instances.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func palette(_ array: [GraphicsContext.Shading]) -> GraphicsContext.Shading
```

## Parameters

- `array` — An array of shading instances. The array must contain at least one element.

## Return Value

A shading instance composed from the given instances.

## See Also

### Composite shading types

- [backdrop](backdrop.md) — A shading instance that draws a copy of the current background.
