---
title: GlassBackgroundDisplayMode
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/glassbackgrounddisplaymode
source_url: 'https://developer.apple.com/documentation/swiftui/glassbackgrounddisplaymode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/glassbackgrounddisplaymode.json'
content_hash: 'sha256:c06371e2218e2b3b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# GlassBackgroundDisplayMode

<sub>Enumeration</sub>

The display mode of a glass background.

<sub>visionOS</sub>

```swift
enum GlassBackgroundDisplayMode
```

## Overview

Use a value of this type to indicate when to display a glass background that you add to a view using a view modifier like [glassBackgroundEffect(displayMode:)](<view/glassbackgroundeffect(displaymode_).md>).

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the mode

- [GlassBackgroundDisplayMode.always](glassbackgrounddisplaymode/always.md) — Always display the glass material.
- [GlassBackgroundDisplayMode.implicit](glassbackgrounddisplaymode/implicit.md) — Display the glass material only when the view isn’t already contained in glass.
- [GlassBackgroundDisplayMode.never](glassbackgrounddisplaymode/never.md) — Never display the glass material.

## See Also

### Adding a glass background on views in visionOS

- [glassBackgroundEffect(displayMode:)](<view/glassbackgroundeffect(displaymode_).md>) — Fills the view’s background with an automatic glass background effect and container-relative rounded rectangle shape.
- [glassBackgroundEffect(in:displayMode:)](<view/glassbackgroundeffect(in_displaymode_).md>) — Fills the view’s background with an automatic glass background effect and a shape that you specify.
- [GlassBackgroundEffect](glassbackgroundeffect.md) — A specification for the appearance of a glass background.
- [AutomaticGlassBackgroundEffect](automaticglassbackgroundeffect.md) — The automatic glass background effect.
- [GlassBackgroundEffectConfiguration](glassbackgroundeffectconfiguration.md) — A configuration used to build a custom effect.
- [FeatheredGlassBackgroundEffect](featheredglassbackgroundeffect.md) — The feathered glass background effect.
- [PlateGlassBackgroundEffect](plateglassbackgroundeffect.md) — The plate glass background effect.
