---
title: OrnamentHoverEffect
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/ornamenthovereffect
source_url: 'https://developer.apple.com/documentation/swiftui/ornamenthovereffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/ornamenthovereffect.json'
content_hash: 'sha256:9bcf951b22928ec2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# OrnamentHoverEffect

<sub>Structure</sub>

Presents an ornament on hover.

<sub>visionOS</sub>

```swift
struct OrnamentHoverEffect<OrnamentView> where OrnamentView : View
```

## Overview

You don’t use this directly. Use `CustomHoverEffect.ornament` to create ornament effects instead.

## Relationships

- **Conforms To**: [CustomHoverEffect](customhovereffect.md)

## See Also

### Responding to hover events

- [onHover(perform:)](<view/onhover(perform_).md>) — Adds an action to perform when the user moves the pointer over or away from the view’s frame.
- [onContinuousHover(coordinateSpace:perform:)](<view/oncontinuoushover(coordinatespace_perform_).md>) — Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.
- [hoverEffect(_:isEnabled:)](<view/hovereffect(__isenabled_).md>) — Applies a hover effect to this view.
- [hoverEffectDisabled(_:)](<view/hovereffectdisabled(__).md>) — Adds a condition that controls whether this view can display hover effects.
- [defaultHoverEffect(_:)](<view/defaulthovereffect(__).md>) — Sets the default hover effect to use for views within this view.
- [isHoverEffectEnabled](environmentvalues/ishovereffectenabled.md) — A Boolean value that indicates whether the view associated with this environment allows hover effects to be displayed.
- [HoverPhase](hoverphase.md) — The current hovering state and value of the pointer.
- [HoverEffectPhaseOverride](hovereffectphaseoverride.md) — Options for overriding a hover effect’s current phase.
- [OrnamentHoverContentEffect](ornamenthovercontenteffect.md) — Presents an ornament on hover using a custom effect.
