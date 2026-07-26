---
title: 'nw_parameters_copy_default_protocol_stack(_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_parameters_copy_default_protocol_stack(_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_parameters_copy_default_protocol_stack(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_parameters_copy_default_protocol_stack%28_%3A%29.json'
content_hash: 'sha256:78108b773ebd5ade'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_parameters_copy_default_protocol_stack(_:)

<sub>Function</sub>

Accesses the protocol stack used by connections and listeners.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_parameters_copy_default_protocol_stack(_ parameters: nw_parameters_t) -> nw_protocol_stack_t
```

## See Also

### Modifying Protocol Stacks

- [nw_protocol_stack_t](nw_protocol_stack_t.md) — An ordered set of protocol options that define the protocols that connections and listeners use.
- [nw_protocol_definition_t](nw_protocol_definition_t.md) — The abstract superclass for identifying a network protocol.
- [nw_protocol_options_t](nw_protocol_options_t.md) — The abstract superclass for configuring the options of a network protocol.
