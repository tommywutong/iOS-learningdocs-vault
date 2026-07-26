---
title: nw_parameters_iterate_interfaces_block_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_parameters_iterate_interfaces_block_t
source_url: 'https://developer.apple.com/documentation/network/nw_parameters_iterate_interfaces_block_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_parameters_iterate_interfaces_block_t.json'
content_hash: 'sha256:f5d63c2083956af6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_parameters_iterate_interfaces_block_t

<sub>Type Alias</sub>

A block that allows inspection of a list of interfaces.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_parameters_iterate_interfaces_block_t = (nw_interface_t) -> Bool
```

## Return Value

Return true to continue iterating, or false to stop iterating.

## See Also

### Selecting Paths

- [nw_parameters_set_required_interface_type](<nw_parameters_set_required_interface_type(____).md>) — Sets an interface type to require on connections and listeners.
- [nw_parameters_get_required_interface_type](<nw_parameters_get_required_interface_type(__).md>) — Accesses the interface type required on connections and listeners.
- [nw_parameters_require_interface](<nw_parameters_require_interface(____).md>) — Sets a specific interface to require on connections, listeners, and browsers.
- [nw_parameters_copy_required_interface](<nw_parameters_copy_required_interface(__).md>) — Accesses the interface required on connections, listeners, and browsers.
- [nw_parameters_set_local_endpoint](<nw_parameters_set_local_endpoint(____).md>) — Sets a specific local IP address and port to use for connections and listeners.
- [nw_parameters_copy_local_endpoint](<nw_parameters_copy_local_endpoint(__).md>) — Accesses the local IP address and port used for connections and listeners.
- [nw_parameters_set_prohibit_constrained](<nw_parameters_set_prohibit_constrained(____).md>) — Prevents connections, listeners, and browsers from using network paths marked as constrained by Low Data Mode.
- [nw_parameters_get_prohibit_constrained](<nw_parameters_get_prohibit_constrained(__).md>) — Checks if connections, listeners, and browsers are prevented from using network paths marked as constrained by Low Data Mode.
- [nw_parameters_set_prohibit_expensive](<nw_parameters_set_prohibit_expensive(____).md>) — Prevents connections, listeners, and browsers from using network paths marked as expensive.
- [nw_parameters_get_prohibit_expensive](<nw_parameters_get_prohibit_expensive(__).md>) — Checks if connections, listeners, and browsers are prevented from using network paths marked as expensive.
- [nw_parameters_prohibit_interface_type](<nw_parameters_prohibit_interface_type(____).md>) — Prevents connections, listeners, and browsers from using a specific interface type.
- [nw_parameters_clear_prohibited_interface_types](<nw_parameters_clear_prohibited_interface_types(__).md>) — Removes all prohibited interface types.
- [nw_parameters_iterate_prohibited_interface_types](<nw_parameters_iterate_prohibited_interface_types(____).md>) — Examines the list of prohibited interface types.
- [nw_parameters_iterate_interface_types_block_t](nw_parameters_iterate_interface_types_block_t.md) — A block that allows inspection of a list of interface types.
- [nw_parameters_prohibit_interface](<nw_parameters_prohibit_interface(____).md>) — Prevents connections and listeners from using a specific interface.
