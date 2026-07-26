---
title: nw_report_resolution_source_cache
framework: Network
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_report_resolution_source_cache
source_url: 'https://developer.apple.com/documentation/network/nw_report_resolution_source_cache'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_report_resolution_source_cache.json'
content_hash: 'sha256:133737e7205e025a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_report_resolution_source_cache

<sub>Global Variable</sub>

The DNS response was retrieved from a local cache.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nw_report_resolution_source_cache: nw_report_resolution_source_t { get }
```

## See Also

### Resolution Sources

- [nw_report_resolution_source_query](nw_report_resolution_source_query.md) — The DNS response was received from the network.
- [nw_report_resolution_source_expired_cache](nw_report_resolution_source_expired_cache.md) — The DNS response had expired and was retrieved from a local cache.
