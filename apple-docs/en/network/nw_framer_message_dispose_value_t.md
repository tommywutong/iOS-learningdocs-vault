---
title: nw_framer_message_dispose_value_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_framer_message_dispose_value_t
source_url: 'https://developer.apple.com/documentation/network/nw_framer_message_dispose_value_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_framer_message_dispose_value_t.json'
content_hash: 'sha256:207e7350d53e9f1c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_framer_message_dispose_value_t

<sub>Type Alias</sub>

A handler that’s invoked when your custom value needs to be released due to a message being released or the value being replaced.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_framer_message_dispose_value_t = (UnsafeMutableRawPointer) -> Void
```

## See Also

### Customizing Framer Messages

- [nw_framer_message_t](nw_framer_message_t.md) — A message for a custom protocol, in which you can store arbitrary key-value pairs.
- [nw_protocol_metadata_is_framer_message](<nw_protocol_metadata_is_framer_message(__).md>) — Checks if a metadata object represents a custom framer protocol message.
- [nw_framer_protocol_create_message](<nw_framer_protocol_create_message(__).md>) — Initializes an empty message for a custom framer definition.
- [nw_framer_message_create](<nw_framer_message_create(__).md>) — Initializes an empty message from within a framer implementation.
- [nw_framer_message_set_value](<nw_framer_message_set_value(________).md>) — Sets a value to be stored in a framer message, with a completion to call to disposed the stored value when the message is released.
- [nw_framer_message_set_object_value](<nw_framer_message_set_object_value(______).md>) — Sets an NSObject value to be stored in a framer message.
- [nw_framer_message_access_value](<nw_framer_message_access_value(______).md>) — Accesses a custom value stored in a framer message.
- [nw_framer_message_copy_object_value](<nw_framer_message_copy_object_value(____).md>) — Accesses an NSObject value stored in a framer message.
