---
title: 'nw_path_is_ultra_constrained(_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_path_is_ultra_constrained(_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_path_is_ultra_constrained(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_path_is_ultra_constrained%28_%3A%29.json'
content_hash: 'sha256:b15e8e64d00c890e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_path_is_ultra_constrained(_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_path_is_ultra_constrained(_ path: nw_path_t) -> Bool
```

## Parameters

- `path` — The path object to check.

## Return Value

Returns true if the path uses any network interface that is considered ultra-constrained, false otherwise.

## Discussion

Checks if the path uses any network interfaces that are considered ultra-constrained.
