---
title: 'nw_connection_receive(_:_:_:_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_connection_receive(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_connection_receive(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_connection_receive%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:7c8b33d61478b130'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_connection_receive(_:_:_:_:)

<sub>Function</sub>

Schedules a single receive completion handler, with a range indicating how many bytes the handler can receive at one time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_connection_receive(_ connection: nw_connection_t, _ minimum_incomplete_length: UInt32, _ maximum_length: UInt32, _ completion: @escaping nw_connection_receive_completion_t)
```

## Parameters

- `connection` — A network connection instance.

- `minimum_incomplete_length` — The minimum length to receive from the connection, until the content is complete.

- `maximum_length` — The maximum length to receive from the connection in a single completion.

- `completion` — A receive completion is invoked exactly once for a call to receive. The completion indicates that the requested content has been received (in which case the content is delivered), or else an error has occurred. The completion delivers the received content, which may be nil if the message is complete or an error occurred, the message context, a flag indicating if the message is complete, and any associated error.

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
