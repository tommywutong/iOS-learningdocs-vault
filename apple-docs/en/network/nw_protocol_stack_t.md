---
title: nw_protocol_stack_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_protocol_stack_t
source_url: 'https://developer.apple.com/documentation/network/nw_protocol_stack_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_protocol_stack_t.json'
content_hash: 'sha256:7ebf67ae27452e31'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_protocol_stack_t

<sub>Type Alias</sub>

An ordered set of protocol options that define the protocols that connections and listeners use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_protocol_stack_t = any OS_nw_protocol_stack
```

## Topics

### Modifying Application Protocols

- [nw_protocol_stack_prepend_application_protocol](<nw_protocol_stack_prepend_application_protocol(____).md>) — Adds a protocol onto the top of the protocol stack.
- [nw_protocol_stack_clear_application_protocols](<nw_protocol_stack_clear_application_protocols(__).md>) — Removes all application protocols from the protocol stack.
- [nw_protocol_stack_iterate_application_protocols](<nw_protocol_stack_iterate_application_protocols(____).md>) — Iterates through the array of application protocol options that will be used by connections and listeners.
- [nw_protocol_stack_iterate_protocols_block_t](nw_protocol_stack_iterate_protocols_block_t.md) — A block that allows you to inspect or modify a single protocol’s options.

### Configuring Lower Protocols

- [nw_protocol_stack_copy_transport_protocol](<nw_protocol_stack_copy_transport_protocol(__).md>) — Accesses the options for the protocol stack’s transport protocol.
- [nw_protocol_stack_set_transport_protocol](<nw_protocol_stack_set_transport_protocol(____).md>) — Replaces the protocol stack’s transport protocol with a new set of options.
- [nw_protocol_stack_copy_internet_protocol](<nw_protocol_stack_copy_internet_protocol(__).md>) — Accesses the protocol stack’s Internet Protocol options.

## See Also

### Modifying Protocol Stacks

- [nw_parameters_copy_default_protocol_stack](<nw_parameters_copy_default_protocol_stack(__).md>) — Accesses the protocol stack used by connections and listeners.
- [nw_protocol_definition_t](nw_protocol_definition_t.md) — The abstract superclass for identifying a network protocol.
- [nw_protocol_options_t](nw_protocol_options_t.md) — The abstract superclass for configuring the options of a network protocol.
