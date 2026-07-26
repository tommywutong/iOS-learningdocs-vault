---
title: checkpoint
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationcenter/messageidentifier/checkpoint
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/checkpoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/messageidentifier/checkpoint.json'
content_hash: 'sha256:bf2bbbff75b593fe'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NotificationCenter](../../notificationcenter.md) · [MessageIdentifier](../messageidentifier.md)

# checkpoint

<sub>Type Property</sub>

An identifier for a message about an undo manager reaching a checkpoint.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var checkpoint: NotificationCenter.BaseMessageIdentifier<UndoManager.CheckpointMessage> { get }
```

## Discussion

Use this identifier with [NotificationCenter](../../notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [CheckpointMessage](../../undomanager/checkpointmessage.md).

## See Also

### Identifying undo manager messages

- [willUndoChange](willundochange.md) — An identifier for a message about an undo manager preparing to perform an undo.
- [didUndoChange](didundochange.md) — An identifier for a message about an undo manager having performed an undo.
- [willRedoChange](willredochange.md) — An identifier for a message about an undo manager preparing to perform a redo.
- [didRedoChange](didredochange.md) — An identifier for a message about an undo manager having performed a redo.
- [didOpenUndoGroup](didopenundogroup.md) — An identifier for a message about an undo manager having opened an undo group.
- [willCloseUndoGroup](willcloseundogroup.md) — An identifier for a message about an undo manager preparing to close an undo group.
- [didCloseUndoGroup](didcloseundogroup.md) — An identifier for a message about an undo manager having closed an undo group.
