---
title: 'animation(_:body:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/hovereffectcontent/animation(_:body:)'
source_url: 'https://developer.apple.com/documentation/swiftui/hovereffectcontent/animation(_:body:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/hovereffectcontent/animation%28_%3Abody%3A%29.json'
content_hash: 'sha256:02a530c2cdf355dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HoverEffectContent](../hovereffectcontent.md)

# animation(_:body:)

<sub>Instance Method</sub>

Applies the given [Animation](../animation.md) to all effects within the `body` closure.

<sub>visionOS</sub>

```swift
func animation(_ animation: Animation?, body: (EmptyHoverEffectContent) -> some HoverEffectContent) -> some HoverEffectContent

```

## Parameters

- `animation` — The animation to use for the effect transition. If `nil` the effects will not animate.

- `body` — A block used to specify the effects to animate. You must use the provided content to build the effects, or behavior is undefined.

## Return Value

A new effect that combines the effects defined in `body` with

## Discussion

Any effects defined within the `body` closure will be combined with this effect, and the `animation` will used to animate those effects’ changes when the effects are applied.

In the following example, the view will use the `.easeIn` animation when activating the effect, but `.easeOut` when the effect becomes inactive:

```swift
Color.red
    .hoverEffect { effect, isActive, proxy in
        effect.animation(isActive ? .easeIn : .easeOut) {
            $0.opacity(isActive ? 1 : 0.5)
        }
    }
```
