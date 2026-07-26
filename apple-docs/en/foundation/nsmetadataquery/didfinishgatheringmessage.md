---
title: NSMetadataQuery.DidFinishGatheringMessage
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmetadataquery/didfinishgatheringmessage
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataquery/didfinishgatheringmessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataquery/didfinishgatheringmessage.json'
content_hash: 'sha256:2e16fda45304f22d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMetadataQuery](../nsmetadataquery.md)

# NSMetadataQuery.DidFinishGatheringMessage

<sub>Structure</sub>

A message a metadata query sends when it finishes the initial result-gathering phase of the query.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DidFinishGatheringMessage
```

## Overview

Observe this message with the identifier [didFinishGathering](../notificationcenter/messageidentifier/didfinishgathering.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [Subject](../notificationcenter/mainactormessage/subject.md) of this message type is [NSMetadataQuery](../nsmetadataquery.md).

This message interoperates with the notification [NSMetadataQueryDidFinishGatheringNotification](../nsnotification/name-swift.struct/nsmetadataquerydidfinishgathering.md). The system notifies observers of the message when the [NotificationCenter](../notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Relationships

- **Conforms To**: [AsyncMessage](../notificationcenter/asyncmessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a message

- [init()](<didfinishgatheringmessage/init().md>) — Creates a message for a metadata query that finished its initial result gathering.

## See Also

### Working with notification messages

- [DidStartGatheringMessage](didstartgatheringmessage.md) — A message a metadata query sends when it starts the initial result-gathering phase of the query.
