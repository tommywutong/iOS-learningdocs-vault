---
title: Process.DidTerminateMessage
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/process/didterminatemessage
source_url: 'https://developer.apple.com/documentation/foundation/process/didterminatemessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/process/didterminatemessage.json'
content_hash: 'sha256:391e19399da4c4e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Process](../process.md)

# Process.DidTerminateMessage

<sub>Structure</sub>

A message the system sends when a task stops operation.

<sub>macOS</sub>

```swift
struct DidTerminateMessage
```

## Overview

Observe this message with the identifier [didTerminate](../notificationcenter/messageidentifier/didterminate.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [Subject](../notificationcenter/mainactormessage/subject.md) of this message type is [Process](../process.md).

This message interoperates with the notification [NSTaskDidTerminateNotification](didterminatenotification.md). The system notifies observers of the message when the [NotificationCenter](../notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Relationships

- **Conforms To**: [AsyncMessage](../notificationcenter/asyncmessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a message

- [init()](<didterminatemessage/init().md>) — Creates a message about a stopped task.
