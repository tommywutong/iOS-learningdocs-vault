---
title: fetchRequest
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchedresultscontroller/fetchrequest
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/fetchrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchedresultscontroller/fetchrequest.json'
content_hash: 'sha256:c6f34c460c98373a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchedResultsController](../nsfetchedresultscontroller.md)

# fetchRequest

<sub>Instance Property</sub>

The fetch request used to do the fetching.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fetchRequest: NSFetchRequest<ResultType> { get }
```

## Discussion

If you want to modify the fetch request, you must follow the steps described in [Modifying the fetch request](../nsfetchedresultscontroller.md#Modifying-the-fetch-request).

## See Also

### Related Documentation

- [- initWithFetchRequest:managedObjectContext:sectionNameKeyPath:cacheName:](<init(fetchrequest_managedobjectcontext_sectionnamekeypath_cachename_).md>) — Returns a fetch request controller initialized using the given arguments.

### Getting Configuration Information

- [managedObjectContext](managedobjectcontext.md) — The managed object context used to fetch objects.
- [sectionNameKeyPath](sectionnamekeypath.md) — The key path of the attribute that determines which section the fetched entity belongs to.
- [cacheName](cachename.md) — The name of the file used to cache section information.
- [delegate](delegate.md) — The object that is notified when the fetched results changed.
- [+ deleteCacheWithName:](<deletecache(withname_).md>) — Deletes the cached section information with the given name.
