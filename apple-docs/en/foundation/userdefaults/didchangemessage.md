---
title: UserDefaults.DidChangeMessage
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/userdefaults/didchangemessage
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/didchangemessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/didchangemessage.json'
content_hash: 'sha256:ae24197cb398bbef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# UserDefaults.DidChangeMessage

<sub>Structure</sub>

A message the system sends when a user-defaults setting changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DidChangeMessage
```

## Overview

When you write a new value to a setting, or remove an existing value, the system generates this message to alert you that your app’s settings changed. Use this message in other parts of your app to incorporate updated settings. The system posts this notification on the same thread you used to make the change.

If a different process changes your app’s settings, the system doesn’t generate this notification. To detect changes made by another process, register a key-value observer on the [UserDefaults](../userdefaults.md) object. Key-value observing reports all updates to setting values, regardless of which process made the change.

Observe this message with the identifier [didChange](../notificationcenter/messageidentifier/didchange-187tw.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [Subject](../notificationcenter/mainactormessage/subject.md) of this message type is [UserDefaults](../userdefaults.md).

This message interoperates with the notification [NSUserDefaultsDidChangeNotification](didchangenotification.md). The system notifies observers of the message when the [NotificationCenter](../notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Relationships

- **Conforms To**: [AsyncMessage](../notificationcenter/asyncmessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a message

- [init()](<didchangemessage/init().md>) — Creates a message for a settings change to the user defaults.

## See Also

### Monitoring settings changes and issues

- [NSUserDefaultsDidChangeNotification](didchangenotification.md) — Posted when the current process changes the value of a setting.
- [SizeLimitExceededMessage](sizelimitexceededmessage.md) — A message the system sends when the size of the data in the defaults database exceeds the maximum.
- [NSUserDefaultsSizeLimitExceededNotification](sizelimitexceedednotification.md) — Posted when the amount of data in the defaults database exceeds the allowed maximum.
