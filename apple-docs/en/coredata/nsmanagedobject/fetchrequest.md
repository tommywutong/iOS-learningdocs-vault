---
title: fetchRequest
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobject/fetchrequest
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/fetchrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/fetchrequest.json'
content_hash: 'sha256:d232c59c5c534eb2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# fetchRequest

<sub>Type Method</sub>

Returns an initialized fetch request with the entity this subclass represents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSFetchRequest *) fetchRequest;
```

## Discussion

This method is only legal to call on subclasses of `NSManagedObject` that represent a single entity in the model.

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
- [- didSave](<didsave().md>) — Provides an opportunity to add code into the life cycle of the managed object after the managed object’s context completes a save operation.
- [- willTurnIntoFault](<willturnintofault().md>) — Provides an opportunity to add code into the life cycle of the managed object before converting it to a fault.
- [- didTurnIntoFault](<didturnintofault().md>) — Provides an opportunity to add code into the life cycle of the managed object after converting it to a fault.
