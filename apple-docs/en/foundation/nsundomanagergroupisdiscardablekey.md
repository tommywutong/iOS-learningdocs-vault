---
title: NSUndoManagerGroupIsDiscardableKey
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsundomanagergroupisdiscardablekey
source_url: 'https://developer.apple.com/documentation/foundation/nsundomanagergroupisdiscardablekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsundomanagergroupisdiscardablekey.json'
content_hash: 'sha256:b6a40755ef59e79c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSUndoManagerGroupIsDiscardableKey

<sub>Global Variable</sub>

A key, used in a notification’s user info, that indicates the undo group contains only discardable actions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSUndoManagerGroupIsDiscardableKey: String
```

## Discussion

The key has a corresponding value of [true](../swift/true.md), wrapped as a Boolean [NSNumber](nsnumber.md) object, if the undo group as a whole is discardable.

## See Also

### Working with notifications

- [NSUndoManagerWillUndoChangeNotification](nsnotification/name-swift.struct/nsundomanagerwillundochange.md) — Posted just before an undo manager performs an undo operation.
- [NSUndoManagerDidUndoChangeNotification](nsnotification/name-swift.struct/nsundomanagerdidundochange.md) — Posted just after an undo manager performs an undo operation.
- [NSUndoManagerWillRedoChangeNotification](nsnotification/name-swift.struct/nsundomanagerwillredochange.md) — Posted just before an undo manager performs a redo operation.
- [NSUndoManagerDidRedoChangeNotification](nsnotification/name-swift.struct/nsundomanagerdidredochange.md) — Posted just after an undo manager performs a redo operation.
- [NSUndoManagerCheckpointNotification](nsnotification/name-swift.struct/nsundomanagercheckpoint.md) — Posted whenever an undo manager opens or closes an undo group (except when it opens a top-level group) and when checking the redo stack.
- [NSUndoManagerDidOpenUndoGroupNotification](nsnotification/name-swift.struct/nsundomanagerdidopenundogroup.md) — Posted whenever an undo manager opens an undo group.
- [NSUndoManagerWillCloseUndoGroupNotification](nsnotification/name-swift.struct/nsundomanagerwillcloseundogroup.md) — Posted before an undo manager closes an undo group.
- [NSUndoManagerDidCloseUndoGroupNotification](nsnotification/name-swift.struct/nsundomanagerdidcloseundogroup.md) — Posted after an undo manager closes an undo group.
