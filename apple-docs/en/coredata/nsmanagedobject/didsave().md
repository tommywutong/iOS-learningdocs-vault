---
title: didSave()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobject/didsave()
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/didsave()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/didsave%28%29.json'
content_hash: 'sha256:8b0eaf674a57a4c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# didSave()

<sub>Instance Method</sub>

Provides an opportunity to add code into the life cycle of the managed object after the managed object’s context completes a save operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func didSave()
```

## Discussion

You can use this method to notify other objects after a save, and to compute transient values from persistent values.

This method can have “side effects” on the persistent values, however any changes you make using standard accessor methods will by default dirty the managed object context and leave your context with unsaved changes. Moreover, if the object’s context has an undo manager, such changes will add an undo operation. For document-based applications, changes made in `didSave` will therefore come into the next undo grouping, which can lead to “empty” undo operations from the user’s perspective. You may want to disable undo registration to avoid this issue.

The sense of “save” in the method name is that of a database commit statement and so applies to deletions as well as to updates to objects. For subclasses, this method is therefore an appropriate locus for code to be executed when an object deleted as well as “saved to disk.” You can find out if an object is marked for deletion with [deleted](isdeleted.md).

### Special Considerations

You cannot attempt to resurrect a deleted object in `didSave`.

## See Also

### Managing Change Events

- [contextShouldIgnoreUnmodeledPropertyChanges](contextshouldignoreunmodeledpropertychanges.md) — A Boolean value that indicates whether to mark instances of the class as having changes when an unmodeled property changes.
- [- awakeFromFetch](<awakefromfetch().md>) — Provides an opportunity to add code into the life cycle of the managed object when fufilling it from a fault.
- [- awakeFromInsert](<awakefrominsert().md>) — Provides an opportunity to add code into the life cycle of the managed object when initially creating it.
- [- awakeFromSnapshotEvents:](<awake(fromsnapshotevents_).md>) — Provides an opportunity to add code into the life cycle of the managed object when fulfilling it from a snapshot.
- [- changedValues](<changedvalues().md>) — Returns a dictionary containing the keys and new values of persistent properties with changes since the last fetching or saving of the managed object.
- [- changedValuesForCurrentEvent](<changedvaluesforcurrentevent().md>) — Returns a dictionary containing the keys and new values of persistent properties with changes since the last fetching or saving of the managed object.
- [- committedValuesForKeys:](<committedvalues(forkeys_).md>) — Returns a dictionary of the most recent fetched or saved values of the managed object for the properties of the specified keys.
- [- prepareForDeletion](<preparefordeletion().md>) — Provides an opportunity to add code into the life cycle of the managed object before deleting it.
- [- willSave](<willsave().md>) — Provides an opportunity to add code into the life cycle of the managed object before saving it.
- [- willTurnIntoFault](<willturnintofault().md>) — Provides an opportunity to add code into the life cycle of the managed object before converting it to a fault.
- [- didTurnIntoFault](<didturnintofault().md>) — Provides an opportunity to add code into the life cycle of the managed object after converting it to a fault.
- [fetchRequest()](<fetchrequest().md>) — Returns an initialized fetch request with the entity this subclass represents.
