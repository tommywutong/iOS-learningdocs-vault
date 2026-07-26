---
title: active
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/hovereffectphaseoverride/active
source_url: 'https://developer.apple.com/documentation/swiftui/hovereffectphaseoverride/active'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/hovereffectphaseoverride/active.json'
content_hash: 'sha256:6268c6dc470964b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HoverEffectPhaseOverride](../hovereffectphaseoverride.md)

# active

<sub>Type Property</sub>

Immediately transition to the active phase.

<sub>visionOS</sub>

```swift
static var active: HoverEffectPhaseOverride { get }
```

## Discussion

Applying this override causes a hover effect to become active immediately, regardless of whether the view is hovered or not. The transition will use the animations defined by the effect, but will ignore any delays. The effect remains active until this override is removed.

When applied to a group, all effects in the group become active as well. Applying overrides to multiple effects in the same group is undefined, due to it not being clear which override should be applied.
