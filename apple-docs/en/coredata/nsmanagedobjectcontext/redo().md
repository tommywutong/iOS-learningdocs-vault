---
title: redo()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontext/redo()
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/redo()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/redo%28%29.json'
content_hash: 'sha256:231085be94da92bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# redo()

<sub>Instance Method</sub>

Sends a redo message to the context’s undo manager, asking it to reverse the latest undo operation applied to objects in the object graph.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func redo()
```

## See Also

### Related Documentation

- [- processPendingChanges](<processpendingchanges().md>) — Forces the context to process changes to the object graph.

### Undoing changes

- [undoManager](undomanager.md) — The object that provides undo support for the context.
- [- undo](<undo().md>) — Sends an undo message to the context’s undo manager, asking it to reverse the latest uncommitted changes applied to objects in the object graph.
- [- reset](<reset().md>) — Returns the context to its base state.
- [- rollback](<rollback().md>) — Removes everything from the undo stack, discards all insertions and deletions, and restores updated objects to their last committed values.
