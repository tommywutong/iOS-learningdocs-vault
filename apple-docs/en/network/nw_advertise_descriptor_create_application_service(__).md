---
title: 'nw_advertise_descriptor_create_application_service(_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_advertise_descriptor_create_application_service(_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_advertise_descriptor_create_application_service(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_advertise_descriptor_create_application_service%28_%3A%29.json'
content_hash: 'sha256:5dbc3ba6281f7f7e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_advertise_descriptor_create_application_service(_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_advertise_descriptor_create_application_service(_ application_service_name: UnsafePointer<CChar>) -> nw_advertise_descriptor_t
```

## See Also

### Functions

- [nw_advertise_descriptor_copy_txt_record_object](<nw_advertise_descriptor_copy_txt_record_object(__).md>) — Accesses the TXT record to advertise with the service.
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
- [nw_browse_result_copy_endpoint](<nw_browse_result_copy_endpoint(__).md>) — The discovered service endpoint.
