---
title: 'hoverEffectDisabled(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/customhovereffect/hovereffectdisabled(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/customhovereffect/hovereffectdisabled(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/customhovereffect/hovereffectdisabled%28_%3A%29.json'
content_hash: 'sha256:26b9da1bd96cd43d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CustomHoverEffect](../customhovereffect.md)

# hoverEffectDisabled(_:)

<sub>Instance Method</sub>

Disables this hover effect.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func hoverEffectDisabled(_ isDisabled: Bool = true) -> some CustomHoverEffect

```

## Parameters

- `isDisabled` — A Boolean value that determines whether the hover effect is disabled or not. Specifying `true` takes precedence over `false`. Default: `true`.

## Return Value

A conditionally disabled hover effect.

## Discussion

Use `hoverEffectDisabled(_:)` to prevent a hover effect from becoming active. When an effect is disabled, all contained effects are also disabled and cannot be re-enabled.

In the following example, the scale effect is disabled if the `accessibilityReduceMotion` setting is enabled:

```swift
struct ScaleAndFadeEffect: CustomHoverEffect {
    @Environment(\.accessibilityReduceMotion) var accessibilityReduceMotion
    func body(content: Content) -> some CustomHoverEffect {
        content.hoverEffect { effect, isActive, _ in
            effect.scaleEffect(!isActive ? 0.95 : 1.05)
        }
        .hoverEffectDisabled(accessibilityReduceMotion)
        .hoverEffect { effect, isActive, _ in
            effect.opacity(!isActive ? 0.9 : 1)
        }
    }
}
```

## See Also

### Creating custom hover effects

- [hoverEffect(_:in:isEnabled:)](<hovereffect(__in_isenabled_).md>) — Applies this effect in parallel with the given `effect`.
- [hoverEffect(in:isEnabled:body:)](<hovereffect(in_isenabled_body_)-swift.method.md>) — Applies a hover effect based on the current phase.
- [hoverEffectGroup(_:)](<hovereffectgroup(__)-swift.method.md>) — Activates this effect as part of an effect group.
- [hoverEffectGroup(id:in:behavior:)](<hovereffectgroup(id_in_behavior_)-swift.method.md>) — Activates this effect as part of an effect group.
