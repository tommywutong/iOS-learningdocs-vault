---
title: NSExtensionContext.WillResignActiveMessage
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsextensioncontext/willresignactivemessage
source_url: 'https://developer.apple.com/documentation/foundation/nsextensioncontext/willresignactivemessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsextensioncontext/willresignactivemessage.json'
content_hash: 'sha256:d165dcb481e4b489'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExtensionContext](../nsextensioncontext.md)

# NSExtensionContext.WillResignActiveMessage

<sub>Structure</sub>

A message the system sends when the extension’s host app moves from the active to the inactive state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct WillResignActiveMessage
```

## Overview

Your extension can use this message to adjust the extension’s activity when it becomes inactive. For example, you might use this message to save any unsaved data to prevent it from being lost.

Observe this message with the identifier [willResignActive](../notificationcenter/messageidentifier/willresignactive-9z4xc.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [Subject](../notificationcenter/mainactormessage/subject.md) of this message type is [NSExtensionContext](../nsextensioncontext.md).

This message interoperates with the notification [NSExtensionHostWillResignActiveNotification](../nsnotification/name-swift.struct/nsextensionhostwillresignactive.md). The system notifies observers of the message when the [NotificationCenter](../notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Relationships

- **Conforms To**: [MainActorMessage](../notificationcenter/mainactormessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a message for a host app becoming inactive

- [init()](<willresignactivemessage/init().md>) — Creates a message for a host app becoming inactive.

## See Also

### Working with notification messages

- [DidBecomeActiveMessage](didbecomeactivemessage.md) — A message the system sends when the extension’s host app moves from the inactive to the active state.
- [DidEnterBackgroundMessage](didenterbackgroundmessage.md) — A message the system sends when the extension’s host app begins running in the background.
- [WillEnterForegroundMessage](willenterforegroundmessage.md) — A message the system sends when the extension’s host app begins running in the foreground.
