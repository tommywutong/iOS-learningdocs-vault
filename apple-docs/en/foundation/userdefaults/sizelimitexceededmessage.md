---
title: UserDefaults.SizeLimitExceededMessage
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/userdefaults/sizelimitexceededmessage
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/sizelimitexceededmessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/sizelimitexceededmessage.json'
content_hash: 'sha256:005817e05656cf73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# UserDefaults.SizeLimitExceededMessage

<sub>Structure</sub>

A message the system sends when the size of the data in the defaults database exceeds the maximum.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SizeLimitExceededMessage
```

## Overview

In tvOS, the system posts this message as a warning when the size of your app’s defaults database reaches 512 kilobytes. If your app continues to write to the defaults database, the system terminates your app when the database reaches or exceeds 1 megabyte in size.

The system doesn’t post size exceeded messages for platforms other than tvOS. The system posts this message on your app’s main thread.

Observe this message with the identifier [sizeLimitExceeded](../notificationcenter/messageidentifier/sizelimitexceeded.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [Subject](../notificationcenter/mainactormessage/subject.md) of this message type is [UserDefaults](../userdefaults.md).

This message interoperates with the notification [NSUserDefaultsSizeLimitExceededNotification](sizelimitexceedednotification.md). The system notifies observers of the message when the [NotificationCenter](../notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Relationships

- **Conforms To**: [MainActorMessage](../notificationcenter/mainactormessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a message

- [init()](<sizelimitexceededmessage/init().md>) — Creates a message when the user defaults database of a tvOS app exceeds its maximum size.

## See Also

### Monitoring settings changes and issues

- [DidChangeMessage](didchangemessage.md) — A message the system sends when a user-defaults setting changes.
- [NSUserDefaultsDidChangeNotification](didchangenotification.md) — Posted when the current process changes the value of a setting.
- [NSUserDefaultsSizeLimitExceededNotification](sizelimitexceedednotification.md) — Posted when the amount of data in the defaults database exceeds the allowed maximum.
