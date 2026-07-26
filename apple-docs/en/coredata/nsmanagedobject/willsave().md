---
title: willSave()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobject/willsave()
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/willsave()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/willsave%28%29.json'
content_hash: 'sha256:5b991f0ec2c47448'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# willSave()

<sub>Instance Method</sub>

Provides an opportunity to add code into the life cycle of the managed object before saving it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func willSave()
```

## Discussion

This method can have “side effects” on persistent values. You can use it to, for example, compute persistent values from other transient or scratchpad values.

If you want to update a persistent property value, you should typically test for equality of any new value with the existing value before making a change. If you change property values using standard accessor methods, Core Data will observe the resultant change notification and so invoke `willSave` again before saving the object’s managed object context. If you continue to modify a value in `willSave`, `willSave` will continue to be called until your program crashes.

For example, if you set a last-modified timestamp, you should check whether either you previously set it in the same save operation, or that the existing timestamp is not less than a small delta from the current time. Typically it’s better to calculate the timestamp once for all the objects being saved (for example, in response to an `NSManagedObjectContextWillSaveNotification`).

If you change property values using primitive accessors, you avoid the possibility of infinite recursion, but Core Data will not notice the change you make.

The sense of “save” in the method name is that of a database commit statement and so applies to deletions as well as to updates to objects. For subclasses, this method is therefore an appropriate locus for code to be executed when an object deleted as well as “saved to disk.” You can find out if an object is marked for deletion with [deleted](isdeleted.md).

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
- [- didSave](<didsave().md>) — Provides an opportunity to add code into the life cycle of the managed object after the managed object’s context completes a save operation.
- [- willTurnIntoFault](<willturnintofault().md>) — Provides an opportunity to add code into the life cycle of the managed object before converting it to a fault.
- [- didTurnIntoFault](<didturnintofault().md>) — Provides an opportunity to add code into the life cycle of the managed object after converting it to a fault.
- [fetchRequest()](<fetchrequest().md>) — Returns an initialized fetch request with the entity this subclass represents.
