---
title: nw_framer_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_framer_t
source_url: 'https://developer.apple.com/documentation/network/nw_framer_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_framer_t.json'
content_hash: 'sha256:a93070362835d028'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_framer_t

<sub>Type Alias</sub>

An object that represents a single instance of your custom protocol running in a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_framer_t = any OS_nw_framer
```

## Discussion

All interaction between your protocol and the connection occurs through this object.

## See Also

### Adding Framers to Connections

- [nw_framer_create_definition](<nw_framer_create_definition(______).md>) — Initializes a new protocol definition based on your protocol implementation.
- [nw_framer_start_handler_t](nw_framer_start_handler_t.md) — A handler that represents the entry point into your custom protocol.
- [nw_framer_start_result_t](nw_framer_start_result_t.md) — Results that you send to indicate the disposition of your protocol after the start handler is invoked.
- [NW_FRAMER_CREATE_FLAGS_DEFAULT](nw_framer_create_flags_default.md) — A constant flag value that indicates that the default framer protocol behavior should be used.
- [nw_framer_create_options](<nw_framer_create_options(__).md>) — Initializes a set of protocol options with a custom framer definition.
