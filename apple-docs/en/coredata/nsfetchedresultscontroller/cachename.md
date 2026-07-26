---
title: cacheName
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchedresultscontroller/cachename
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/cachename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchedresultscontroller/cachename.json'
content_hash: 'sha256:12011fad5b8723ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchedResultsController](../nsfetchedresultscontroller.md)

# cacheName

<sub>Instance Property</sub>

The name of the file used to cache section information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var cacheName: String? { get }
```

## Discussion

The file itself is stored in a private directory; you can only access it by name using [+ deleteCacheWithName:](<deletecache(withname_).md>)

## See Also

### Related Documentation

- [- initWithFetchRequest:managedObjectContext:sectionNameKeyPath:cacheName:](<init(fetchrequest_managedobjectcontext_sectionnamekeypath_cachename_).md>) — Returns a fetch request controller initialized using the given arguments.

### Getting Configuration Information

- [fetchRequest](fetchrequest.md) — The fetch request used to do the fetching.
- [managedObjectContext](managedobjectcontext.md) — The managed object context used to fetch objects.
- [sectionNameKeyPath](sectionnamekeypath.md) — The key path of the attribute that determines which section the fetched entity belongs to.
- [delegate](delegate.md) — The object that is notified when the fetched results changed.
- [+ deleteCacheWithName:](<deletecache(withname_).md>) — Deletes the cached section information with the given name.
