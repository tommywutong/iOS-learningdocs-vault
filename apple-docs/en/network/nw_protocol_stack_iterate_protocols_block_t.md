---
title: nw_protocol_stack_iterate_protocols_block_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_protocol_stack_iterate_protocols_block_t
source_url: 'https://developer.apple.com/documentation/network/nw_protocol_stack_iterate_protocols_block_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_protocol_stack_iterate_protocols_block_t.json'
content_hash: 'sha256:6044a74a72b8d38d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_protocol_stack_iterate_protocols_block_t

<sub>Type Alias</sub>

A block that allows you to inspect or modify a single protocol’s options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_protocol_stack_iterate_protocols_block_t = (nw_protocol_options_t) -> Void
```

## See Also

### Modifying Application Protocols

- [nw_protocol_stack_prepend_application_protocol](<nw_protocol_stack_prepend_application_protocol(____).md>) — Adds a protocol onto the top of the protocol stack.
- [nw_protocol_stack_clear_application_protocols](<nw_protocol_stack_clear_application_protocols(__).md>) — Removes all application protocols from the protocol stack.
- [nw_protocol_stack_iterate_application_protocols](<nw_protocol_stack_iterate_application_protocols(____).md>) — Iterates through the array of application protocol options that will be used by connections and listeners.
