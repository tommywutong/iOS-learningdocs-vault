---
title: NSExtensionContext.WillEnterForegroundMessage
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsextensioncontext/willenterforegroundmessage
source_url: 'https://developer.apple.com/documentation/foundation/nsextensioncontext/willenterforegroundmessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsextensioncontext/willenterforegroundmessage.json'
content_hash: 'sha256:5f6addd7f04f08eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExtensionContext](../nsextensioncontext.md)

# NSExtensionContext.WillEnterForegroundMessage

<sub>Structure</sub>

A message the system sends when the extension’s host app begins running in the foreground.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct WillEnterForegroundMessage
```

## Overview

Your extension can use this message to restart tasks that it stopped when the app moved to the background.

Observe this message with the identifier [willEnterForeground](../notificationcenter/messageidentifier/willenterforeground-p1og.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [Subject](../notificationcenter/mainactormessage/subject.md) of this message type is [NSExtensionContext](../nsextensioncontext.md).

This message interoperates with the notification [NSExtensionHostWillEnterForegroundNotification](../nsnotification/name-swift.struct/nsextensionhostwillenterforeground.md). The system notifies observers of the message when the [NotificationCenter](../notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Relationships

- **Conforms To**: [MainActorMessage](../notificationcenter/mainactormessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a message for a host app entering the foreground

- [init()](<willenterforegroundmessage/init().md>) — Creates a message for a host app entering the foreground.

## See Also

### Working with notification messages

- [DidBecomeActiveMessage](didbecomeactivemessage.md) — A message the system sends when the extension’s host app moves from the inactive to the active state.
- [WillResignActiveMessage](willresignactivemessage.md) — A message the system sends when the extension’s host app moves from the active to the inactive state.
- [DidEnterBackgroundMessage](didenterbackgroundmessage.md) — A message the system sends when the extension’s host app begins running in the background.
