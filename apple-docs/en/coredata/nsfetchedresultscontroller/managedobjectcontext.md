---
title: managedObjectContext
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchedresultscontroller/managedobjectcontext
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/managedobjectcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchedresultscontroller/managedobjectcontext.json'
content_hash: 'sha256:1dd172c41fea7a81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchedResultsController](../nsfetchedresultscontroller.md)

# managedObjectContext

<sub>Instance Property</sub>

The managed object context used to fetch objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var managedObjectContext: NSManagedObjectContext { get }
```

## Discussion

The controller registers to listen to change notifications on this context and properly update its result set and section information.

## See Also

### Getting Configuration Information

- [fetchRequest](fetchrequest.md) — The fetch request used to do the fetching.
- [sectionNameKeyPath](sectionnamekeypath.md) — The key path of the attribute that determines which section the fetched entity belongs to.
- [cacheName](cachename.md) — The name of the file used to cache section information.
- [delegate](delegate.md) — The object that is notified when the fetched results changed.
- [+ deleteCacheWithName:](<deletecache(withname_).md>) — Deletes the cached section information with the given name.
