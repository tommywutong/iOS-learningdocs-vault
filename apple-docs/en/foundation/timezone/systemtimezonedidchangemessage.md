---
title: TimeZone.SystemTimeZoneDidChangeMessage
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/timezone/systemtimezonedidchangemessage
source_url: 'https://developer.apple.com/documentation/foundation/timezone/systemtimezonedidchangemessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timezone/systemtimezonedidchangemessage.json'
content_hash: 'sha256:e284cc64785ce73d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [TimeZone](../timezone.md)

# TimeZone.SystemTimeZoneDidChangeMessage

<sub>Structure</sub>

A message the system sends when the system time zone changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SystemTimeZoneDidChangeMessage
```

## Overview

Observe this message with the identifier [systemTimeZoneDidChange](../notificationcenter/messageidentifier/systemtimezonedidchange.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [Subject](../notificationcenter/mainactormessage/subject.md) of this message type is [TimeZone](../timezone.md).

This message interoperates with the notification [NSSystemTimeZoneDidChangeNotification](../nsnotification/name-swift.struct/nssystemtimezonedidchange.md). The system notifies observers of the message when the [NotificationCenter](../notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Relationships

- **Conforms To**: [MainActorMessage](../notificationcenter/mainactormessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a message for a system time zone change

- [init(previousTimeZone:)](<systemtimezonedidchangemessage/init(previoustimezone_).md>) — Creates a message for a change in the system time zone.

### Accessing message properties

- [previousTimeZone](systemtimezonedidchangemessage/previoustimezone.md) — The previous system time zone, prior to the change.
