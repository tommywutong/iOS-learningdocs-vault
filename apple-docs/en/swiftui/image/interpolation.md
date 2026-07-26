---
title: Image.Interpolation
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/image/interpolation
source_url: 'https://developer.apple.com/documentation/swiftui/image/interpolation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/image/interpolation.json'
content_hash: 'sha256:db09efa5b112def3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Image](../image.md)

# Image.Interpolation

<sub>Enumeration</sub>

The level of quality for rendering an image that requires interpolation, such as a scaled image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Interpolation
```

## Overview

The [interpolation(_:)](<interpolation(__).md>) modifier specifies the interpolation behavior when using the [resizable(capInsets:resizingMode:)](<resizable(capinsets_resizingmode_).md>) modifier on an [Image](../image.md). Use this behavior to prioritize rendering performance or image quality.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting interpolation options

- [Image.Interpolation.high](interpolation/high.md) — A value that indicates a high level of interpolation quality, which may slow down image rendering.
- [Image.Interpolation.low](interpolation/low.md) — A value that indicates a low level of interpolation quality, which may speed up image rendering.
- [Image.Interpolation.medium](interpolation/medium.md) — A value that indicates a medium level of interpolation quality, between the low- and high-quality values.
- [Image.Interpolation.none](interpolation/none.md) — A value that indicates SwiftUI doesn’t interpolate image data.

## See Also

### Specifying rendering behavior

- [antialiased(_:)](<antialiased(__).md>) — Specifies whether SwiftUI applies antialiasing when rendering the image.
- [symbolRenderingMode(_:)](<symbolrenderingmode(__).md>) — Sets the rendering mode for symbol images within this view.
- [renderingMode(_:)](<renderingmode(__).md>) — Indicates whether SwiftUI renders an image as-is, or by using a different mode.
- [interpolation(_:)](<interpolation(__).md>) — Specifies the current level of quality for rendering an image that requires interpolation.
- [TemplateRenderingMode](templaterenderingmode.md) — A type that indicates how SwiftUI renders images.
