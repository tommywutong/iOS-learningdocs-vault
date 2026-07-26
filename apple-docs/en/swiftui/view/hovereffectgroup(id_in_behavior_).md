---
title: 'hoverEffectGroup(id:in:behavior:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/hovereffectgroup(id:in:behavior:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/hovereffectgroup(id:in:behavior:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/hovereffectgroup%28id%3Ain%3Abehavior%3A%29.json'
content_hash: 'sha256:54fe764e845a6812'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# hoverEffectGroup(id:in:behavior:)

<sub>Instance Method</sub>

Adds a [HoverEffectGroup](../hovereffectgroup.md) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.

<sub>visionOS</sub>

```swift
nonisolated func hoverEffectGroup(id: String? = nil, in namespace: Namespace.ID, behavior: HoverEffectGroup.Behavior = .activatesGroup) -> some View

```

## Parameters

- `id` — An optional id to give the group. If provided, the group will be uniquely identified by combining the id and the namespace.

- `namespace` — The namespace that identifies the group. If `nil`, this modifier has no effect.

- `behavior` — How the effect will behave relative to other effects in the group.

## Return Value

A new effect that is matched to other effects in the same group.

## Discussion

You use this modifier when all effects defined on a view and its subviews should activate together. In the following example hovering anywhere over the view will activate the `hoverEffect`s added to the `Text` and the background view, as well as any effects added to the group by other views:

```swift
struct EffectView: View {
    @Namespace var namespace

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
        .hoverEffectGroup(in: namespace)
    }
}
```

The effect group is uniquely identified by combining the `id` and `namespace` parameters. If an `id` is not provided, the effect will be identified by the `namespace` alone. Providing a `name` is useful when creating effects that use multiple, related groups.

The default behavior of a matched effect is to activate the effect group when hovered. The `behavior` parameter can be used to choose alternative behaviors. See [Behavior](../hovereffectgroup/behavior.md) for all possible behaviors.

## See Also

### Changing view appearance for hover events

- [hoverEffect(_:)](<hovereffect(__).md>) — Applies a hover effect to this view.
- [HoverEffect](../hovereffect.md) — An effect applied when the pointer hovers over a view.
- [hoverEffect(_:in:isEnabled:)](<hovereffect(__in_isenabled_).md>) — Applies a hover effect to this view, optionally adding it to a [HoverEffectGroup](../hovereffectgroup.md).
- [hoverEffect(in:isEnabled:body:)](<hovereffect(in_isenabled_body_).md>) — Applies a hover effect to this view described by the given closure.
- [CustomHoverEffect](../customhovereffect.md) — A type that represents how a view should change when a pointer hovers over a view, or when someone looks at the view.
- [ContentHoverEffect](../contenthovereffect.md) — A `CustomHoverEffect` that applies effects to a view on hover using a closure.
- [HoverEffectGroup](../hovereffectgroup.md) — Describes a grouping of effects that activate together.
- [hoverEffectGroup()](<hovereffectgroup().md>) — Adds an implicit [HoverEffectGroup](../hovereffectgroup.md) to all effects defined on descendant views, so that all effects added to subviews activate as a group whenever this view or any descendant views are hovered.
- [hoverEffectGroup(_:)](<hovereffectgroup(__).md>) — Adds a [HoverEffectGroup](../hovereffectgroup.md) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [GroupHoverEffect](../grouphovereffect.md) — A `CustomHoverEffect` that activates a named group of effects.
- [HoverEffectContent](../hovereffectcontent.md) — A type that describes the effects of a view for a particular hover effect phase.
- [EmptyHoverEffectContent](../emptyhovereffectcontent.md) — An empty base effect that you use to build other effects.
- [handPointerBehavior(_:)](<handpointerbehavior(__).md>) — Sets the behavior of the hand pointer while the user is interacting with the view.
- [HandPointerBehavior](../handpointerbehavior.md) — A behavior that can be applied to the hand pointer while the user is interacting with a view.
