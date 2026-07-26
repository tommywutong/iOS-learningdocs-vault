---
title: 'hoverEffectGroup(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/customhovereffect/hovereffectgroup(_:)-swift.method'
source_url: 'https://developer.apple.com/documentation/swiftui/customhovereffect/hovereffectgroup(_:)-swift.method'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/customhovereffect/hovereffectgroup%28_%3A%29-swift.method.json'
content_hash: 'sha256:984bb64928b69278'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CustomHoverEffect](../customhovereffect.md)

# hoverEffectGroup(_:)

<sub>Instance Method</sub>

Activates this effect as part of an effect group.

<sub>visionOS</sub>

```swift
func hoverEffectGroup(_ group: HoverEffectGroup?) -> some CustomHoverEffect

```

## Parameters

- `group` — The `HoverEffectGroup` to activate when this view is hovered. If `nil`, this modifier has no effect.

## Return Value

A new effect that activates with other effects in the same group.

## Discussion

You use this method to compose effects that affect multiple views in concert. In the following example, both views’ effects are in the same group. As a result, hovering over either view will activate all effects in the group, causing both views to become fully opaque:

```swift
struct EffectView: View {
    var effectGroup: HoverEffectGroup?

    var body: some View {
        Color.red
            .frame(width: 100, height: 100)
            .hoverEffect(
                FadeEffect().hoverEffectGroup(effectGroup)
            )
        Color.blue
            .frame(width: 100, height: 100)
            .hoverEffect(
                FadeEffect().hoverEffectGroup(effectGroup)
            )
    }
}

struct FadeEffect: CustomHoverEffect {
    func body(content: Content) -> some CustomHoverEffect {
        content.hoverEffect { effect, isActive, _ in
            effect.opacity(isActive ? 1 : 0.5)
        }
    }
}
```

## See Also

### Creating custom hover effects

- [hoverEffect(_:in:isEnabled:)](<hovereffect(__in_isenabled_).md>) — Applies this effect in parallel with the given `effect`.
- [hoverEffect(in:isEnabled:body:)](<hovereffect(in_isenabled_body_)-swift.method.md>) — Applies a hover effect based on the current phase.
- [hoverEffectGroup(id:in:behavior:)](<hovereffectgroup(id_in_behavior_)-swift.method.md>) — Activates this effect as part of an effect group.
- [hoverEffectDisabled(_:)](<hovereffectdisabled(__).md>) — Disables this hover effect.
