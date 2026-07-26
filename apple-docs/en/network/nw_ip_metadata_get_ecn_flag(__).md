---
title: 'nw_ip_metadata_get_ecn_flag(_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_ip_metadata_get_ecn_flag(_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_ip_metadata_get_ecn_flag(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_ip_metadata_get_ecn_flag%28_%3A%29.json'
content_hash: 'sha256:e3718679a8e9d38f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_ip_metadata_get_ecn_flag(_:)

<sub>Function</sub>

Checks the Explicit Congestion Notification flag value received on an IP packet.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_ip_metadata_get_ecn_flag(_ metadata: nw_protocol_metadata_t) -> nw_ip_ecn_flag_t
```

## See Also

### Handling IP Packets

- [nw_ip_create_metadata](<nw_ip_create_metadata().md>) — Initializes an IP packet configuration with default settings.
- [nw_protocol_metadata_is_ip](<nw_protocol_metadata_is_ip(__).md>) — Checks whether a metadata object represents an IP packet.
- [nw_ip_metadata_set_ecn_flag](<nw_ip_metadata_set_ecn_flag(____).md>) — Sets a specific Explicit Congestion Notification flag value to set on an IP packet.
- [nw_ip_ecn_flag_t](nw_ip_ecn_flag_t.md) — Flag values for Explicit Congestion Notifications in IP packets.
- [nw_ip_metadata_set_service_class](<nw_ip_metadata_set_service_class(____).md>) — Sets a specific service class to mark on an IP packet.
- [nw_ip_metadata_get_service_class](<nw_ip_metadata_get_service_class(__).md>) — Accesses a specific service class to mark on an IP packet.
- [nw_ip_metadata_get_receive_time](<nw_ip_metadata_get_receive_time(__).md>) — Access the time at which a packet was received, in nanoseconds, based on `CLOCK_MONOTONIC_RAW`.
