---
title: Message.Messages
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/message/messages-swift.struct
source_url: 'https://developer.apple.com/documentation/storekit/message/messages-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/message/messages-swift.struct.json'
content_hash: 'sha256:b4c3baeab055b034'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Message](../message.md)

# Message.Messages

<sub>Structure</sub>

An asynchronous sequence of messages from the App Store.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct Messages
```

## Overview

The `Message.Messages` structure provides a sequence of messages that the App Store sends to your app. Iterate over the contents of this structure asynchronously to retrieve each message if your app needs to delay the message.

Don’t create this structure directly. Instead, use [messages](messages-swift.type.property.md) method to retrieve the messages.

## Relationships

- **Conforms To**: [AsyncSequence](../../swift/asyncsequence.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## See Also

### Getting messages and message reasons

- [messages](messages-swift.type.property.md) — The asynchronous sequence that sends a message when the App Store creates it.
- [reason](reason-swift.property.md) — The reason that the App Store sends the message.
- [Reason](reason-swift.struct.md) — Reasons for the App Store messages.
