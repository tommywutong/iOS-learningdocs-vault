---
title: Locale.CurrentLocaleDidChangeMessage
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/currentlocaledidchangemessage
source_url: 'https://developer.apple.com/documentation/foundation/locale/currentlocaledidchangemessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/currentlocaledidchangemessage.json'
content_hash: 'sha256:b64b427f06fa9928'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# Locale.CurrentLocaleDidChangeMessage

<sub>Structure</sub>

A message the system sends when the current locale changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CurrentLocaleDidChangeMessage
```

## Overview

Register an observer for this message if your app displays content that’s affected by the current locale, such as dates, times, numbers, and so on. Use the message to trigger updates to your app’s interface.

Observe this message with the identifier [currentLocaleDidChange](../notificationcenter/messageidentifier/currentlocaledidchange.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [Subject](../notificationcenter/mainactormessage/subject.md) of this message type is [Locale](../locale.md).

This message interoperates with the notification [NSCurrentLocaleDidChangeNotification](../nslocale/currentlocaledidchangenotification.md). The system notifies observers of the message when the [NotificationCenter](../notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Relationships

- **Conforms To**: [MainActorMessage](../notificationcenter/mainactormessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a message for a change in locale

- [init()](<currentlocaledidchangemessage/init().md>) — Creates a message for the change in current locale.
