---
title: awakeFromFetch()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobject/awakefromfetch()
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/awakefromfetch()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/awakefromfetch%28%29.json'
content_hash: 'sha256:09da20df12a32cca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# awakeFromFetch()

<sub>Instance Method</sub>

Provides an opportunity to add code into the life cycle of the managed object when fufilling it from a fault.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func awakeFromFetch()
```

## Discussion

You typically use this method to compute derived values or to recreate transient relationships from the receiver’s persistent properties.

The managed object context’s change processing is explicitly disabled around this method so that you can use public setters to establish transient values and other caches without dirtying the object or its context. Because of this, however, you should not modify relationships in this method as the inverse will not be set.

> [!important] Important
> Subclasses must invoke super’s implementation before performing their own initialization.

## See Also

### Related Documentation

- [- setPrimitiveValue:forKey:](<setprimitivevalue(__forkey_).md>) — Sets the value of a given property in the managed object’s private internal storage.
- [- primitiveValueForKey:](<primitivevalue(forkey_).md>) — Returns the value for the specified property from the managed object’s private internal storage .

### Managing Change Events

- [contextShouldIgnoreUnmodeledPropertyChanges](contextshouldignoreunmodeledpropertychanges.md) — A Boolean value that indicates whether to mark instances of the class as having changes when an unmodeled property changes.
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
