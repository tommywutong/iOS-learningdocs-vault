---
title: inactive
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/hovereffectphaseoverride/inactive
source_url: 'https://developer.apple.com/documentation/swiftui/hovereffectphaseoverride/inactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/hovereffectphaseoverride/inactive.json'
content_hash: 'sha256:9094c9e53c58c3c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HoverEffectPhaseOverride](../hovereffectphaseoverride.md)

# inactive

<sub>Type Property</sub>

Immediately transition to the inactive phase.

<sub>visionOS</sub>

```swift
static var inactive: HoverEffectPhaseOverride { get }
```

## Discussion

Applying this override causes an effect to become inactive immediately, regardless of whether the view is hovered or not. The transition will use the animations defined by the effect, but will ignore any delays. The effect remains inactive until this override is removed.

When applied to a group, all effects in the group become inactive as well. Applying overrides to multiple effects in the same group is undefined, due to it not being clear which override should be applied.
