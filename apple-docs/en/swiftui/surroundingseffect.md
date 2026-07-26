---
title: SurroundingsEffect
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 26.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/surroundingseffect
source_url: 'https://developer.apple.com/documentation/swiftui/surroundingseffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/surroundingseffect.json'
content_hash: 'sha256:a321c313cb9f0a99'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SurroundingsEffect

<sub>Structure</sub>

Effects that the system can apply to passthrough video.

<sub>macOS, visionOS</sub>

```swift
struct SurroundingsEffect
```

## Overview

Use one of these values with the [preferredSurroundingsEffect(_:)](<view/preferredsurroundingseffect(__).md>) view modifier to indicate what effect to apply to passthrough video when the modified view is displayed.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md)

## Topics

### Getting the effect

- [systemDark](surroundingseffect/systemdark.md) — An effect that dims passthrough video. _(deprecated)_

### Type Properties

- [dark](surroundingseffect/dark.md) — An effect that dims passthrough video.
- [semiDark](surroundingseffect/semidark.md) — An effect that dims passthrough video less than [dark](surroundingseffect/dark.md).
- [ultraDark](surroundingseffect/ultradark.md) — An effect that dims passthrough video more than [dark](surroundingseffect/dark.md)

### Type Methods

- [colorMultiply(_:)](<surroundingseffect/colormultiply(__).md>) — An effect that applies a custom tint to the passthrough video by multiplying the passthrough with a [Color](color.md).
- [dim(intensity:)](<surroundingseffect/dim(intensity_).md>) — An effect that dims the passthrough video a custom amount.

## See Also

### Configuring passthrough

- [preferredSurroundingsEffect(_:)](<view/preferredsurroundingseffect(__).md>) — Applies an effect to passthrough video.
- [breakthroughEffect(_:)](<view/breakthrougheffect(__).md>) — Ensures that the view is always visible to the user, even when other content is occluding it, like 3D models.
- [BreakthroughEffect](breakthrougheffect.md)
