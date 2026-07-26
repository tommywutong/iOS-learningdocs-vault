---
title: BlendMode
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/blendmode
source_url: 'https://developer.apple.com/documentation/swiftui/blendmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/blendmode.json'
content_hash: 'sha256:315f9e4fd5d225fb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# BlendMode

<sub>Enumeration</sub>

Modes for compositing a view with overlapping content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum BlendMode
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the default

- [BlendMode.normal](blendmode/normal.md)

### Darkening

- [BlendMode.darken](blendmode/darken.md)
- [BlendMode.multiply](blendmode/multiply.md)
- [BlendMode.colorBurn](blendmode/colorburn.md)
- [BlendMode.plusDarker](blendmode/plusdarker.md)

### Lightening

- [BlendMode.lighten](blendmode/lighten.md)
- [BlendMode.screen](blendmode/screen.md)
- [BlendMode.colorDodge](blendmode/colordodge.md)
- [BlendMode.plusLighter](blendmode/pluslighter.md)

### Adding contrast

- [BlendMode.overlay](blendmode/overlay.md)
- [BlendMode.softLight](blendmode/softlight.md)
- [BlendMode.hardLight](blendmode/hardlight.md)

### Inverting

- [BlendMode.difference](blendmode/difference.md)
- [BlendMode.exclusion](blendmode/exclusion.md)

### Mixing color components

- [BlendMode.hue](blendmode/hue.md)
- [BlendMode.saturation](blendmode/saturation.md)
- [BlendMode.color](blendmode/color.md)
- [BlendMode.luminosity](blendmode/luminosity.md)

### Accessing Porter-Duff modes

- [BlendMode.sourceAtop](blendmode/sourceatop.md)
- [BlendMode.destinationOver](blendmode/destinationover.md)
- [BlendMode.destinationOut](blendmode/destinationout.md)

## See Also

### Compositing views

- [blendMode(_:)](<view/blendmode(__).md>) — Sets the blend mode for compositing this view with overlapping views.
- [compositingGroup()](<view/compositinggroup().md>) — Wraps this view in a compositing group.
- [drawingGroup(opaque:colorMode:)](<view/drawinggroup(opaque_colormode_).md>) — Composites this view’s contents into an offscreen image before final display.
- [ColorRenderingMode](colorrenderingmode.md) — The set of possible working color spaces for color-compositing operations.
- [CompositorContent](compositorcontent.md)
- [CompositorContentBuilder](compositorcontentbuilder.md) — A result builder for composing a collection of [CompositorContent](compositorcontent.md) elements.
- [AnyCompositorContent](anycompositorcontent.md) — Type erased compositor content.
