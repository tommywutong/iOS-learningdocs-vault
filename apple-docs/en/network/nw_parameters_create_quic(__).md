---
title: 'nw_parameters_create_quic(_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_parameters_create_quic(_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_parameters_create_quic(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_parameters_create_quic%28_%3A%29.json'
content_hash: 'sha256:d14b409a63a52f8c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_parameters_create_quic(_:)

<sub>Function</sub>

Initializes parameters for QUIC connections and listeners.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_parameters_create_quic(_ configure_quic: @escaping nw_parameters_configure_protocol_block_t) -> nw_parameters_t
```

## Parameters

- `configure_quic` — A Swift closure, or an Objective-C block, that receives an [nw_protocol_options_t](nw_protocol_options_t.md) instance. Provide a custom block and call the various `nw_quic_set…` functions on this instance to customize connection and listener parameters. If you want to use default parameters, pass `NW_PARAMETERS_DEFAULT_CONFIGURATION` for this value. This method doesn’t support passing `NW_PARAMETERS_DISABLE_PROTOCOL` to disable the protocol.

## See Also

### Functions

- [nw_advertise_descriptor_copy_txt_record_object](<nw_advertise_descriptor_copy_txt_record_object(__).md>) — Accesses the TXT record to advertise with the service.
- [nw_advertise_descriptor_create_application_service](<nw_advertise_descriptor_create_application_service(__).md>)
- [nw_advertise_descriptor_create_bonjour_service](<nw_advertise_descriptor_create_bonjour_service(______).md>) — Initializes a Bonjour service to advertise.
- [nw_advertise_descriptor_get_application_service_name](<nw_advertise_descriptor_get_application_service_name(__).md>)
- [nw_advertise_descriptor_get_no_auto_rename](<nw_advertise_descriptor_get_no_auto_rename(__).md>) — Checks whether the service prohibits automatic renaming in the event of a name conflict.
- [nw_advertise_descriptor_set_no_auto_rename](<nw_advertise_descriptor_set_no_auto_rename(____).md>) — Sets a Boolean to indicate whether the service prohibits automatic renaming in the event of a name conflict.
- [nw_advertise_descriptor_set_txt_record](<nw_advertise_descriptor_set_txt_record(______).md>) — Sets the TXT record as a raw buffer to advertise with the service.
- [nw_advertise_descriptor_set_txt_record_object](<nw_advertise_descriptor_set_txt_record_object(____).md>) — Sets the TXT record to advertise with the service.
- [nw_browse_descriptor_create_application_service](<nw_browse_descriptor_create_application_service(__).md>)
- [nw_browse_descriptor_create_bonjour_service](<nw_browse_descriptor_create_bonjour_service(____).md>) — Initializes a service descriptor used to discover a Bonjour service.
- [nw_browse_descriptor_get_application_service_name](<nw_browse_descriptor_get_application_service_name(__).md>)
- [nw_browse_descriptor_get_bonjour_service_domain](<nw_browse_descriptor_get_bonjour_service_domain(__).md>) — Accesses the Bonjour service domain set on a browse descriptor.
- [nw_browse_descriptor_get_bonjour_service_type](<nw_browse_descriptor_get_bonjour_service_type(__).md>) — Accesses the Bonjour service type set on a browse descriptor.
- [nw_browse_descriptor_get_include_txt_record](<nw_browse_descriptor_get_include_txt_record(__).md>) — Checks if the browse descriptor requires including associated TXT records with all results.
- [nw_browse_descriptor_set_include_txt_record](<nw_browse_descriptor_set_include_txt_record(____).md>) — Requires including associated TXT records with all results generated for this service descriptor.
