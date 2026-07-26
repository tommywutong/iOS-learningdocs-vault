---
title: 'nw_quic_get_initial_max_streams_unidirectional(_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_quic_get_initial_max_streams_unidirectional(_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_quic_get_initial_max_streams_unidirectional(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_quic_get_initial_max_streams_unidirectional%28_%3A%29.json'
content_hash: 'sha256:bccde8e6d7b5b576'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_quic_get_initial_max_streams_unidirectional(_:)

<sub>Function</sub>

Accesses a QUIC connection’s initial maximum number of unidirectional streams.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_quic_get_initial_max_streams_unidirectional(_ options: nw_protocol_options_t) -> UInt64
```

## Parameters

- `options` — A QUIC protocol options instance.

## Return Value

The value of the `initial_max_streams_uni` transport parameter.

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
