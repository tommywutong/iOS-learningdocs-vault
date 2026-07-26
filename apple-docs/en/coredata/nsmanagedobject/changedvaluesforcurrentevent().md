---
title: changedValuesForCurrentEvent()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobject/changedvaluesforcurrentevent()
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/changedvaluesforcurrentevent()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/changedvaluesforcurrentevent%28%29.json'
content_hash: 'sha256:68df2d2dcd0f00ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# changedValuesForCurrentEvent()

<sub>Instance Method</sub>

Returns a dictionary containing the keys and new values of persistent properties with changes since the last fetching or saving of the managed object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func changedValuesForCurrentEvent() -> [String : Any]
```

## Return Value

A dictionary with keys that are the names of persistent properties with changes since the last posting of [NSManagedObjectContextObjectsDidChange](../../foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextobjectsdidchange.md), and with the new values for those properties.

## Discussion

This method only reports changes to properties that are persistent properties of the receiver, not changes to transient properties or custom instance variables.

> [!note] Note
> In Objective-C, this method returns the keys and values of persistent properties with changes since the last posting of [NSManagedObjectContextObjectsDidChangeNotification](../nsmanagedobjectcontextobjectsdidchangenotification.md).

## See Also

### Managing Change Events

- [contextShouldIgnoreUnmodeledPropertyChanges](contextshouldignoreunmodeledpropertychanges.md) — A Boolean value that indicates whether to mark instances of the class as having changes when an unmodeled property changes.
- [- awakeFromFetch](<awakefromfetch().md>) — Provides an opportunity to add code into the life cycle of the managed object when fufilling it from a fault.
- [- awakeFromInsert](<awakefrominsert().md>) — Provides an opportunity to add code into the life cycle of the managed object when initially creating it.
- [- awakeFromSnapshotEvents:](<awake(fromsnapshotevents_).md>) — Provides an opportunity to add code into the life cycle of the managed object when fulfilling it from a snapshot.
- [- changedValues](<changedvalues().md>) — Returns a dictionary containing the keys and new values of persistent properties with changes since the last fetching or saving of the managed object.
- [- committedValuesForKeys:](<committedvalues(forkeys_).md>) — Returns a dictionary of the most recent fetched or saved values of the managed object for the properties of the specified keys.
- [- prepareForDeletion](<preparefordeletion().md>) — Provides an opportunity to add code into the life cycle of the managed object before deleting it.
- [- willSave](<willsave().md>) — Provides an opportunity to add code into the life cycle of the managed object before saving it.
- [- didSave](<didsave().md>) — Provides an opportunity to add code into the life cycle of the managed object after the managed object’s context completes a save operation.
- [- willTurnIntoFault](<willturnintofault().md>) — Provides an opportunity to add code into the life cycle of the managed object before converting it to a fault.
- [- didTurnIntoFault](<didturnintofault().md>) — Provides an opportunity to add code into the life cycle of the managed object after converting it to a fault.
- [fetchRequest()](<fetchrequest().md>) — Returns an initialized fetch request with the entity this subclass represents.
