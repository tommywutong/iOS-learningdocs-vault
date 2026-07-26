---
title: undo()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontext/undo()
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/undo()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/undo%28%29.json'
content_hash: 'sha256:7f399da4d8ab3e67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# undo()

<sub>Instance Method</sub>

Sends an undo message to the context’s undo manager, asking it to reverse the latest uncommitted changes applied to objects in the object graph.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func undo()
```

## See Also

### Related Documentation

- [- processPendingChanges](<processpendingchanges().md>) — Forces the context to process changes to the object graph.

### Undoing changes

- [undoManager](undomanager.md) — The object that provides undo support for the context.
- [- redo](<redo().md>) — Sends a redo message to the context’s undo manager, asking it to reverse the latest undo operation applied to objects in the object graph.
- [- reset](<reset().md>) — Returns the context to its base state.
- [- rollback](<rollback().md>) — Removes everything from the undo stack, discards all insertions and deletions, and restores updated objects to their last committed values.
