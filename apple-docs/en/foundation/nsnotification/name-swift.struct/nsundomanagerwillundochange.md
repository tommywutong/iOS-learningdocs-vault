---
title: NSUndoManagerWillUndoChange
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/nsundomanagerwillundochange
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsundomanagerwillundochange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/nsundomanagerwillundochange.json'
content_hash: 'sha256:374d605130157a5e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# NSUndoManagerWillUndoChange

<sub>Type Property</sub>

Posted just before an undo manager performs an undo operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let NSUndoManagerWillUndoChange: NSNotification.Name
```

## Discussion

If you invoke [- undo](<../../undomanager/undo().md>) or [- undoNestedGroup](<../../undomanager/undonestedgroup().md>), this notification is posted. The notification object is the [UndoManager](../../undomanager.md) object. This notification doesn’t contain a `userInfo` dictionary.

The system posts this notification on the actor, thread, or dispatch queue that calls [- undo](<../../undomanager/undo().md>).

## See Also

### Working with notifications

- [NSUndoManagerDidUndoChangeNotification](nsundomanagerdidundochange.md) — Posted just after an undo manager performs an undo operation.
- [NSUndoManagerWillRedoChangeNotification](nsundomanagerwillredochange.md) — Posted just before an undo manager performs a redo operation.
- [NSUndoManagerDidRedoChangeNotification](nsundomanagerdidredochange.md) — Posted just after an undo manager performs a redo operation.
- [NSUndoManagerCheckpointNotification](nsundomanagercheckpoint.md) — Posted whenever an undo manager opens or closes an undo group (except when it opens a top-level group) and when checking the redo stack.
- [NSUndoManagerDidOpenUndoGroupNotification](nsundomanagerdidopenundogroup.md) — Posted whenever an undo manager opens an undo group.
- [NSUndoManagerWillCloseUndoGroupNotification](nsundomanagerwillcloseundogroup.md) — Posted before an undo manager closes an undo group.
- [NSUndoManagerDidCloseUndoGroupNotification](nsundomanagerdidcloseundogroup.md) — Posted after an undo manager closes an undo group.
- [NSUndoManagerGroupIsDiscardableKey](../../nsundomanagergroupisdiscardablekey.md) — A key, used in a notification’s user info, that indicates the undo group contains only discardable actions.
