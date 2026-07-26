---
title: 'inactiveTemporarily(trigger:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/hovereffectphaseoverride/inactivetemporarily(trigger:)'
source_url: 'https://developer.apple.com/documentation/swiftui/hovereffectphaseoverride/inactivetemporarily(trigger:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/hovereffectphaseoverride/inactivetemporarily%28trigger%3A%29.json'
content_hash: 'sha256:1da5b7448e370195'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HoverEffectPhaseOverride](../hovereffectphaseoverride.md)

# inactiveTemporarily(trigger:)

<sub>Type Method</sub>

Temporaily transitions to the inactve phase until all animations finish, and the transition is complete.

<sub>visionOS</sub>

```swift
static func inactiveTemporarily(trigger: some Equatable) -> HoverEffectPhaseOverride
```

## Parameters

- `trigger` — A value to observe for changes. The override will be reapplied whenever this value changes.

## Discussion

Use `inactiveTemporarily(trigger:)` to override an effect’s phase until it fully transitions to its inactive phase. The transition will use the animations defined by the effect, but will ignore any delays.

When the override expires, the effect will respond to hover events again. If the view isn’t hovered, the effect will remain in the inactive phase. Otherwise it will begin transitioning to the active phase, honoring any delays defined on the effect.

When applied to a group, all effects in the group become inactive as well. Applying overrides to multiple effects in the same group is undefined, due to it not being clear which override should be applied.
