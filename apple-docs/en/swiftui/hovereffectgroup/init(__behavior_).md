---
title: 'init(_:behavior:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/hovereffectgroup/init(_:behavior:)'
source_url: 'https://developer.apple.com/documentation/swiftui/hovereffectgroup/init(_:behavior:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/hovereffectgroup/init%28_%3Abehavior%3A%29.json'
content_hash: 'sha256:fa53549759c5ed6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HoverEffectGroup](../hovereffectgroup.md)

# init(_:behavior:)

<sub>Initializer</sub>

Creates a new [HoverEffectGroup](../hovereffectgroup.md) from a `Namespace.ID`.

<sub>visionOS</sub>

```swift
init(_ namespace: Namespace.ID, behavior: HoverEffectGroup.Behavior = .activatesGroup)
```

## Parameters

- `namespace` — The namespace that identifies the group.

- `behavior` — How the effect will behave relative to other effects in the group.

## Return Value

A new HoverEffectGroup
