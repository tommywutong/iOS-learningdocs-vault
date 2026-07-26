---
title: 'nw_framer_create_options(_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_framer_create_options(_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_framer_create_options(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_framer_create_options%28_%3A%29.json'
content_hash: 'sha256:83866ba2ad73080f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_framer_create_options(_:)

<sub>Function</sub>

Initializes a set of protocol options with a custom framer definition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_framer_create_options(_ framer_definition: nw_protocol_definition_t) -> nw_protocol_options_t
```

## See Also

### Adding Framers to Connections

- [nw_framer_create_definition](<nw_framer_create_definition(______).md>) — Initializes a new protocol definition based on your protocol implementation.
- [nw_framer_start_handler_t](nw_framer_start_handler_t.md) — A handler that represents the entry point into your custom protocol.
- [nw_framer_t](nw_framer_t.md) — An object that represents a single instance of your custom protocol running in a connection.
- [nw_framer_start_result_t](nw_framer_start_result_t.md) — Results that you send to indicate the disposition of your protocol after the start handler is invoked.
- [NW_FRAMER_CREATE_FLAGS_DEFAULT](nw_framer_create_flags_default.md) — A constant flag value that indicates that the default framer protocol behavior should be used.
