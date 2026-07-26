---
title: 'toggledTemporarily(trigger:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/hovereffectphaseoverride/toggledtemporarily(trigger:)'
source_url: 'https://developer.apple.com/documentation/swiftui/hovereffectphaseoverride/toggledtemporarily(trigger:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/hovereffectphaseoverride/toggledtemporarily%28trigger%3A%29.json'
content_hash: 'sha256:c8b016c1c1c2a4d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HoverEffectPhaseOverride](../hovereffectphaseoverride.md)

# toggledTemporarily(trigger:)

<sub>Type Method</sub>

Temporaily transitions to the opposite of the effect’s current phase at the moment the override is applied.

<sub>visionOS</sub>

```swift
static func toggledTemporarily(trigger: some Equatable) -> HoverEffectPhaseOverride
```

## Parameters

- `trigger` — A value to observe for changes. The override will be reapplied whenever this value changes.

## Discussion

Use `toggledTemporarily(trigger:)` to toggle an effect’s current phase until it fully transitions to its new phase. The transition will use the animations defined by the effect, but will ignore any delays.

When the override expires, the effect will respond to hover events again. If the view is hovered, the effect will transition to it’s active phase, otherwise its inactive phase.
