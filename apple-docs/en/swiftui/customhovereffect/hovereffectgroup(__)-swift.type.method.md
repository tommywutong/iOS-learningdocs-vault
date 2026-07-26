---
title: 'hoverEffectGroup(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/customhovereffect/hovereffectgroup(_:)-swift.type.method'
source_url: 'https://developer.apple.com/documentation/swiftui/customhovereffect/hovereffectgroup(_:)-swift.type.method'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/customhovereffect/hovereffectgroup%28_%3A%29-swift.type.method.json'
content_hash: 'sha256:4c8d611c01926382'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CustomHoverEffect](../customhovereffect.md)

# hoverEffectGroup(_:)

<sub>Type Method</sub>

Creates an effect that activates a named group of effects.

<sub>visionOS</sub>

```swift
static func hoverEffectGroup(_ group: HoverEffectGroup?) -> GroupHoverEffect
```

## Parameters

- `group` — The `HoverEffectGroup` to activate when this view is hovered. If `nil`, this modifier has no effect.

## Return Value

An effect that activates the given hover group.
