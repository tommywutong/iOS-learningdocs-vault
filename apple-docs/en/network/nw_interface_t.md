---
title: nw_interface_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_interface_t
source_url: 'https://developer.apple.com/documentation/network/nw_interface_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_interface_t.json'
content_hash: 'sha256:ba6f491a9e73e77e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_interface_t

<sub>Type Alias</sub>

An interface that a network connection uses to send and receive data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_interface_t = any OS_nw_interface
```

## Topics

### Network Interface Types

- [nw_interface_type_t](nw_interface_type_t.md) — Types of network interfaces, based on their link layer media types.

### Inspecting Interfaces

- [nw_interface_get_type](<nw_interface_get_type(__).md>) — Accesses the type of the interface, such as Wi-Fi or Loopback.
- [nw_interface_get_name](<nw_interface_get_name(__).md>) — Accesses the name of the interface.
- [nw_interface_get_index](<nw_interface_get_index(__).md>) — Accesses the system interface index associated with the interface.
