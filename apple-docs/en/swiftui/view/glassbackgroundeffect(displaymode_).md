---
title: 'glassBackgroundEffect(displayMode:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/glassbackgroundeffect(displaymode:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/glassbackgroundeffect(displaymode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/glassbackgroundeffect%28displaymode%3A%29.json'
content_hash: 'sha256:21cb6b2988870112'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# glassBackgroundEffect(displayMode:)

<sub>Instance Method</sub>

Fills the view’s background with an automatic glass background effect and container-relative rounded rectangle shape.

<sub>visionOS</sub>

```swift
nonisolated func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode = .always) -> some View

```

## Parameters

- `displayMode` — When to display the glass background. The default is [GlassBackgroundDisplayMode.always](../glassbackgrounddisplaymode/always.md).

## Return Value

A view with a glass background.

## Discussion

Use this modifier to add a 3D glass background material that includes thickness, specularity, glass blur, shadows, and other effects. Because of its physical depth, the glass background influences z-axis layout.

To ensure that the effect renders properly when you add it to a collection of views in a [ZStack](../zstack.md), add the modifier to the stack rather to one of the views in the stack. This includes when you create an implicit stack with view modifiers like [overlay(alignment:content:)](<overlay(alignment_content_).md>) or [background(alignment:content:)](<background(alignment_content_).md>). In those cases, you might need to create an explicit [ZStack](../zstack.md) inside the `content` closure to have a place to add the glass background modifier.

## See Also

### Adding a glass background on views in visionOS

- [glassBackgroundEffect(in:displayMode:)](<glassbackgroundeffect(in_displaymode_).md>) — Fills the view’s background with an automatic glass background effect and a shape that you specify.
- [GlassBackgroundDisplayMode](../glassbackgrounddisplaymode.md) — The display mode of a glass background.
- [GlassBackgroundEffect](../glassbackgroundeffect.md) — A specification for the appearance of a glass background.
- [AutomaticGlassBackgroundEffect](../automaticglassbackgroundeffect.md) — The automatic glass background effect.
- [GlassBackgroundEffectConfiguration](../glassbackgroundeffectconfiguration.md) — A configuration used to build a custom effect.
- [FeatheredGlassBackgroundEffect](../featheredglassbackgroundeffect.md) — The feathered glass background effect.
- [PlateGlassBackgroundEffect](../plateglassbackgroundeffect.md) — The plate glass background effect.
