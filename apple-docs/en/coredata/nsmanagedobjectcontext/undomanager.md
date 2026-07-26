---
title: undoManager
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontext/undomanager
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/undomanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/undomanager.json'
content_hash: 'sha256:5597fdc50d903ad4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# undoManager

<sub>Instance Property</sub>

The object that provides undo support for the context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var undoManager: UndoManager? { get set }
```

## Discussion

Enable undo support for a context by setting this property to an instance of [UndoManager](../../foundation/undomanager.md). This can be an undo manager that’s exclusive to the context, or an existing undo manager if you want to integrate the context’s undo operations with those of the rest of your app.

If your context uses an undo manager, you can realize a performance benefit by temporarily setting this property to `nil` when performing expensive operations on that context, such as importing a large number of objects.

The default value is `nil`.

## See Also

### Undoing changes

- [- undo](<undo().md>) — Sends an undo message to the context’s undo manager, asking it to reverse the latest uncommitted changes applied to objects in the object graph.
- [- redo](<redo().md>) — Sends a redo message to the context’s undo manager, asking it to reverse the latest undo operation applied to objects in the object graph.
- [- reset](<reset().md>) — Returns the context to its base state.
- [- rollback](<rollback().md>) — Removes everything from the undo stack, discards all insertions and deletions, and restores updated objects to their last committed values.
