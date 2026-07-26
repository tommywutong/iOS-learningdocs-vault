---
title: 'hoverEffect(_:in:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/customhovereffect/hovereffect(_:in:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/customhovereffect/hovereffect(_:in:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/customhovereffect/hovereffect%28_%3Ain%3Aisenabled%3A%29.json'
content_hash: 'sha256:fb1918dc94dd4b62'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CustomHoverEffect](../customhovereffect.md)

# hoverEffect(_:in:isEnabled:)

<sub>Instance Method</sub>

Applies this effect in parallel with the given `effect`.

<sub>visionOS</sub>

```swift
func hoverEffect(_ effect: some CustomHoverEffect, in group: HoverEffectGroup? = nil, isEnabled: Bool = true) -> some CustomHoverEffect

```

## Parameters

- `effect` — A [CustomHoverEffect](../customhovereffect.md) to combine with this effect.

- `group` — An optional [HoverEffectGroup](../hovereffectgroup.md) to add this effect to.

- `isEnabled` — Whether `effect` is enabled or not.

## Discussion

Use `hoverEffect(_:)` to combine two effects into a single effect that applies both effects in parallel. Modifiers like [hoverEffectDisabled(_:)](<hovereffectdisabled(__).md>) applied to `effect` will not apply to this effect.

For example, in the following effect only the `ScaleUpEffect` is disabled, since modifiers applied to that effect are applied independently.

```swift
struct FadeAndScaleEffect: CustomHoverEffect {
    @Environment(\.accessibilityReduceMotion) var accessibilityReduceMotion
    func body(content: Content) -> some CustomHoverEffect {
        content
            .hoverEffect { effect, isActive, _ in
                effect.opacity(isActive ? 1 : 0.9)
            }
            .hoverEffect(
                ScaleUpEffect().hoverEffectDisabled(accessibilityReduceMotion)
            )
    }
}

struct ScaleUpEffect: CustomHoverEffect {
    func body(content: Content) -> some CustomHoverEffect {
        content.hoverEffect { effect, isActive, _ in
            effect.scaleEffect(isActive ? 1.05 : 1.0)
        }
    }
}
```

- Returns a new effect that applies both effects in parallel.

## See Also

### Creating custom hover effects

- [hoverEffect(in:isEnabled:body:)](<hovereffect(in_isenabled_body_)-swift.method.md>) — Applies a hover effect based on the current phase.
- [hoverEffectGroup(_:)](<hovereffectgroup(__)-swift.method.md>) — Activates this effect as part of an effect group.
- [hoverEffectGroup(id:in:behavior:)](<hovereffectgroup(id_in_behavior_)-swift.method.md>) — Activates this effect as part of an effect group.
- [hoverEffectDisabled(_:)](<hovereffectdisabled(__).md>) — Disables this hover effect.
