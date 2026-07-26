---
title: nw_error_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_error_t
source_url: 'https://developer.apple.com/documentation/network/nw_error_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_error_t.json'
content_hash: 'sha256:23fe3a34931576a9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_error_t

<sub>Type Alias</sub>

The errors returned by the Network framework.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_error_t = any OS_nw_error
```

## Topics

### Inspecting Errors

- [nw_error_get_error_domain](<nw_error_get_error_domain(__).md>) — Accesses the domain of the network error.
- [nw_error_domain_t](nw_error_domain_t.md) — The error domain for errors used by the Network framework.
- [nw_error_get_error_code](<nw_error_get_error_code(__).md>) — Accesses the specific code of the network error.
- [nw_error_copy_cf_error](<nw_error_copy_cf_error(__).md>) — Returns a copy of a network error.
