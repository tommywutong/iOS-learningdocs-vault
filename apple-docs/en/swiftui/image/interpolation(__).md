---
title: 'interpolation(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/image/interpolation(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/image/interpolation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/image/interpolation%28_%3A%29.json'
content_hash: 'sha256:f1c81fd4fff507ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Image](../image.md)

# interpolation(_:)

<sub>Instance Method</sub>

Specifies the current level of quality for rendering an image that requires interpolation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func interpolation(_ interpolation: Image.Interpolation) -> Image
```

## Parameters

- `interpolation` — The quality level, expressed as a value of the `Interpolation` type, that SwiftUI applies when interpolating an image.

## Return Value

An image with the given interpolation value set.

## Discussion

See the article [Fitting images into available space](../fitting-images-into-available-space.md) for examples of using `interpolation(_:)` when scaling an [Image](../image.md).

## See Also

### Specifying rendering behavior

- [antialiased(_:)](<antialiased(__).md>) — Specifies whether SwiftUI applies antialiasing when rendering the image.
- [symbolRenderingMode(_:)](<symbolrenderingmode(__).md>) — Sets the rendering mode for symbol images within this view.
- [renderingMode(_:)](<renderingmode(__).md>) — Indicates whether SwiftUI renders an image as-is, or by using a different mode.
- [TemplateRenderingMode](templaterenderingmode.md) — A type that indicates how SwiftUI renders images.
- [Interpolation](interpolation.md) — The level of quality for rendering an image that requires interpolation, such as a scaled image.
