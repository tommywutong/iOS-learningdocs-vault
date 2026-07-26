---
title: 'symbolRenderingMode(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/image/symbolrenderingmode(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/image/symbolrenderingmode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/image/symbolrenderingmode%28_%3A%29.json'
content_hash: 'sha256:8ebb13c76c74f8e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Image](../image.md)

# symbolRenderingMode(_:)

<sub>Instance Method</sub>

Sets the rendering mode for symbol images within this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func symbolRenderingMode(_ mode: SymbolRenderingMode?) -> Image
```

## Parameters

- `mode` — The symbol rendering mode to use.

## Return Value

A view that uses the rendering mode you supply.

## See Also

### Specifying rendering behavior

- [antialiased(_:)](<antialiased(__).md>) — Specifies whether SwiftUI applies antialiasing when rendering the image.
- [renderingMode(_:)](<renderingmode(__).md>) — Indicates whether SwiftUI renders an image as-is, or by using a different mode.
- [interpolation(_:)](<interpolation(__).md>) — Specifies the current level of quality for rendering an image that requires interpolation.
- [TemplateRenderingMode](templaterenderingmode.md) — A type that indicates how SwiftUI renders images.
- [Interpolation](interpolation.md) — The level of quality for rendering an image that requires interpolation, such as a scaled image.
