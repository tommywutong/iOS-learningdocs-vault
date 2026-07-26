---
title: Image.TemplateRenderingMode
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/image/templaterenderingmode
source_url: 'https://developer.apple.com/documentation/swiftui/image/templaterenderingmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/image/templaterenderingmode.json'
content_hash: 'sha256:133c54da3406c274'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Image](../image.md)

# Image.TemplateRenderingMode

<sub>Enumeration</sub>

A type that indicates how SwiftUI renders images.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum TemplateRenderingMode
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting rendering modes

- [Image.TemplateRenderingMode.original](templaterenderingmode/original.md) — A mode that renders pixels of bitmap images as-is.
- [Image.TemplateRenderingMode.template](templaterenderingmode/template.md) — A mode that renders all non-transparent pixels as the foreground color.

## See Also

### Specifying rendering behavior

- [antialiased(_:)](<antialiased(__).md>) — Specifies whether SwiftUI applies antialiasing when rendering the image.
- [symbolRenderingMode(_:)](<symbolrenderingmode(__).md>) — Sets the rendering mode for symbol images within this view.
- [renderingMode(_:)](<renderingmode(__).md>) — Indicates whether SwiftUI renders an image as-is, or by using a different mode.
- [interpolation(_:)](<interpolation(__).md>) — Specifies the current level of quality for rendering an image that requires interpolation.
- [Interpolation](interpolation.md) — The level of quality for rendering an image that requires interpolation, such as a scaled image.
