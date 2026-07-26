---
title: 'nw_parameters_get_expired_dns_behavior(_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_parameters_get_expired_dns_behavior(_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_parameters_get_expired_dns_behavior(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_parameters_get_expired_dns_behavior%28_%3A%29.json'
content_hash: 'sha256:b079c38160c6659a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_parameters_get_expired_dns_behavior(_:)

<sub>Function</sub>

Checks the behavior for how expired DNS answers should be used.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_parameters_get_expired_dns_behavior(_ parameters: nw_parameters_t) -> nw_parameters_expired_dns_behavior_t
```

## See Also

### Customizing Connection Options

- [nw_parameters_set_multipath_service](<nw_parameters_set_multipath_service(____).md>) — Enables multipath protocols to allow connections to use multiple interfaces.
- [nw_parameters_get_multipath_service](<nw_parameters_get_multipath_service(__).md>) — Checks if multipath is enabled on a connection.
- [nw_multipath_service_t](nw_multipath_service_t.md) — Modes in which a connection can support multipath protocols.
- [nw_parameters_set_service_class](<nw_parameters_set_service_class(____).md>) — Sets a level of service quality to use for connections.
- [nw_parameters_get_service_class](<nw_parameters_get_service_class(__).md>) — Checks the level of service quality used for connections.
- [nw_service_class_t](nw_service_class_t.md) — Levels of service quality that can be used with a connection.
- [nw_parameters_set_fast_open_enabled](<nw_parameters_set_fast_open_enabled(____).md>) — Enables sending application data with protocol handshakes.
- [nw_parameters_get_fast_open_enabled](<nw_parameters_get_fast_open_enabled(__).md>) — Checks if sending application data with protocol handshakes is enabled.
- [nw_parameters_set_expired_dns_behavior](<nw_parameters_set_expired_dns_behavior(____).md>) — Sets the behavior for how expired DNS answers should be used.
- [nw_parameters_expired_dns_behavior_t](nw_parameters_expired_dns_behavior_t.md) — Options for configuring how expired DNS answers should be used.
- [nw_parameters_set_requires_dnssec_validation](<nw_parameters_set_requires_dnssec_validation(____).md>) — Determines whether a connection requires DNSSEC validation when resolving endpoints.
- [nw_parameters_requires_dnssec_validation](<nw_parameters_requires_dnssec_validation(__).md>) — Checks whether a connection requires DNSSEC validation when resolving endpoints.
- [nw_parameters_set_prefer_no_proxy](<nw_parameters_set_prefer_no_proxy(____).md>) — Sets a Boolean that indicates that connections should ignore proxies when they are enabled on the system.
- [nw_parameters_get_prefer_no_proxy](<nw_parameters_get_prefer_no_proxy(__).md>) — Checks if proxies are ignored by default.
- [nw_parameters_set_include_peer_to_peer](<nw_parameters_set_include_peer_to_peer(____).md>) — Enables peer-to-peer link technologies for connections and listeners.
