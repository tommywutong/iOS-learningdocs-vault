---
title: CompositorContentBuilder
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/compositorcontentbuilder
source_url: 'https://developer.apple.com/documentation/swiftui/compositorcontentbuilder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/compositorcontentbuilder.json'
content_hash: 'sha256:07698fa88eaae2c7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# CompositorContentBuilder

<sub>Structure</sub>

A result builder for composing a collection of [CompositorContent](compositorcontent.md) elements.

<sub>macOS, visionOS</sub>

```swift
@resultBuilder struct CompositorContentBuilder
```

## Topics

### Structures

- [Content](compositorcontentbuilder/content.md) — A representation of the content of a compositor content builder.

### Type Methods

- [buildBlock(_:)](<compositorcontentbuilder/buildblock(__).md>)
- [buildEither(first:)](<compositorcontentbuilder/buildeither(first_).md>) — Produces content for a conditional statement in a multi-statement closure when the condition is true.
- [buildEither(second:)](<compositorcontentbuilder/buildeither(second_).md>) — Produces content for a conditional statement in a multi-statement closure when the condition is false.
- [buildExpression(_:)](<compositorcontentbuilder/buildexpression(__).md>)
- [buildLimitedAvailability(_:)](<compositorcontentbuilder/buildlimitedavailability(__).md>) — Processes scene content for a conditional compiler-control statement that performs an availability check.

## See Also

### Compositing views

- [blendMode(_:)](<view/blendmode(__).md>) — Sets the blend mode for compositing this view with overlapping views.
- [compositingGroup()](<view/compositinggroup().md>) — Wraps this view in a compositing group.
- [drawingGroup(opaque:colorMode:)](<view/drawinggroup(opaque_colormode_).md>) — Composites this view’s contents into an offscreen image before final display.
- [BlendMode](blendmode.md) — Modes for compositing a view with overlapping content.
- [ColorRenderingMode](colorrenderingmode.md) — The set of possible working color spaces for color-compositing operations.
- [CompositorContent](compositorcontent.md)
- [AnyCompositorContent](anycompositorcontent.md) — Type erased compositor content.
