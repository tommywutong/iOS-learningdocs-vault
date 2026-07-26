---
title: 'nw_framer_copy_parameters(_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_framer_copy_parameters(_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_framer_copy_parameters(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_framer_copy_parameters%28_%3A%29.json'
content_hash: 'sha256:8b369f81c8d5edd7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_framer_copy_parameters(_:)

<sub>Function</sub>

Accesses the parameters of the connection in which your protocol is running.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_framer_copy_parameters(_ framer: nw_framer_t) -> nw_parameters_t
```

## See Also

### Inspecting Instance Properties

- [nw_framer_copy_remote_endpoint](<nw_framer_copy_remote_endpoint(__).md>) — Accesses the remote endpoint of the connection in which your protocol is running.
- [nw_framer_copy_local_endpoint](<nw_framer_copy_local_endpoint(__).md>) — Accesses the local endpoint of the connection in which your protocol is running.
