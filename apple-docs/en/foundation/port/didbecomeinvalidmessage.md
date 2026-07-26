---
title: Port.DidBecomeInvalidMessage
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/port/didbecomeinvalidmessage
source_url: 'https://developer.apple.com/documentation/foundation/port/didbecomeinvalidmessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/port/didbecomeinvalidmessage.json'
content_hash: 'sha256:f3c80d282487392f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Port](../port.md)

# Port.DidBecomeInvalidMessage

<sub>Structure</sub>

A message the system sends when a port becomes invalid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DidBecomeInvalidMessage
```

## Overview

A [SocketPort](../socketport.md) object can’t detect when its connection to a remote port is lost, even if the remote port is on the same machine. Therefore, it can’t invalidate itself and post this message. Instead, your app needs to detect the timeout error when sending the next message.

The [Port](../port.md) object sending this message is no longer useful, so all receivers should unregister themselves for any notifications involving the port. The handler that receives this message should check to see which port became invalid before attempting to do anything. In particular, observers that receive all `DidBecomeInvalidMessage` instances should be aware that the system handles communication with the window server through a `Port`. If this port becomes invalid, drawing operations cause a fatal error.

Observe this message with the identifier [didBecomeInvalid](../notificationcenter/messageidentifier/didbecomeinvalid.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [Subject](../notificationcenter/mainactormessage/subject.md) of this message type is [Port](../port.md).

This message interoperates with the notification [NSPortDidBecomeInvalidNotification](didbecomeinvalidnotification.md). The system notifies observers of the message when the [NotificationCenter](../notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Relationships

- **Conforms To**: [AsyncMessage](../notificationcenter/asyncmessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a message

- [init()](<didbecomeinvalidmessage/init().md>) — Creates a message that indicates a port became invalid.
