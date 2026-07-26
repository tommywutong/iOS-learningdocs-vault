---
title: hoverEffectGroup()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view/hovereffectgroup()
source_url: 'https://developer.apple.com/documentation/swiftui/view/hovereffectgroup()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/hovereffectgroup%28%29.json'
content_hash: 'sha256:cbef62b8b079f90d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# hoverEffectGroup()

<sub>Instance Method</sub>

Adds an implicit [HoverEffectGroup](../hovereffectgroup.md) to all effects defined on descendant views, so that all effects added to subviews activate as a group whenever this view or any descendant views are hovered.

<sub>visionOS</sub>

```swift
nonisolated func hoverEffectGroup() -> some View

```

## Return Value

A view that activates the given hover group, as well as all effects added to subviews.

## Discussion

You use this modifier when all effects defined on a view and its subviews should activate together. In the following example hovering anywhere over the view will activate the `hoverEffect`s added to the `Text` and the background view:

```swift
struct EffectView: View {
    var effectGroup: HoverEffectGroup?

    var body: some View {
        HStack {
            Image(systemName: "exclamationmark.triangle.fill")
            Text("12 Issues")
                .hoverEffect { effect, isActive, _ in
                    effect.opacity(isActive ? 1 : 0.5)
                }
        }
        .padding()
        .background {
            Capsule()
                .fill(.yellow)
                .hoverEffect { effect, isActive, _ in
                    effect.opacity(isActive ? 0.25 : 0.1)
                }
        }
        .hoverEffectGroup()
   }
}
```

## See Also

### Changing view appearance for hover events

- [hoverEffect(_:)](<hovereffect(__).md>) — Applies a hover effect to this view.
- [HoverEffect](../hovereffect.md) — An effect applied when the pointer hovers over a view.
- [hoverEffect(_:in:isEnabled:)](<hovereffect(__in_isenabled_).md>) — Applies a hover effect to this view, optionally adding it to a [HoverEffectGroup](../hovereffectgroup.md).
- [hoverEffect(in:isEnabled:body:)](<hovereffect(in_isenabled_body_).md>) — Applies a hover effect to this view described by the given closure.
- [CustomHoverEffect](../customhovereffect.md) — A type that represents how a view should change when a pointer hovers over a view, or when someone looks at the view.
- [ContentHoverEffect](../contenthovereffect.md) — A `CustomHoverEffect` that applies effects to a view on hover using a closure.
- [HoverEffectGroup](../hovereffectgroup.md) — Describes a grouping of effects that activate together.
- [hoverEffectGroup(_:)](<hovereffectgroup(__).md>) — Adds a [HoverEffectGroup](../hovereffectgroup.md) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [hoverEffectGroup(id:in:behavior:)](<hovereffectgroup(id_in_behavior_).md>) — Adds a [HoverEffectGroup](../hovereffectgroup.md) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [GroupHoverEffect](../grouphovereffect.md) — A `CustomHoverEffect` that activates a named group of effects.
- [HoverEffectContent](../hovereffectcontent.md) — A type that describes the effects of a view for a particular hover effect phase.
- [EmptyHoverEffectContent](../emptyhovereffectcontent.md) — An empty base effect that you use to build other effects.
- [handPointerBehavior(_:)](<handpointerbehavior(__).md>) — Sets the behavior of the hand pointer while the user is interacting with the view.
- [HandPointerBehavior](../handpointerbehavior.md) — A behavior that can be applied to the hand pointer while the user is interacting with a view.
