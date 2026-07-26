---
title: 'antialiased(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/image/antialiased(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/image/antialiased(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/image/antialiased%28_%3A%29.json'
content_hash: 'sha256:67132ff36a470336'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Image](../image.md)

# antialiased(_:)

<sub>Instance Method</sub>

Specifies whether SwiftUI applies antialiasing when rendering the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func antialiased(_ isAntialiased: Bool) -> Image
```

## Parameters

- `isAntialiased` — A Boolean value that specifies whether to allow antialiasing. Pass `true` to allow antialising, `false` otherwise.

## Return Value

An image with the antialiasing behavior set.

## See Also

### Specifying rendering behavior

- [symbolRenderingMode(_:)](<symbolrenderingmode(__).md>) — Sets the rendering mode for symbol images within this view.
- [renderingMode(_:)](<renderingmode(__).md>) — Indicates whether SwiftUI renders an image as-is, or by using a different mode.
- [interpolation(_:)](<interpolation(__).md>) — Specifies the current level of quality for rendering an image that requires interpolation.
- [TemplateRenderingMode](templaterenderingmode.md) — A type that indicates how SwiftUI renders images.
- [Interpolation](interpolation.md) — The level of quality for rendering an image that requires interpolation, such as a scaled image.
