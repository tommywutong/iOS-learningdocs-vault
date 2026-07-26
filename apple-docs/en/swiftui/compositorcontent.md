---
title: CompositorContent
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/compositorcontent
source_url: 'https://developer.apple.com/documentation/swiftui/compositorcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/compositorcontent.json'
content_hash: 'sha256:21791d154fc5a992'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# CompositorContent

<sub>Protocol</sub>

<sub>macOS, visionOS</sub>

```swift
@MainActor protocol CompositorContent
```

## Relationships

- **Conforming Types**: [AnyCompositorContent](anycompositorcontent.md), [Content](compositorcontentbuilder/content.md)

## Topics

### Associated Types

- [Body](compositorcontent/body-swift.associatedtype.md)

### Instance Properties

- [body](compositorcontent/body-swift.property.md)

### Instance Methods

- [contentCaptureProtected(_:)](<compositorcontent/contentcaptureprotected(__).md>) — Marks the view as a view that activates content protection during scene capture events, such as screenshots, screen recordings, screensharing, etc.
- [onAppear(perform:)](<compositorcontent/onappear(perform_).md>) — Adds an action to perform before this content appears.
- [onChange(of:initial:_:)](<compositorcontent/onchange(of_initial___).md>)
- [onDisappear(perform:)](<compositorcontent/ondisappear(perform_).md>) — Adds an action to perform after this content disappears.
- [onImmersionChange(initial:_:)](<compositorcontent/onimmersionchange(initial___).md>) — Performs an action when the immersion state of your app changes.
- [onWorldRecenter(action:)](<compositorcontent/onworldrecenter(action_).md>) — Adds an action to perform when recentering the view with the digital crown.
- [persistentSystemOverlays(_:)](<compositorcontent/persistentsystemoverlays(__).md>) — Sets the preferred visibility of the non-transient system views overlaying the app.
- [preferredSurroundingsEffect(_:)](<compositorcontent/preferredsurroundingseffect(__).md>) — Applies an effect to passthrough video.
- [upperLimbVisibility(_:)](<compositorcontent/upperlimbvisibility(__).md>) — Sets the preferred visibility of the user’s upper limbs, while an [ImmersiveSpace](immersivespace.md) scene is presented.

## See Also

### Compositing views

- [blendMode(_:)](<view/blendmode(__).md>) — Sets the blend mode for compositing this view with overlapping views.
- [compositingGroup()](<view/compositinggroup().md>) — Wraps this view in a compositing group.
- [drawingGroup(opaque:colorMode:)](<view/drawinggroup(opaque_colormode_).md>) — Composites this view’s contents into an offscreen image before final display.
- [BlendMode](blendmode.md) — Modes for compositing a view with overlapping content.
- [ColorRenderingMode](colorrenderingmode.md) — The set of possible working color spaces for color-compositing operations.
- [CompositorContentBuilder](compositorcontentbuilder.md) — A result builder for composing a collection of [CompositorContent](compositorcontent.md) elements.
- [AnyCompositorContent](anycompositorcontent.md) — Type erased compositor content.
