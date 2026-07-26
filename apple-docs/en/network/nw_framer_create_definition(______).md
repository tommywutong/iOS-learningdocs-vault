---
title: 'nw_framer_create_definition(_:_:_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_framer_create_definition(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_framer_create_definition(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_framer_create_definition%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:37a60b106831f2c9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_framer_create_definition(_:_:_:)

<sub>Function</sub>

Initializes a new protocol definition based on your protocol implementation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_framer_create_definition(_ identifier: UnsafePointer<CChar>, _ flags: UInt32, _ start_handler: @escaping nw_framer_start_handler_t) -> nw_protocol_definition_t
```

## Discussion

Each time you initialize a protocol definition with your custom start handler, a new definition is created that will not be considered equal to other definitions. If you need to associate messages with a protocol you have added to a connection’s protocol stack, make sure to use the same definition.

## See Also

### Adding Framers to Connections

- [nw_framer_start_handler_t](nw_framer_start_handler_t.md) — A handler that represents the entry point into your custom protocol.
- [nw_framer_t](nw_framer_t.md) — An object that represents a single instance of your custom protocol running in a connection.
- [nw_framer_start_result_t](nw_framer_start_result_t.md) — Results that you send to indicate the disposition of your protocol after the start handler is invoked.
- [NW_FRAMER_CREATE_FLAGS_DEFAULT](nw_framer_create_flags_default.md) — A constant flag value that indicates that the default framer protocol behavior should be used.
- [nw_framer_create_options](<nw_framer_create_options(__).md>) — Initializes a set of protocol options with a custom framer definition.
