---
title: ignoresGroup
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/hovereffectgroup/behavior/ignoresgroup
source_url: 'https://developer.apple.com/documentation/swiftui/hovereffectgroup/behavior/ignoresgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/hovereffectgroup/behavior/ignoresgroup.json'
content_hash: 'sha256:b5ffac4a38ae8447'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [HoverEffectGroup](../../hovereffectgroup.md) · [Behavior](../behavior.md)

# ignoresGroup

<sub>Type Property</sub>

Ignores the current phase of the match group.

<sub>visionOS</sub>

```swift
static let ignoresGroup: HoverEffectGroup.Behavior
```

## Discussion

Use this behavior when an effect should neither activate a group, or become activated by any other effect in the group. The effect will only become active when directly hovered.
