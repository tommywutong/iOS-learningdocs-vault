---
title: AnyCompositorContent
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/anycompositorcontent
source_url: 'https://developer.apple.com/documentation/swiftui/anycompositorcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/anycompositorcontent.json'
content_hash: 'sha256:1c4f3507e1a3d1a7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AnyCompositorContent

<sub>Structure</sub>

Type erased compositor content.

<sub>macOS, visionOS</sub>

```swift
nonisolated struct AnyCompositorContent
```

## Relationships

- **Conforms To**: [CompositorContent](compositorcontent.md)

## Topics

### Initializers

- [init(_:)](<anycompositorcontent/init(__).md>) — Create an instance that type-erases `CompositorContent`.
- [init(erasing:)](<anycompositorcontent/init(erasing_).md>)

## See Also

### Compositing views

- [blendMode(_:)](<view/blendmode(__).md>) — Sets the blend mode for compositing this view with overlapping views.
- [compositingGroup()](<view/compositinggroup().md>) — Wraps this view in a compositing group.
- [drawingGroup(opaque:colorMode:)](<view/drawinggroup(opaque_colormode_).md>) — Composites this view’s contents into an offscreen image before final display.
- [BlendMode](blendmode.md) — Modes for compositing a view with overlapping content.
- [ColorRenderingMode](colorrenderingmode.md) — The set of possible working color spaces for color-compositing operations.
- [CompositorContent](compositorcontent.md)
- [CompositorContentBuilder](compositorcontentbuilder.md) — A result builder for composing a collection of [CompositorContent](compositorcontent.md) elements.
