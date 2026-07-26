---
title: NSUndoManagerDidCloseUndoGroup
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/nsundomanagerdidcloseundogroup
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsundomanagerdidcloseundogroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/nsundomanagerdidcloseundogroup.json'
content_hash: 'sha256:da1a82b6cdf79a98'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# NSUndoManagerDidCloseUndoGroup

<sub>Type Property</sub>

Posted after an undo manager closes an undo group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let NSUndoManagerDidCloseUndoGroup: NSNotification.Name
```

## Discussion

This notification originates in the implementation of the [- endUndoGrouping](<../../undomanager/endundogrouping().md>) method.

The notification object is the `NSUndoManager` object. This notification doesn’t contain a `userInfo` dictionary.

The system posts this notification on the actor, thread, or dispatch queue that calls [- endUndoGrouping](<../../undomanager/endundogrouping().md>).

## See Also

### Working with notifications

- [NSUndoManagerWillUndoChangeNotification](nsundomanagerwillundochange.md) — Posted just before an undo manager performs an undo operation.
- [NSUndoManagerDidUndoChangeNotification](nsundomanagerdidundochange.md) — Posted just after an undo manager performs an undo operation.
- [NSUndoManagerWillRedoChangeNotification](nsundomanagerwillredochange.md) — Posted just before an undo manager performs a redo operation.
- [NSUndoManagerDidRedoChangeNotification](nsundomanagerdidredochange.md) — Posted just after an undo manager performs a redo operation.
- [NSUndoManagerCheckpointNotification](nsundomanagercheckpoint.md) — Posted whenever an undo manager opens or closes an undo group (except when it opens a top-level group) and when checking the redo stack.
- [NSUndoManagerDidOpenUndoGroupNotification](nsundomanagerdidopenundogroup.md) — Posted whenever an undo manager opens an undo group.
- [NSUndoManagerWillCloseUndoGroupNotification](nsundomanagerwillcloseundogroup.md) — Posted before an undo manager closes an undo group.
- [NSUndoManagerGroupIsDiscardableKey](../../nsundomanagergroupisdiscardablekey.md) — A key, used in a notification’s user info, that indicates the undo group contains only discardable actions.
