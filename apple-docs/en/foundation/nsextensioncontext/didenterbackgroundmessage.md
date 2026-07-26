---
title: NSExtensionContext.DidEnterBackgroundMessage
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsextensioncontext/didenterbackgroundmessage
source_url: 'https://developer.apple.com/documentation/foundation/nsextensioncontext/didenterbackgroundmessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsextensioncontext/didenterbackgroundmessage.json'
content_hash: 'sha256:c275cfade5051047'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExtensionContext](../nsextensioncontext.md)

# NSExtensionContext.DidEnterBackgroundMessage

<sub>Structure</sub>

A message the system sends when the extension’s host app begins running in the background.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DidEnterBackgroundMessage
```

## Overview

You can use this message in your extension to stop tasks and prepare for the system to suspend the extension.

Extensions receive only a short amount of time to perform any background work. If you need more time to complete critical tasks, use the methods of the [ProcessInfo](../processinfo.md) class to request that time.

Observe this message with the identifier [didEnterBackground](../notificationcenter/messageidentifier/didenterbackground-5gdtk.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [Subject](../notificationcenter/mainactormessage/subject.md) of this message type is [NSExtensionContext](../nsextensioncontext.md).

This message interoperates with the notification [NSExtensionHostDidEnterBackgroundNotification](../nsnotification/name-swift.struct/nsextensionhostdidenterbackground.md). The system notifies observers of the message when the [NotificationCenter](../notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Relationships

- **Conforms To**: [MainActorMessage](../notificationcenter/mainactormessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a message for a host app entering the background

- [init()](<didenterbackgroundmessage/init().md>) — Creates a message for a host app entering the background.

## See Also

### Working with notification messages

- [DidBecomeActiveMessage](didbecomeactivemessage.md) — A message the system sends when the extension’s host app moves from the inactive to the active state.
- [WillResignActiveMessage](willresignactivemessage.md) — A message the system sends when the extension’s host app moves from the active to the inactive state.
- [WillEnterForegroundMessage](willenterforegroundmessage.md) — A message the system sends when the extension’s host app begins running in the foreground.
