---
title: NW_FRAMER_CREATE_FLAGS_DEFAULT
framework: Network
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_framer_create_flags_default
source_url: 'https://developer.apple.com/documentation/network/nw_framer_create_flags_default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_framer_create_flags_default.json'
content_hash: 'sha256:e640aa9627517fa2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NW_FRAMER_CREATE_FLAGS_DEFAULT

<sub>Global Variable</sub>

A constant flag value that indicates that the default framer protocol behavior should be used.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NW_FRAMER_CREATE_FLAGS_DEFAULT: Int32 { get }
```

## See Also

### Adding Framers to Connections

- [nw_framer_create_definition](<nw_framer_create_definition(______).md>) — Initializes a new protocol definition based on your protocol implementation.
- [nw_framer_start_handler_t](nw_framer_start_handler_t.md) — A handler that represents the entry point into your custom protocol.
- [nw_framer_t](nw_framer_t.md) — An object that represents a single instance of your custom protocol running in a connection.
- [nw_framer_start_result_t](nw_framer_start_result_t.md) — Results that you send to indicate the disposition of your protocol after the start handler is invoked.
- [nw_framer_create_options](<nw_framer_create_options(__).md>) — Initializes a set of protocol options with a custom framer definition.
