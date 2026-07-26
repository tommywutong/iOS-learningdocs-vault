---
title: preservesGroup
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/hovereffectgroup/behavior/preservesgroup
source_url: 'https://developer.apple.com/documentation/swiftui/hovereffectgroup/behavior/preservesgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/hovereffectgroup/behavior/preservesgroup.json'
content_hash: 'sha256:d4faa7d7e9abd919'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [HoverEffectGroup](../../hovereffectgroup.md) · [Behavior](../behavior.md)

# preservesGroup

<sub>Type Property</sub>

Preserves the current phase of the group.

<sub>visionOS</sub>

```swift
static let preservesGroup: HoverEffectGroup.Behavior
```

## Discussion

Use this behavior when an effect should not activate other effects in a group, unless the group already active. This is useful for describing which parts of a view should trigger an effect, while allowing other areas to simply prevent the effect from ending.
