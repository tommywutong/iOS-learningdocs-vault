---
title: 'toggled(trigger:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/hovereffectphaseoverride/toggled(trigger:)'
source_url: 'https://developer.apple.com/documentation/swiftui/hovereffectphaseoverride/toggled(trigger:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/hovereffectphaseoverride/toggled%28trigger%3A%29.json'
content_hash: 'sha256:506356d60aa3193b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HoverEffectPhaseOverride](../hovereffectphaseoverride.md)

# toggled(trigger:)

<sub>Type Method</sub>

Immediately transition to the opposite of an effect’s current phase.

<sub>visionOS</sub>

```swift
static func toggled(trigger: some Equatable) -> HoverEffectPhaseOverride
```

## Parameters

- `trigger` — A value to observe for changes. The override will be reapplied whenever this value changes.

## Discussion

Applying this override causes an effect to transition to the opposite of its current phase at the moment the override is applied. If the effect is `active`, this is equivalent to applying the `inactive` override (and vice versa). Hover effects may be applied outside the app process, so this override allows the current phase to be toggled without needing to know the current phase.

The `toggled` override changes the effect’s phase when first applied, and also whenever the given `Equatable` trigger value changes. This allows the effect’s phase to be toggled repeatedly.

When applied to a group, all effects in the group will be affected (just like the `active` or `inactive` overrides). Applying overrides to multiple effects in the same group is undefined, due to it not being clear which override should be applied.
