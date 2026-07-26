---
title: nw_protocol_options_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_protocol_options_t
source_url: 'https://developer.apple.com/documentation/network/nw_protocol_options_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_protocol_options_t.json'
content_hash: 'sha256:f37d9db6fbc714d0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_protocol_options_t

<sub>Type Alias</sub>

The abstract superclass for configuring the options of a network protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_protocol_options_t = any OS_nw_protocol_options
```

## Topics

### Inspecting Protocols

- [nw_protocol_options_copy_definition](<nw_protocol_options_copy_definition(__).md>) — Accesses the protocol definition associated with the options object.

## See Also

### Modifying Protocol Stacks

- [nw_parameters_copy_default_protocol_stack](<nw_parameters_copy_default_protocol_stack(__).md>) — Accesses the protocol stack used by connections and listeners.
- [nw_protocol_stack_t](nw_protocol_stack_t.md) — An ordered set of protocol options that define the protocols that connections and listeners use.
- [nw_protocol_definition_t](nw_protocol_definition_t.md) — The abstract superclass for identifying a network protocol.
