---
title: contextShouldIgnoreUnmodeledPropertyChanges
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobject/contextshouldignoreunmodeledpropertychanges
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/contextshouldignoreunmodeledpropertychanges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/contextshouldignoreunmodeledpropertychanges.json'
content_hash: 'sha256:5a996e15d7b5f506'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# contextShouldIgnoreUnmodeledPropertyChanges

<sub>Type Property</sub>

A Boolean value that indicates whether to mark instances of the class as having changes when an unmodeled property changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var contextShouldIgnoreUnmodeledPropertyChanges: Bool { get }
```

## Return Value

[false](../../swift/false.md) if instances of the class should be marked as having changes if an unmodeled property is changed, otherwise [true](../../swift/true.md).

## Discussion

The default value is [true](../../swift/true.md).

## See Also

### Related Documentation

- [hasChanges](../nsmanagedobjectcontext/haschanges.md) — A Boolean value that indicates whether the context has uncommitted changes.

### Managing Change Events

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
- [fetchRequest()](<fetchrequest().md>) — Returns an initialized fetch request with the entity this subclass represents.
