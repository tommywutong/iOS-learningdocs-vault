---
title: 'nw_connection_cancel_current_endpoint(_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_connection_cancel_current_endpoint(_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_connection_cancel_current_endpoint(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_connection_cancel_current_endpoint%28_%3A%29.json'
content_hash: 'sha256:6d99c937d8f09157'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_connection_cancel_current_endpoint(_:)

<sub>Function</sub>

Causes the current endpoint to be rejected, allowing the connection to try another resolved address.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_connection_cancel_current_endpoint(_ connection: nw_connection_t)
```

## Discussion

Protocols that do not have handshakes, such as UDP, do not allow connections to validate connectivity on their own. Cancelling an endpoint allows you to indicate that a certain endpoint should be rejected due to a lack of valid response. If other addresses were resolved for the remote endpoint, those will be attempted next.

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
