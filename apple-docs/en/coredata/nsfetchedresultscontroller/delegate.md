---
title: delegate
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchedresultscontroller/delegate
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchedresultscontroller/delegate.json'
content_hash: 'sha256:ba763ee27cfcde5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchedResultsController](../nsfetchedresultscontroller.md)

# delegate

<sub>Instance Property</sub>

The object that is notified when the fetched results changed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
unowned(unsafe) var delegate: (any NSFetchedResultsControllerDelegate)? { get set }
```

## Discussion

If you do not specify a delegate, the controller does not track changes to managed objects associated with its managed object context.

## See Also

### Getting Configuration Information

- [fetchRequest](fetchrequest.md) — The fetch request used to do the fetching.
- [managedObjectContext](managedobjectcontext.md) — The managed object context used to fetch objects.
- [sectionNameKeyPath](sectionnamekeypath.md) — The key path of the attribute that determines which section the fetched entity belongs to.
- [cacheName](cachename.md) — The name of the file used to cache section information.
- [+ deleteCacheWithName:](<deletecache(withname_).md>) — Deletes the cached section information with the given name.
