---
title: HoverEffectPhaseOverride
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/hovereffectphaseoverride
source_url: 'https://developer.apple.com/documentation/swiftui/hovereffectphaseoverride'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/hovereffectphaseoverride.json'
content_hash: 'sha256:da16cda4cf6b198b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# HoverEffectPhaseOverride

<sub>Structure</sub>

Options for overriding a hover effect’s current phase.

<sub>visionOS</sub>

```swift
struct HoverEffectPhaseOverride
```

## Overview

By default hover effects transition between the active and inactive phases in response to hover events. Use `HoverEffectPhaseOverride` to cause a hover effect to transition between phases based on other criteria.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md)

## Topics

### Type Properties

- [active](hovereffectphaseoverride/active.md) — Immediately transition to the active phase.
- [inactive](hovereffectphaseoverride/inactive.md) — Immediately transition to the inactive phase.

### Type Methods

- [activeTemporarily(trigger:)](<hovereffectphaseoverride/activetemporarily(trigger_).md>) — Temporaily transitions to the active phase until all animations finish, and the transition is complete.
- [inactiveTemporarily(trigger:)](<hovereffectphaseoverride/inactivetemporarily(trigger_).md>) — Temporaily transitions to the inactve phase until all animations finish, and the transition is complete.
- [toggled(trigger:)](<hovereffectphaseoverride/toggled(trigger_).md>) — Immediately transition to the opposite of an effect’s current phase.
- [toggledTemporarily(trigger:)](<hovereffectphaseoverride/toggledtemporarily(trigger_).md>) — Temporaily transitions to the opposite of the effect’s current phase at the moment the override is applied.

## See Also

### Responding to hover events

- [onHover(perform:)](<view/onhover(perform_).md>) — Adds an action to perform when the user moves the pointer over or away from the view’s frame.
- [onContinuousHover(coordinateSpace:perform:)](<view/oncontinuoushover(coordinatespace_perform_).md>) — Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.
- [hoverEffect(_:isEnabled:)](<view/hovereffect(__isenabled_).md>) — Applies a hover effect to this view.
- [hoverEffectDisabled(_:)](<view/hovereffectdisabled(__).md>) — Adds a condition that controls whether this view can display hover effects.
- [defaultHoverEffect(_:)](<view/defaulthovereffect(__).md>) — Sets the default hover effect to use for views within this view.
- [isHoverEffectEnabled](environmentvalues/ishovereffectenabled.md) — A Boolean value that indicates whether the view associated with this environment allows hover effects to be displayed.
- [HoverPhase](hoverphase.md) — The current hovering state and value of the pointer.
- [OrnamentHoverContentEffect](ornamenthovercontenteffect.md) — Presents an ornament on hover using a custom effect.
- [OrnamentHoverEffect](ornamenthovereffect.md) — Presents an ornament on hover.
