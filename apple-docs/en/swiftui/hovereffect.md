---
title: HoverEffect
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/hovereffect
source_url: 'https://developer.apple.com/documentation/swiftui/hovereffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/hovereffect.json'
content_hash: 'sha256:b87f647dfea2d631'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# HoverEffect

<sub>Structure</sub>

An effect applied when the pointer hovers over a view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct HoverEffect
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomHoverEffect](customhovereffect.md), [Escapable](../swift/escapable.md)

## Topics

### Getting hover effects

- [automatic](hovereffect/automatic.md) — An effect  that attempts to determine the effect automatically. This is the default effect.
- [highlight](hovereffect/highlight.md) — An effect  that morphs the pointer into a platter behind the view and shows a light source indicating position.
- [lift](hovereffect/lift.md) — An effect that slides the pointer under the view and disappears as the view scales up and gains a shadow.

### Initializers

- [init(_:)](<hovereffect/init(__).md>) — Create a `HoverEffect` that contains the specified custom hover effect.

## See Also

### Changing view appearance for hover events

- [hoverEffect(_:)](<view/hovereffect(__).md>) — Applies a hover effect to this view.
- [hoverEffect(_:in:isEnabled:)](<view/hovereffect(__in_isenabled_).md>) — Applies a hover effect to this view, optionally adding it to a [HoverEffectGroup](hovereffectgroup.md).
- [hoverEffect(in:isEnabled:body:)](<view/hovereffect(in_isenabled_body_).md>) — Applies a hover effect to this view described by the given closure.
- [CustomHoverEffect](customhovereffect.md) — A type that represents how a view should change when a pointer hovers over a view, or when someone looks at the view.
- [ContentHoverEffect](contenthovereffect.md) — A `CustomHoverEffect` that applies effects to a view on hover using a closure.
- [HoverEffectGroup](hovereffectgroup.md) — Describes a grouping of effects that activate together.
- [hoverEffectGroup()](<view/hovereffectgroup().md>) — Adds an implicit [HoverEffectGroup](hovereffectgroup.md) to all effects defined on descendant views, so that all effects added to subviews activate as a group whenever this view or any descendant views are hovered.
- [hoverEffectGroup(_:)](<view/hovereffectgroup(__).md>) — Adds a [HoverEffectGroup](hovereffectgroup.md) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [hoverEffectGroup(id:in:behavior:)](<view/hovereffectgroup(id_in_behavior_).md>) — Adds a [HoverEffectGroup](hovereffectgroup.md) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [GroupHoverEffect](grouphovereffect.md) — A `CustomHoverEffect` that activates a named group of effects.
- [HoverEffectContent](hovereffectcontent.md) — A type that describes the effects of a view for a particular hover effect phase.
- [EmptyHoverEffectContent](emptyhovereffectcontent.md) — An empty base effect that you use to build other effects.
- [handPointerBehavior(_:)](<view/handpointerbehavior(__).md>) — Sets the behavior of the hand pointer while the user is interacting with the view.
- [HandPointerBehavior](handpointerbehavior.md) — A behavior that can be applied to the hand pointer while the user is interacting with a view.
