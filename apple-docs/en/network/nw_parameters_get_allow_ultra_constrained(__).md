---
title: 'nw_parameters_get_allow_ultra_constrained(_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_parameters_get_allow_ultra_constrained(_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_parameters_get_allow_ultra_constrained(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_parameters_get_allow_ultra_constrained%28_%3A%29.json'
content_hash: 'sha256:02d9745d5387a121'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_parameters_get_allow_ultra_constrained(_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_parameters_get_allow_ultra_constrained(_ parameters: nw_parameters_t) -> Bool
```

## Parameters

- `parameters` — The parameters to check.

## Return Value

Returns whether or not ultra-constrained interfaces are allowed.

## Discussion

Check if the parameters explicitly allow connectivity over ultra-constrained interfaces.
