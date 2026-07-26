---
title: Date.SystemClockDidChangeMessage
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/systemclockdidchangemessage
source_url: 'https://developer.apple.com/documentation/foundation/date/systemclockdidchangemessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/systemclockdidchangemessage.json'
content_hash: 'sha256:526b73bd6a18fb83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Date](../date.md)

# Date.SystemClockDidChangeMessage

<sub>Structure</sub>

A message the system sends when the system clock changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SystemClockDidChangeMessage
```

## Overview

Various events can initiate this message, such as a call to `settimeofday(_:_:)`, or if the person using the device changes values in Settings.

Observe this message with the identifier [systemClockDidChange](../notificationcenter/messageidentifier/systemclockdidchange.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [Subject](../notificationcenter/mainactormessage/subject.md) of this message type is [Date](../date.md).

This message interoperates with the notification [NSSystemClockDidChangeNotification](../nsnotification/name-swift.struct/nssystemclockdidchange.md). The system notifies observers of the message when the [NotificationCenter](../notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Relationships

- **Conforms To**: [MainActorMessage](../notificationcenter/mainactormessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a message for a system clock change

- [init()](<systemclockdidchangemessage/init().md>) — Creates a message for a change in the system clock.
