---
title: 'init(id:in:behavior:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/hovereffectgroup/init(id:in:behavior:)'
source_url: 'https://developer.apple.com/documentation/swiftui/hovereffectgroup/init(id:in:behavior:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/hovereffectgroup/init%28id%3Ain%3Abehavior%3A%29.json'
content_hash: 'sha256:97e268ea88e880ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HoverEffectGroup](../hovereffectgroup.md)

# init(id:in:behavior:)

<sub>Initializer</sub>

Creates a new [HoverEffectGroup](../hovereffectgroup.md).

<sub>visionOS</sub>

```swift
init(id: String?, in namespace: Namespace.ID, behavior: HoverEffectGroup.Behavior = .activatesGroup)
```

## Parameters

- `id` — An optional id to give the group. If provided, the group will be uniquely identified by combining the id and the namespace.

- `namespace` — The namespace that identifies the group.

- `behavior` — How the effect will behave relative to other effects in the group.

## Return Value

A new HoverEffectGroup
