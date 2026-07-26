---
title: 'hoverEffectGroup(id:in:behavior:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/customhovereffect/hovereffectgroup(id:in:behavior:)-swift.type.method'
source_url: 'https://developer.apple.com/documentation/swiftui/customhovereffect/hovereffectgroup(id:in:behavior:)-swift.type.method'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/customhovereffect/hovereffectgroup%28id%3Ain%3Abehavior%3A%29-swift.type.method.json'
content_hash: 'sha256:895e7d36784aed8c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CustomHoverEffect](../customhovereffect.md)

# hoverEffectGroup(id:in:behavior:)

<sub>Type Method</sub>

Creates an effect that activates a named group of effects.

<sub>visionOS</sub>

```swift
static func hoverEffectGroup(id: String? = nil, in namespace: Namespace.ID, behavior: HoverEffectGroup.Behavior = .activatesGroup) -> GroupHoverEffect
```

## Parameters

- `id` — An optional id to give the group. If provided, the group will be uniquely identified by combining the id and the namespace.

- `namespace` — The namespace that identifies the group. If `nil`, this modifier has no effect.

- `behavior` — How the effect will behave relative to other effects in the group.

## Return Value

A new effect that activates the given effect group.

## Discussion

The effect group is uniquely identified by combining the `id` and `namespace` parameters. If an `id` is not provided, the effect will be identified by the `namespace` alone. Providing an `id` is useful when creating effects that use multiple, closely-related groups.

The default behavior of an effect is to activate the effect group when hovered. The `behavior` parameter can be used to choose alternative behaviors. See [Behavior](../hovereffectgroup/behavior.md) for all possible behaviors.
