---
title: 'nw_protocol_stack_copy_internet_protocol(_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_protocol_stack_copy_internet_protocol(_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_protocol_stack_copy_internet_protocol(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_protocol_stack_copy_internet_protocol%28_%3A%29.json'
content_hash: 'sha256:06323b59d063ae83'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_protocol_stack_copy_internet_protocol(_:)

<sub>Function</sub>

Accesses the protocol stack’s Internet Protocol options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_protocol_stack_copy_internet_protocol(_ stack: nw_protocol_stack_t) -> nw_protocol_options_t?
```

## See Also

### Configuring Lower Protocols

- [nw_protocol_stack_copy_transport_protocol](<nw_protocol_stack_copy_transport_protocol(__).md>) — Accesses the options for the protocol stack’s transport protocol.
- [nw_protocol_stack_set_transport_protocol](<nw_protocol_stack_set_transport_protocol(____).md>) — Replaces the protocol stack’s transport protocol with a new set of options.
