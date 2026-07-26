---
title: 'nw_parameters_set_allow_ultra_constrained(_:_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_parameters_set_allow_ultra_constrained(_:_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_parameters_set_allow_ultra_constrained(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_parameters_set_allow_ultra_constrained%28_%3A_%3A%29.json'
content_hash: 'sha256:0b73fbd08f74707d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_parameters_set_allow_ultra_constrained(_:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_parameters_set_allow_ultra_constrained(_ parameters: nw_parameters_t, _ allow_ultra_constrained: Bool)
```

## Parameters

- `parameters` — The parameters to modify.

- `allow_ultra_constrained` — Whether or not ultra-constrained interfaces are allowed.

## Discussion

Explicitly allow connectivity over ultra-constrained interfaces. Without this being set, connections are not allowed to use these interfaces.
