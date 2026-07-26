---
title: messages
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/message/messages-swift.type.property
source_url: 'https://developer.apple.com/documentation/storekit/message/messages-swift.type.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/message/messages-swift.type.property.json'
content_hash: 'sha256:c0bb0a469462fd95'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Message](../message.md)

# messages

<sub>Type Property</sub>

The asynchronous sequence that sends a message when the App Store creates it.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static var messages: Message.Messages { get }
```

## Discussion

If your app doesn’t implement this message listener, StoreKit retrieves any messages from the App Store each time your app launches, and presents them by default.

For more information about listening for and displaying messages, see [Message](../message.md).

## See Also

### Getting messages and message reasons

- [reason](reason-swift.property.md) — The reason that the App Store sends the message.
- [Messages](messages-swift.struct.md) — An asynchronous sequence of messages from the App Store.
- [Reason](reason-swift.struct.md) — Reasons for the App Store messages.
