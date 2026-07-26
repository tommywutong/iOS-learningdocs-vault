---
title: FeatheredGlassBackgroundEffect
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 2.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/featheredglassbackgroundeffect
source_url: 'https://developer.apple.com/documentation/swiftui/featheredglassbackgroundeffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/featheredglassbackgroundeffect.json'
content_hash: 'sha256:a45e1fc560506c66'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# FeatheredGlassBackgroundEffect

<sub>Structure</sub>

The feathered glass background effect.

<sub>visionOS</sub>

```swift
struct FeatheredGlassBackgroundEffect
```

## Overview

You can also use [feathered](glassbackgroundeffect/feathered.md) to construct this effect.

The layout size of a view with feathered glass background is based on the content size instead of the glass background size. When the glass background is clipped by an outer container, such as VStack or HStack, it can be resolved by increasing content size, such as content padding, or reducing the feathered glass background size with its padding parameter.

## Relationships

- **Conforms To**: [GlassBackgroundEffect](glassbackgroundeffect.md)

## Topics

### Initializers

- [init()](<featheredglassbackgroundeffect/init().md>) — Creates a feathered glass background effect.
- [init(padding:softEdgeRadius:)](<featheredglassbackgroundeffect/init(padding_softedgeradius_).md>) — Creates a feathered glassBackground effect.

## See Also

### Adding a glass background on views in visionOS

- [glassBackgroundEffect(displayMode:)](<view/glassbackgroundeffect(displaymode_).md>) — Fills the view’s background with an automatic glass background effect and container-relative rounded rectangle shape.
- [glassBackgroundEffect(in:displayMode:)](<view/glassbackgroundeffect(in_displaymode_).md>) — Fills the view’s background with an automatic glass background effect and a shape that you specify.
- [GlassBackgroundDisplayMode](glassbackgrounddisplaymode.md) — The display mode of a glass background.
- [GlassBackgroundEffect](glassbackgroundeffect.md) — A specification for the appearance of a glass background.
- [AutomaticGlassBackgroundEffect](automaticglassbackgroundeffect.md) — The automatic glass background effect.
- [GlassBackgroundEffectConfiguration](glassbackgroundeffectconfiguration.md) — A configuration used to build a custom effect.
- [PlateGlassBackgroundEffect](plateglassbackgroundeffect.md) — The plate glass background effect.
