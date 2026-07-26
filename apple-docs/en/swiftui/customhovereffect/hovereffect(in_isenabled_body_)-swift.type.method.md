---
title: 'hoverEffect(in:isEnabled:body:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/customhovereffect/hovereffect(in:isenabled:body:)-swift.type.method'
source_url: 'https://developer.apple.com/documentation/swiftui/customhovereffect/hovereffect(in:isenabled:body:)-swift.type.method'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/customhovereffect/hovereffect%28in%3Aisenabled%3Abody%3A%29-swift.type.method.json'
content_hash: 'sha256:eb636f9e37422d4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CustomHoverEffect](../customhovereffect.md)

# hoverEffect(in:isEnabled:body:)

<sub>Type Method</sub>

Creates a hover effect that applies effects to a view using the given closure.

<sub>visionOS</sub>

```swift
static func hoverEffect<C>(in group: HoverEffectGroup? = nil, isEnabled: Bool = true, body: @escaping (EmptyHoverEffectContent, Bool, GeometryProxy) -> C) -> ContentHoverEffect<C> where Self == ContentHoverEffect<C>, C : HoverEffectContent
```

## Parameters

- `group` — An optional [HoverEffectGroup](../hovereffectgroup.md) to add this effect to.

- `isEnabled` — Whether the effect is enabled or not. If `false`, the effect will not become active when hovered.

- `body` — The closure that constructs a `HoverEffectContent` for each of the effect’s phases.

## Return Value

A new effect that applies effects to a view using the given body closure.

## Discussion

The closure is provided an empty effect that you use to compose effects, as well as a boolean describing which phase is being requested. A [GeometryProxy](../geometryproxy.md) is also provided, allowing effects to change based on the view’s geometry.

Typically the `CustomHoverEffect/hoverEffect(in:isEnabled:body:)` or [hoverEffect(in:isEnabled:body:)](<../view/hovereffect(in_isenabled_body_).md>) modifiers are used to create effects. Use this method when you need to create effects in other contexts.

For example, the following code uses this method and [HoverEffect](../hovereffect.md) to create a type-erased fade effect:

```swift
HoverEffect(
    .hoverEffect { e, isActive, _ in
        e.opacity(isActive ? 1 : 0)
    }
)
```
