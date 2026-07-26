---
title: GlassBackgroundEffect
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [visionOS 2.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/glassbackgroundeffect
source_url: 'https://developer.apple.com/documentation/swiftui/glassbackgroundeffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/glassbackgroundeffect.json'
content_hash: 'sha256:260fc4c2e3d96cff'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# GlassBackgroundEffect

<sub>Protocol</sub>

A specification for the appearance of a glass background.

<sub>visionOS</sub>

```swift
protocol GlassBackgroundEffect
```

## Relationships

- **Conforming Types**: [AutomaticGlassBackgroundEffect](automaticglassbackgroundeffect.md), [FeatheredGlassBackgroundEffect](featheredglassbackgroundeffect.md), [PlateGlassBackgroundEffect](plateglassbackgroundeffect.md)

## Topics

### Associated Types

- [Body](glassbackgroundeffect/body.md) — The type of effect representing the body of this effect. When you create a custom effect, Swift infers this type from your implementation of the required [makeBody(configuration:)](<glassbackgroundeffect/makebody(configuration_).md>) method.

### Instance Methods

- [makeBody(configuration:)](<glassbackgroundeffect/makebody(configuration_).md>) — Defines the effect produced by this effect.

### Type Aliases

- [Configuration](glassbackgroundeffect/configuration.md) — The configuration type passed to `makeBody(configuration:)`.

### Type Properties

- [automatic](glassbackgroundeffect/automatic.md) — The default glass background effect, based on the glass’s context.
- [feathered](glassbackgroundeffect/feathered.md) — A feathered background effect with default padding amount and default soft edge radial size.
- [plate](glassbackgroundeffect/plate.md) — A plate glass background effect.

### Type Methods

- [feathered(padding:softEdgeRadius:)](<glassbackgroundeffect/feathered(padding_softedgeradius_).md>) — A feathered background effect with custom padding and soft edge radius.

## See Also

### Adding a glass background on views in visionOS

- [glassBackgroundEffect(displayMode:)](<view/glassbackgroundeffect(displaymode_).md>) — Fills the view’s background with an automatic glass background effect and container-relative rounded rectangle shape.
- [glassBackgroundEffect(in:displayMode:)](<view/glassbackgroundeffect(in_displaymode_).md>) — Fills the view’s background with an automatic glass background effect and a shape that you specify.
- [GlassBackgroundDisplayMode](glassbackgrounddisplaymode.md) — The display mode of a glass background.
- [AutomaticGlassBackgroundEffect](automaticglassbackgroundeffect.md) — The automatic glass background effect.
- [GlassBackgroundEffectConfiguration](glassbackgroundeffectconfiguration.md) — A configuration used to build a custom effect.
- [FeatheredGlassBackgroundEffect](featheredglassbackgroundeffect.md) — The feathered glass background effect.
- [PlateGlassBackgroundEffect](plateglassbackgroundeffect.md) — The plate glass background effect.
