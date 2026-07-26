---
title: 'nw_framer_message_access_value(_:_:_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_framer_message_access_value(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_framer_message_access_value(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_framer_message_access_value%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:6db0ade2a902a666'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_framer_message_access_value(_:_:_:)

<sub>Function</sub>

Accesses a custom value stored in a framer message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_framer_message_access_value(_ message: nw_framer_message_t, _ key: UnsafePointer<CChar>, _ access_value: (UnsafeRawPointer?) -> Bool) -> Bool
```

## Parameters

- `message` — The message to inspect.

- `key` — The custom key used to store the value.

- `access_value` — A block that will deliver the pointer value stored for the key. The block will be called inline. Returns a value to return to the outer function.

## Return Value

Returns false if the key was not present, or else the boolean returned by the access block.

## See Also

### Customizing Framer Messages

- [nw_framer_message_t](nw_framer_message_t.md) — A message for a custom protocol, in which you can store arbitrary key-value pairs.
- [nw_protocol_metadata_is_framer_message](<nw_protocol_metadata_is_framer_message(__).md>) — Checks if a metadata object represents a custom framer protocol message.
- [nw_framer_protocol_create_message](<nw_framer_protocol_create_message(__).md>) — Initializes an empty message for a custom framer definition.
- [nw_framer_message_create](<nw_framer_message_create(__).md>) — Initializes an empty message from within a framer implementation.
- [nw_framer_message_set_value](<nw_framer_message_set_value(________).md>) — Sets a value to be stored in a framer message, with a completion to call to disposed the stored value when the message is released.
- [nw_framer_message_dispose_value_t](nw_framer_message_dispose_value_t.md) — A handler that’s invoked when your custom value needs to be released due to a message being released or the value being replaced.
- [nw_framer_message_set_object_value](<nw_framer_message_set_object_value(______).md>) — Sets an NSObject value to be stored in a framer message.
- [nw_framer_message_copy_object_value](<nw_framer_message_copy_object_value(____).md>) — Accesses an NSObject value stored in a framer message.
