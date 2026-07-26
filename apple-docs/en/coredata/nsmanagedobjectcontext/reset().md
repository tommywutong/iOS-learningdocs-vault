---
title: reset()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontext/reset()
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/reset()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/reset%28%29.json'
content_hash: 'sha256:683d28db76db5f53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# reset()

<sub>Instance Method</sub>

Returns the context to its base state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func reset()
```

## Discussion

All the receiver’s managed objects are “forgotten.” If you use this method, you should ensure that you also discard references to any managed objects fetched using the receiver, since they will be invalid afterwards.

## See Also

### Related Documentation

- [stalenessInterval](stalenessinterval.md) — The maximum length of time that may have elapsed since the store previously fetched data before fulfilling a fault issues a new fetch.

### Undoing changes

- [undoManager](undomanager.md) — The object that provides undo support for the context.
- [- undo](<undo().md>) — Sends an undo message to the context’s undo manager, asking it to reverse the latest uncommitted changes applied to objects in the object graph.
- [- redo](<redo().md>) — Sends a redo message to the context’s undo manager, asking it to reverse the latest undo operation applied to objects in the object graph.
- [- rollback](<rollback().md>) — Removes everything from the undo stack, discards all insertions and deletions, and restores updated objects to their last committed values.
