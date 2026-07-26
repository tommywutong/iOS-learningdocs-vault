---
title: 'init(send:receive:components:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/portmessage/init(send:receive:components:)'
source_url: 'https://developer.apple.com/documentation/foundation/portmessage/init(send:receive:components:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/portmessage/init%28send%3Areceive%3Acomponents%3A%29.json'
content_hash: 'sha256:ca59cb6a842718c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PortMessage](../portmessage.md)

# init(send:receive:components:)

<sub>Initializer</sub>

Initializes a newly allocated `NSPortMessage` object to send given data on a given port and to receiver replies on another given port.

<sub>Mac Catalyst, macOS</sub>

```swift
init(send sendPort: Port?, receive replyPort: Port?, components: [Any]?)
```

## Parameters

- `sendPort` — The port on which the message is sent.

- `replyPort` — The port on which replies to the message arrive.

- `components` — The data to send in the message. `components` should contain only `NSData` and `NSPort` objects, and the contents of the `NSData` objects should be in network byte order.

## Return Value

An `NSPortMessage` object initialized to send `components` on `sendPort` and to receiver replies on `receivePort`.

## Discussion

An `NSPortMessage` object initialized with this method has a message identifier of 0.

This is the designated initializer for `NSPortMessage`.

## See Also

### Related Documentation

- [msgid](msgid.md) — Returns the identifier for the receiver.
- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)
