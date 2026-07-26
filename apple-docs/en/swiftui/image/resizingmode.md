---
title: Image.ResizingMode
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/image/resizingmode
source_url: 'https://developer.apple.com/documentation/swiftui/image/resizingmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/image/resizingmode.json'
content_hash: 'sha256:f794a598f149dd23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Image](../image.md)

# Image.ResizingMode

<sub>Enumeration</sub>

The modes that SwiftUI uses to resize an image to fit within its containing view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum ResizingMode
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting resizing modes

- [Image.ResizingMode.stretch](resizingmode/stretch.md) — A mode to enlarge or reduce the size of an image so that it fills the available space.
- [Image.ResizingMode.tile](resizingmode/tile.md) — A mode to repeat the image at its original size, as many times as necessary to fill the available space.

## See Also

### Configuring an image

- [Fitting images into available space](../fitting-images-into-available-space.md) — Adjust the size and shape of images in your app’s user interface by applying view modifiers.
- [imageScale(_:)](<../view/imagescale(__).md>) — Scales images within the view according to one of the relative sizes available including small, medium, and large images sizes.
- [imageScale](../environmentvalues/imagescale.md) — The image scale for this environment.
- [Scale](scale.md) — A scale to apply to vector images relative to text.
- [Orientation](orientation.md) — The orientation of an image.
