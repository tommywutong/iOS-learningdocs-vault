---
title: ContentHoverEffect
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/contenthovereffect
source_url: 'https://developer.apple.com/documentation/swiftui/contenthovereffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/contenthovereffect.json'
content_hash: 'sha256:84f402e0745203bf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ContentHoverEffect

<sub>Structure</sub>

A `CustomHoverEffect` that applies effects to a view on hover using a closure.

<sub>visionOS</sub>

```swift
struct ContentHoverEffect<Effect> where Effect : HoverEffectContent
```

## Overview

Use the [hoverEffect(in:isEnabled:body:)](<customhovereffect/hovereffect(in_isenabled_body_)-swift.type.method.md>) method or the `CustomHoverEffect/hoverEffect(in:isEnabled:body:)` or [hoverEffect(in:isEnabled:body:)](<view/hovereffect(in_isenabled_body_).md>) modifiers to create content effects.

## Relationships

- **Conforms To**: [CustomHoverEffect](customhovereffect.md)

## See Also

### Changing view appearance for hover events

- [hoverEffect(_:)](<view/hovereffect(__).md>) — Applies a hover effect to this view.
- [HoverEffect](hovereffect.md) — An effect applied when the pointer hovers over a view.
- [hoverEffect(_:in:isEnabled:)](<view/hovereffect(__in_isenabled_).md>) — Applies a hover effect to this view, optionally adding it to a [HoverEffectGroup](hovereffectgroup.md).
- [hoverEffect(in:isEnabled:body:)](<view/hovereffect(in_isenabled_body_).md>) — Applies a hover effect to this view described by the given closure.
- [CustomHoverEffect](customhovereffect.md) — A type that represents how a view should change when a pointer hovers over a view, or when someone looks at the view.
- [HoverEffectGroup](hovereffectgroup.md) — Describes a grouping of effects that activate together.
- [hoverEffectGroup()](<view/hovereffectgroup().md>) — Adds an implicit [HoverEffectGroup](hovereffectgroup.md) to all effects defined on descendant views, so that all effects added to subviews activate as a group whenever this view or any descendant views are hovered.
- [hoverEffectGroup(_:)](<view/hovereffectgroup(__).md>) — Adds a [HoverEffectGroup](hovereffectgroup.md) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [hoverEffectGroup(id:in:behavior:)](<view/hovereffectgroup(id_in_behavior_).md>) — Adds a [HoverEffectGroup](hovereffectgroup.md) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [GroupHoverEffect](grouphovereffect.md) — A `CustomHoverEffect` that activates a named group of effects.
- [HoverEffectContent](hovereffectcontent.md) — A type that describes the effects of a view for a particular hover effect phase.
- [EmptyHoverEffectContent](emptyhovereffectcontent.md) — An empty base effect that you use to build other effects.
- [handPointerBehavior(_:)](<view/handpointerbehavior(__).md>) — Sets the behavior of the hand pointer while the user is interacting with the view.
- [HandPointerBehavior](handpointerbehavior.md) — A behavior that can be applied to the hand pointer while the user is interacting with a view.
