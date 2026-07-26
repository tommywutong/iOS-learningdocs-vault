---
title: NSExtensionContext.DidBecomeActiveMessage
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsextensioncontext/didbecomeactivemessage
source_url: 'https://developer.apple.com/documentation/foundation/nsextensioncontext/didbecomeactivemessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsextensioncontext/didbecomeactivemessage.json'
content_hash: 'sha256:db35838d62c2dc18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExtensionContext](../nsextensioncontext.md)

# NSExtensionContext.DidBecomeActiveMessage

<sub>Structure</sub>

A message the system sends when the extension’s host app moves from the inactive to the active state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DidBecomeActiveMessage
```

## Overview

You can use this message to adjust your extension’s activity when the host app becomes active.

Observe this message with the identifier [didBecomeActive](../notificationcenter/messageidentifier/didbecomeactive-79dvm.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [Subject](../notificationcenter/mainactormessage/subject.md) of this message type is [NSExtensionContext](../nsextensioncontext.md).

This message interoperates with the notification [NSExtensionHostDidBecomeActiveNotification](../nsnotification/name-swift.struct/nsextensionhostdidbecomeactive.md). The system notifies observers of the message when the [NotificationCenter](../notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Relationships

- **Conforms To**: [MainActorMessage](../notificationcenter/mainactormessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a message for a host app becoming active

- [init()](<didbecomeactivemessage/init().md>) — Creates a message for a host app becoming active.

## See Also

### Working with notification messages

- [WillResignActiveMessage](willresignactivemessage.md) — A message the system sends when the extension’s host app moves from the active to the inactive state.
- [DidEnterBackgroundMessage](didenterbackgroundmessage.md) — A message the system sends when the extension’s host app begins running in the background.
- [WillEnterForegroundMessage](willenterforegroundmessage.md) — A message the system sends when the extension’s host app begins running in the foreground.
