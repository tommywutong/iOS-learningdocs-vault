---
title: 'measure(in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/resolvedtext/measure(in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/resolvedtext/measure(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/resolvedtext/measure%28in%3A%29.json'
content_hash: 'sha256:9650304adeaf9efe'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [ResolvedText](../resolvedtext.md)

# measure(in:)

<sub>Instance Method</sub>

Measures the size of the resolved text for a given area into which the text should be placed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func measure(in size: CGSize) -> CGSize
```

## Parameters

- `size` — The area to place the [Text](../../text.md) view in.

## See Also

### Getting the text properties

- [firstBaseline(in:)](<firstbaseline(in_).md>) — Gets the distance from the first line’s ascender to its baseline.
- [lastBaseline(in:)](<lastbaseline(in_).md>) — Gets the distance from the first line’s ascender to the last line’s baseline.
- [shading](shading.md) — The shading to fill uncolored text regions with.
