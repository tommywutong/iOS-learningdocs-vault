---
title: nw_txt_record_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_txt_record_t
source_url: 'https://developer.apple.com/documentation/network/nw_txt_record_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_txt_record_t.json'
content_hash: 'sha256:d48e7adf7ec337af'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_txt_record_t

<sub>Type Alias</sub>

A dictionary representing a TXT record in a DNS packet.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_txt_record_t = any OS_nw_txt_record
```

## Topics

### Creating TXT Records

- [nw_txt_record_create_dictionary](<nw_txt_record_create_dictionary().md>) — Initializes a TXT record as a dictionary of strings.
- [nw_txt_record_create_with_bytes](<nw_txt_record_create_with_bytes(____).md>) — Initializes a TXT record with raw bytes.
- [nw_txt_record_copy](<nw_txt_record_copy(__).md>) — Performs a deep copy of a TXT record.
- [nw_txt_record_set_key](<nw_txt_record_set_key(________).md>) — Sets a data value in a TXT record dictionary.
- [nw_txt_record_remove_key](<nw_txt_record_remove_key(____).md>) — Removes a data value in a TXT record dictionary.

### Examining TXT Records

- [nw_txt_record_is_dictionary](<nw_txt_record_is_dictionary(__).md>) — Checks whether a TXT record conforms to a dictionary format.
- [nw_txt_record_get_key_count](<nw_txt_record_get_key_count(__).md>) — Accesses the number of keys stored in the TXT record dictionary.
- [nw_txt_record_apply](<nw_txt_record_apply(____).md>) — Iterates through all keys in a TXT record dictionary.
- [nw_txt_record_applier_t](nw_txt_record_applier_t.md) — A block that iterates over values and keys in a TXT record dictionary.
- [nw_txt_record_access_key](<nw_txt_record_access_key(______).md>) — Accesses the value for a specific key in a TXT record dictionary.
- [nw_txt_record_access_key_t](nw_txt_record_access_key_t.md) — A block that returns a value in a TXT record dictionary.
- [nw_txt_record_find_key](<nw_txt_record_find_key(____).md>) — Checks the status of value associated with a key in a TXT record dictionary.
- [nw_txt_record_find_key_t](nw_txt_record_find_key_t.md) — Status values describing what kind of value is stored in a TXT record dictionary.
- [nw_txt_record_is_equal](<nw_txt_record_is_equal(____).md>) — Checks whether two TXT records are equivalent.
- [nw_txt_record_access_bytes](<nw_txt_record_access_bytes(____).md>) — Accesses the raw bytes contained within a TXT record.
- [nw_txt_record_access_bytes_t](nw_txt_record_access_bytes_t.md) — A block that provides access to the raw bytes of a TXT record.

## See Also

### Data Types

- [nw_advertise_descriptor_t](nw_advertise_descriptor_t.md) — A description used to advertise the Bonjour service that a listener provides.
- [nw_browse_descriptor_t](nw_browse_descriptor_t.md) — A service description used to discover Bonjour services.
- [nw_browse_result_change_t](nw_browse_result_change_t.md) — Flags describing ways in which discovered services can change between specific results.
- [nw_browse_result_enumerate_interface_t](nw_browse_result_enumerate_interface_t.md) — A handler that enumerates the interfaces associated with a discovered service.
- [nw_browse_result_t](nw_browse_result_t.md) — A discovered service and metadata about the service.
- [nw_browser_browse_results_changed_handler_t](nw_browser_browse_results_changed_handler_t.md) — A handler that delivers updates about discovered services.
- [nw_browser_state_changed_handler_t](nw_browser_state_changed_handler_t.md) — A handler that delivers browser state updates with associated errors.
- [nw_browser_t](nw_browser_t.md) — An object you use to browse for available network services.
- [nw_connection_boolean_event_handler_t](nw_connection_boolean_event_handler_t.md) — A handler that receives Boolean state updates from a connection, such as viability and better path state.
- [nw_connection_group_new_connection_handler_t](nw_connection_group_new_connection_handler_t.md)
- [nw_connection_group_receive_handler_t](nw_connection_group_receive_handler_t.md) — A handler that receives inbound messages from members of the group.
- [nw_connection_group_send_completion_t](nw_connection_group_send_completion_t.md) — A completion to notify you when data has been processed and sent.
- [nw_connection_group_state_changed_handler_t](nw_connection_group_state_changed_handler_t.md) — A handler that receives connection group state updates.
- [nw_connection_group_t](nw_connection_group_t.md) — An object you use to communicate with a group of endpoints, such as an IP multicast group on a local network.
- [nw_connection_path_event_handler_t](nw_connection_path_event_handler_t.md) — A handler that delivers network path updates.
