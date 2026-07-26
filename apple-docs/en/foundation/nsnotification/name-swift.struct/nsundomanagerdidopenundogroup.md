---
title: NSUndoManagerDidOpenUndoGroup
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/nsundomanagerdidopenundogroup
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsundomanagerdidopenundogroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/nsundomanagerdidopenundogroup.json'
content_hash: 'sha256:c967515b9c08f5a3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# NSUndoManagerDidOpenUndoGroup

<sub>Type Property</sub>

Posted whenever an undo manager opens an undo group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let NSUndoManagerDidOpenUndoGroup: NSNotification.Name
```

## Discussion

This notification originates in the implementation of the [- beginUndoGrouping](<../../undomanager/beginundogrouping().md>) method.

The notification object is the `NSUndoManager` object. This notification doesn’t contain a `userInfo` dictionary.

The system posts this notification on the actor, thread, or dispatch queue that calls [- beginUndoGrouping](<../../undomanager/beginundogrouping().md>).

## See Also

### Working with notifications

- [NSUndoManagerWillUndoChangeNotification](nsundomanagerwillundochange.md) — Posted just before an undo manager performs an undo operation.
- [NSUndoManagerDidUndoChangeNotification](nsundomanagerdidundochange.md) — Posted just after an undo manager performs an undo operation.
- [NSUndoManagerWillRedoChangeNotification](nsundomanagerwillredochange.md) — Posted just before an undo manager performs a redo operation.
- [NSUndoManagerDidRedoChangeNotification](nsundomanagerdidredochange.md) — Posted just after an undo manager performs a redo operation.
- [NSUndoManagerCheckpointNotification](nsundomanagercheckpoint.md) — Posted whenever an undo manager opens or closes an undo group (except when it opens a top-level group) and when checking the redo stack.
- [NSUndoManagerWillCloseUndoGroupNotification](nsundomanagerwillcloseundogroup.md) — Posted before an undo manager closes an undo group.
- [NSUndoManagerDidCloseUndoGroupNotification](nsundomanagerdidcloseundogroup.md) — Posted after an undo manager closes an undo group.
- [NSUndoManagerGroupIsDiscardableKey](../../nsundomanagergroupisdiscardablekey.md) — A key, used in a notification’s user info, that indicates the undo group contains only discardable actions.
