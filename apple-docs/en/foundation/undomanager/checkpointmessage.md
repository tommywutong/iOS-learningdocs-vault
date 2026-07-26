---
title: UndoManager.CheckpointMessage
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/undomanager/checkpointmessage
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/checkpointmessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/checkpointmessage.json'
content_hash: 'sha256:92561f696e8a7ab3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# UndoManager.CheckpointMessage

<sub>Structure</sub>

A message that an undo manager sends at certain checkpoints.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CheckpointMessage
```

## Overview

The undo manager posts this message when it opens or closes an undo group (except when it opens a top-level group) and when it checks the redo stack.

Observe this message type with the identifier [checkpoint](../notificationcenter/messageidentifier/checkpoint.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [Subject](../notificationcenter/mainactormessage/subject.md) of this message type is [UndoManager](../undomanager.md).

This message interoperates with the notification [NSUndoManagerCheckpointNotification](../nsnotification/name-swift.struct/nsundomanagercheckpoint.md). The system notifies observers of the message when the [NotificationCenter](../notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Relationships

- **Conforms To**: [MainActorMessage](../notificationcenter/mainactormessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Initializers

- [init()](<checkpointmessage/init().md>) — Creates a undo manager checkpoint message.

## See Also

### Working with notification messages

- [WillUndoChangeMessage](willundochangemessage.md) — A message that an undo manager sends before undoing a change.
- [DidUndoChangeMessage](didundochangemessage.md) — A message that an undo manager sends after undoing a change.
- [WillRedoChangeMessage](willredochangemessage.md) — A message that an undo manager sends before redoing a change.
- [DidRedoChangeMessage](didredochangemessage.md) — A message that an undo manager sends after redoing a change.
- [DidOpenUndoGroupMessage](didopenundogroupmessage.md) — A message that an undo manager sends after opening an undo group.
- [WillCloseUndoGroupMessage](willcloseundogroupmessage.md) — A message that an undo manager sends before closing an undo group.
- [DidCloseUndoGroupMessage](didcloseundogroupmessage.md) — A message that an undo manager sends after closing an undo group.
