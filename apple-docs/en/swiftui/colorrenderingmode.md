---
title: ColorRenderingMode
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/colorrenderingmode
source_url: 'https://developer.apple.com/documentation/swiftui/colorrenderingmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/colorrenderingmode.json'
content_hash: 'sha256:046aa8ccce70fa76'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ColorRenderingMode

<sub>Enumeration</sub>

The set of possible working color spaces for color-compositing operations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum ColorRenderingMode
```

## Overview

Each color space guarantees the preservation of a particular range of color values.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting rendering modes

- [ColorRenderingMode.extendedLinear](colorrenderingmode/extendedlinear.md) — The extended linear sRGB working color space.
- [ColorRenderingMode.linear](colorrenderingmode/linear.md) — The linear sRGB working color space.
- [ColorRenderingMode.nonLinear](colorrenderingmode/nonlinear.md) — The non-linear sRGB working color space.

## See Also

### Compositing views

- [blendMode(_:)](<view/blendmode(__).md>) — Sets the blend mode for compositing this view with overlapping views.
- [compositingGroup()](<view/compositinggroup().md>) — Wraps this view in a compositing group.
- [drawingGroup(opaque:colorMode:)](<view/drawinggroup(opaque_colormode_).md>) — Composites this view’s contents into an offscreen image before final display.
- [BlendMode](blendmode.md) — Modes for compositing a view with overlapping content.
- [CompositorContent](compositorcontent.md)
- [CompositorContentBuilder](compositorcontentbuilder.md) — A result builder for composing a collection of [CompositorContent](compositorcontent.md) elements.
- [AnyCompositorContent](anycompositorcontent.md) — Type erased compositor content.
