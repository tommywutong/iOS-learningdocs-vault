---
title: UndoManager.WillCloseUndoGroupMessage
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/undomanager/willcloseundogroupmessage
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/willcloseundogroupmessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/willcloseundogroupmessage.json'
content_hash: 'sha256:5f3c538337390e16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# UndoManager.WillCloseUndoGroupMessage

<sub>Structure</sub>

A message that an undo manager sends before closing an undo group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct WillCloseUndoGroupMessage
```

## Overview

The undo manager posts this message after you call [- endUndoGrouping](<endundogrouping().md>). Because this is a “will”-style message, the undo manager sends the message before it closes the undo group.

Observe this message with the identifier [willCloseUndoGroup](../notificationcenter/messageidentifier/willcloseundogroup.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [Subject](../notificationcenter/mainactormessage/subject.md) of this message type is [UndoManager](../undomanager.md).

This message interoperates with the notification [NSUndoManagerWillCloseUndoGroupNotification](../nsnotification/name-swift.struct/nsundomanagerwillcloseundogroup.md). The system notifies observers of the message when the [NotificationCenter](../notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Relationships

- **Conforms To**: [MainActorMessage](../notificationcenter/mainactormessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Initializers

- [init()](<willcloseundogroupmessage/init().md>) — Creates a will close undo group message.

## See Also

### Working with notification messages

- [WillUndoChangeMessage](willundochangemessage.md) — A message that an undo manager sends before undoing a change.
- [DidUndoChangeMessage](didundochangemessage.md) — A message that an undo manager sends after undoing a change.
- [WillRedoChangeMessage](willredochangemessage.md) — A message that an undo manager sends before redoing a change.
- [DidRedoChangeMessage](didredochangemessage.md) — A message that an undo manager sends after redoing a change.
- [CheckpointMessage](checkpointmessage.md) — A message that an undo manager sends at certain checkpoints.
- [DidOpenUndoGroupMessage](didopenundogroupmessage.md) — A message that an undo manager sends after opening an undo group.
- [DidCloseUndoGroupMessage](didcloseundogroupmessage.md) — A message that an undo manager sends after closing an undo group.
