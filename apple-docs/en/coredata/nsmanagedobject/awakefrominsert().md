---
title: awakeFromInsert()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobject/awakefrominsert()
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/awakefrominsert()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/awakefrominsert%28%29.json'
content_hash: 'sha256:a644946ccc088dc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# awakeFromInsert()

<sub>Instance Method</sub>

Provides an opportunity to add code into the life cycle of the managed object when initially creating it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func awakeFromInsert()
```

## Discussion

You typically use this method to initialize special default property values. This method is invoked only once in the object’s lifetime.

If you want to set attribute values in an implementation of this method, you should typically use primitive accessor methods (either [- setPrimitiveValue:forKey:](<setprimitivevalue(__forkey_).md>) or—better—the appropriate custom primitive accessors). This ensures that the new values are treated as baseline values rather than being recorded as undoable changes for the properties in question.

> [!important] Important
> Subclasses must invoke super’s implementation before performing their own initialization.

### Special Considerations

If you create a managed object then perform undo operations to bring the managed object context to a state prior to the object’s creation, then perform redo operations to bring the managed object context back to a state after the object’s creation, [- awakeFromInsert](<awakefrominsert().md>) is _not_ invoked a second time.

You are typically discouraged from performing fetches within an implementation of [- awakeFromInsert](<awakefrominsert().md>). Although it is allowed, execution of the fetch request can trigger the sending of internal Core Data notifications which may have unwanted side-effects. For example, in macOS, an instance of [NSArrayController](../../appkit/nsarraycontroller.md) may end up inserting a new object into its content array twice.

## See Also

### Managing Change Events

- [contextShouldIgnoreUnmodeledPropertyChanges](contextshouldignoreunmodeledpropertychanges.md) — A Boolean value that indicates whether to mark instances of the class as having changes when an unmodeled property changes.
- [- awakeFromFetch](<awakefromfetch().md>) — Provides an opportunity to add code into the life cycle of the managed object when fufilling it from a fault.
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
