---
title: nw_path_status_unsatisfied
framework: Network
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_path_status_unsatisfied
source_url: 'https://developer.apple.com/documentation/network/nw_path_status_unsatisfied'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_path_status_unsatisfied.json'
content_hash: 'sha256:eb0182918b3756ba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_path_status_unsatisfied

<sub>Global Variable</sub>

The path is not available for use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nw_path_status_unsatisfied: nw_path_status_t { get }
```

## See Also

### Status Values

- [nw_path_status_invalid](nw_path_status_invalid.md) — The path is not valid.
- [nw_path_status_satisfied](nw_path_status_satisfied.md) — The path is available to establish connections and send data.
- [nw_path_status_satisfiable](nw_path_status_satisfiable.md) — The path is not currently available, but establishing a new connection may activate the path.
