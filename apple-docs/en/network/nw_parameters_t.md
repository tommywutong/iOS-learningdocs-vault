---
title: nw_parameters_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_parameters_t
source_url: 'https://developer.apple.com/documentation/network/nw_parameters_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_parameters_t.json'
content_hash: 'sha256:eb0f1af686693009'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_parameters_t

<sub>Type Alias</sub>

An object that stores the protocols to use for connections, options for sending data, and network path constraints.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_parameters_t = any OS_nw_parameters
```

## Topics

### Creating Parameters

- [nw_parameters_create_secure_tcp](<nw_parameters_create_secure_tcp(____).md>) — Initializes parameters for TLS or TCP connections and listeners.
- [nw_parameters_create_secure_udp](<nw_parameters_create_secure_udp(____).md>) — Initializes parameters for DTLS or UDP connections and listeners.
- [nw_parameters_create_quic](<nw_parameters_create_quic(__).md>) — Initializes parameters for QUIC connections and listeners.
- [nw_parameters_configure_protocol_block_t](nw_parameters_configure_protocol_block_t.md) — A block to configure protocol options during the creation of a parameters object.
- [nw_parameters_create](<nw_parameters_create().md>) — Initializes parameters for connections, listeners, and browsers with no protocols specified.
- [nw_parameters_create_custom_ip](<nw_parameters_create_custom_ip(____).md>) — Initializes parameters for connections and listeners using a custom IP protocol.
- [nw_parameters_copy](<nw_parameters_copy(__).md>) — Peforms a deep copy of a parameters object.

### Modifying Protocol Stacks

- [nw_parameters_copy_default_protocol_stack](<nw_parameters_copy_default_protocol_stack(__).md>) — Accesses the protocol stack used by connections and listeners.
- [nw_protocol_stack_t](nw_protocol_stack_t.md) — An ordered set of protocol options that define the protocols that connections and listeners use.
- [nw_protocol_definition_t](nw_protocol_definition_t.md) — The abstract superclass for identifying a network protocol.
- [nw_protocol_options_t](nw_protocol_options_t.md) — The abstract superclass for configuring the options of a network protocol.

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
- [nw_parameters_clear_prohibited_interfaces](<nw_parameters_clear_prohibited_interfaces(__).md>) — Removes all prohibited interface types.
- [nw_parameters_iterate_prohibited_interfaces](<nw_parameters_iterate_prohibited_interfaces(____).md>) — Examines the list of prohibited interfaces.
- [nw_parameters_iterate_interfaces_block_t](nw_parameters_iterate_interfaces_block_t.md) — A block that allows inspection of a list of interfaces.

### Customizing Connection Options

- [nw_parameters_set_multipath_service](<nw_parameters_set_multipath_service(____).md>) — Enables multipath protocols to allow connections to use multiple interfaces.
- [nw_parameters_get_multipath_service](<nw_parameters_get_multipath_service(__).md>) — Checks if multipath is enabled on a connection.
- [nw_multipath_service_t](nw_multipath_service_t.md) — Modes in which a connection can support multipath protocols.
- [nw_parameters_set_service_class](<nw_parameters_set_service_class(____).md>) — Sets a level of service quality to use for connections.
- [nw_parameters_get_service_class](<nw_parameters_get_service_class(__).md>) — Checks the level of service quality used for connections.
- [nw_service_class_t](nw_service_class_t.md) — Levels of service quality that can be used with a connection.
- [nw_parameters_set_fast_open_enabled](<nw_parameters_set_fast_open_enabled(____).md>) — Enables sending application data with protocol handshakes.
- [nw_parameters_get_fast_open_enabled](<nw_parameters_get_fast_open_enabled(__).md>) — Checks if sending application data with protocol handshakes is enabled.
- [nw_parameters_set_expired_dns_behavior](<nw_parameters_set_expired_dns_behavior(____).md>) — Sets the behavior for how expired DNS answers should be used.
- [nw_parameters_get_expired_dns_behavior](<nw_parameters_get_expired_dns_behavior(__).md>) — Checks the behavior for how expired DNS answers should be used.
- [nw_parameters_expired_dns_behavior_t](nw_parameters_expired_dns_behavior_t.md) — Options for configuring how expired DNS answers should be used.
- [nw_parameters_set_requires_dnssec_validation](<nw_parameters_set_requires_dnssec_validation(____).md>) — Determines whether a connection requires DNSSEC validation when resolving endpoints.
- [nw_parameters_requires_dnssec_validation](<nw_parameters_requires_dnssec_validation(__).md>) — Checks whether a connection requires DNSSEC validation when resolving endpoints.
- [nw_parameters_set_prefer_no_proxy](<nw_parameters_set_prefer_no_proxy(____).md>) — Sets a Boolean that indicates that connections should ignore proxies when they are enabled on the system.
- [nw_parameters_get_prefer_no_proxy](<nw_parameters_get_prefer_no_proxy(__).md>) — Checks if proxies are ignored by default.
- [nw_parameters_set_include_peer_to_peer](<nw_parameters_set_include_peer_to_peer(____).md>) — Enables peer-to-peer link technologies for connections and listeners.
- [nw_parameters_get_include_peer_to_peer](<nw_parameters_get_include_peer_to_peer(__).md>) — Checks whether a connection is allowed to use peer-to-peer link technologies.
- [nw_parameters_set_reuse_local_address](<nw_parameters_set_reuse_local_address(____).md>) — Allows reusing local addresses and ports across connections.
- [nw_parameters_get_reuse_local_address](<nw_parameters_get_reuse_local_address(__).md>) — Checks whether a connection allows reusing local addresses and ports.
- [nw_parameters_set_local_only](<nw_parameters_set_local_only(____).md>) — Restricts listeners to only accepting connections from the local link.
- [nw_parameters_get_local_only](<nw_parameters_get_local_only(__).md>) — Checks if a listener is restricted to accepting connections from the local link.

### Configuring Privacy Settings

- [nw_parameters_set_privacy_context](<nw_parameters_set_privacy_context(____).md>) — Associates a privacy context with any connections or listeners that use the parameters.
- [nw_privacy_context_t](nw_privacy_context_t.md) — An object that defines the privacy requirements for a set of connections.
