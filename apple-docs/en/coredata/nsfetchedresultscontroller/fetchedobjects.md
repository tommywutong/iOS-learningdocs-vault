---
title: fetchedObjects
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchedresultscontroller/fetchedobjects
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/fetchedobjects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchedresultscontroller/fetchedobjects.json'
content_hash: 'sha256:610b237c55c10557'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchedResultsController](../nsfetchedresultscontroller.md)

# fetchedObjects

<sub>Instance Property</sub>

The results of the fetch.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fetchedObjects: [ResultType]? { get }
```

## Discussion

The value of the property is `nil` if [- performFetch:](<performfetch().md>) hasn’t been called.

The results array only includes instances of the entity specified by the fetch request ([fetchRequest](fetchrequest.md)) and that match its predicate. (If the fetch request has no predicate, then the results array includes all instances of the entity specified by the fetch request.)

The results array reflects the in-memory state of managed objects in the controller’s managed object context, not their state in the persistent store. The returned array does not, however, update as managed objects are inserted, modified, or deleted.

## See Also

### Related Documentation

- [fetch(_:)](<../nsmanagedobjectcontext/fetch(__)-38ys1.md>) — Returns an array of objects that meet the criteria of the specified fetch request.

### Accessing Results

- [- objectAtIndexPath:](<object(at_).md>) — Returns the object at the given index path in the fetch results.
- [- indexPathForObject:](<indexpath(forobject_).md>) — Returns the index path of a given object.
