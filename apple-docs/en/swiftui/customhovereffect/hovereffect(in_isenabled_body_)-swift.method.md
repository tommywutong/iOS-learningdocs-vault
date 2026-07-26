---
title: 'hoverEffect(in:isEnabled:body:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/customhovereffect/hovereffect(in:isenabled:body:)-swift.method'
source_url: 'https://developer.apple.com/documentation/swiftui/customhovereffect/hovereffect(in:isenabled:body:)-swift.method'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/customhovereffect/hovereffect%28in%3Aisenabled%3Abody%3A%29-swift.method.json'
content_hash: 'sha256:47942d681e295e3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CustomHoverEffect](../customhovereffect.md)

# hoverEffect(in:isEnabled:body:)

<sub>Instance Method</sub>

Applies a hover effect based on the current phase.

<sub>visionOS</sub>

```swift
func hoverEffect(in group: HoverEffectGroup? = nil, isEnabled: Bool = true, body: @escaping (EmptyHoverEffectContent, Bool, GeometryProxy) -> some HoverEffectContent) -> some CustomHoverEffect

```

## Parameters

- `group` — An optional [HoverEffectGroup](../hovereffectgroup.md) to add this effect to.

- `isEnabled` — Whether the effect is enabled or not. If `false`, the effect’s inactive state will be applied, and it will not apply the active state when hovered.

- `body` — The closure that constructs a `HoverEffectContent` for each of the effect’s phases.

## Return Value

A new effect that changes a view’s appearance when hovered.

## Discussion

You use this modifier to describe how a view should change when hovered. The given closure is provided an empty effect that you use to compose an effect, as well as a boolean describing which phase is being requested. A [GeometryProxy](../geometryproxy.md) is also provided, allowing effects to change based on the view’s geometry.

In the following example, the effect will apply a scale of 1.0 to a view when inactive, and then scale to 1.1 when active:

```swift
struct ScaleHoverEffect: CustomHoverEffect {
    func body(content: Content) -> some CustomHoverEffect {
        content.hoverEffect { effect, isActive, proxy in
            effect.scaleEffect(!isActive ? 1.0 : 1.1)
        }
    }
}
```

Use the [animation(_:body:)](<../hovereffectcontent/animation(__body_).md>) modifier to specify how visual changes should be animated.

## See Also

### Creating custom hover effects

- [hoverEffect(_:in:isEnabled:)](<hovereffect(__in_isenabled_).md>) — Applies this effect in parallel with the given `effect`.
- [hoverEffectGroup(_:)](<hovereffectgroup(__)-swift.method.md>) — Activates this effect as part of an effect group.
- [hoverEffectGroup(id:in:behavior:)](<hovereffectgroup(id_in_behavior_)-swift.method.md>) — Activates this effect as part of an effect group.
- [hoverEffectDisabled(_:)](<hovereffectdisabled(__).md>) — Disables this hover effect.
