---
title: 'hoverEffect(_:in:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/hovereffect(_:in:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/hovereffect(_:in:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/hovereffect%28_%3Ain%3Aisenabled%3A%29.json'
content_hash: 'sha256:73a4173adca3c963'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# hoverEffect(_:in:isEnabled:)

<sub>Instance Method</sub>

Applies a hover effect to this view, optionally adding it to a [HoverEffectGroup](../hovereffectgroup.md).

<sub>visionOS</sub>

```swift
nonisolated func hoverEffect(_ effect: some CustomHoverEffect, in group: HoverEffectGroup?, isEnabled: Bool = true) -> some View

```

## Parameters

- `effect` — The effect to apply to this view.

- `group` — An optional `HoverEffectGroup` the effect should belong to.

- `isEnabled` — Whether this effect is enabled or not.

## Return Value

A new view that applies the hover effect to `self` whenever the view is hovered, or the [HoverEffectGroup](../hovereffectgroup.md) is activated.

## See Also

### Changing view appearance for hover events

- [hoverEffect(_:)](<hovereffect(__).md>) — Applies a hover effect to this view.
- [HoverEffect](../hovereffect.md) — An effect applied when the pointer hovers over a view.
- [hoverEffect(in:isEnabled:body:)](<hovereffect(in_isenabled_body_).md>) — Applies a hover effect to this view described by the given closure.
- [CustomHoverEffect](../customhovereffect.md) — A type that represents how a view should change when a pointer hovers over a view, or when someone looks at the view.
- [ContentHoverEffect](../contenthovereffect.md) — A `CustomHoverEffect` that applies effects to a view on hover using a closure.
- [HoverEffectGroup](../hovereffectgroup.md) — Describes a grouping of effects that activate together.
- [hoverEffectGroup()](<hovereffectgroup().md>) — Adds an implicit [HoverEffectGroup](../hovereffectgroup.md) to all effects defined on descendant views, so that all effects added to subviews activate as a group whenever this view or any descendant views are hovered.
- [hoverEffectGroup(_:)](<hovereffectgroup(__).md>) — Adds a [HoverEffectGroup](../hovereffectgroup.md) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [hoverEffectGroup(id:in:behavior:)](<hovereffectgroup(id_in_behavior_).md>) — Adds a [HoverEffectGroup](../hovereffectgroup.md) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [GroupHoverEffect](../grouphovereffect.md) — A `CustomHoverEffect` that activates a named group of effects.
- [HoverEffectContent](../hovereffectcontent.md) — A type that describes the effects of a view for a particular hover effect phase.
- [EmptyHoverEffectContent](../emptyhovereffectcontent.md) — An empty base effect that you use to build other effects.
- [handPointerBehavior(_:)](<handpointerbehavior(__).md>) — Sets the behavior of the hand pointer while the user is interacting with the view.
- [HandPointerBehavior](../handpointerbehavior.md) — A behavior that can be applied to the hand pointer while the user is interacting with a view.
