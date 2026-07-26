---
title: nw_multipath_service_disabled
framework: Network
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_multipath_service_disabled
source_url: 'https://developer.apple.com/documentation/network/nw_multipath_service_disabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_multipath_service_disabled.json'
content_hash: 'sha256:c924e644a8535c08'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_multipath_service_disabled

<sub>Global Variable</sub>

Disable multipath.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nw_multipath_service_disabled: nw_multipath_service_t { get }
```

## See Also

### Multipath service types

- [nw_multipath_service_handover](nw_multipath_service_handover.md) — Enable multipath, but only use other interfaces when the primary interface is lost.
- [nw_multipath_service_interactive](nw_multipath_service_interactive.md) — Enable multipath to use other interfaces when the primary interface encounters loss or delay.
- [nw_multipath_service_aggregate](nw_multipath_service_aggregate.md) — Enable multipath to maximize bandwidth across multiple interfaces.
