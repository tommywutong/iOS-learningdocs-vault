---
title: 'deleteCache(withName:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsfetchedresultscontroller/deletecache(withname:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/deletecache(withname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchedresultscontroller/deletecache%28withname%3A%29.json'
content_hash: 'sha256:4ad79d90fd42fe2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchedResultsController](../nsfetchedresultscontroller.md)

# deleteCache(withName:)

<sub>Type Method</sub>

Deletes the cached section information with the given name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func deleteCache(withName name: String?)
```

## Parameters

- `name` — The name of the cache file to delete. If `name` is `nil`, deletes all cache files.

## See Also

### Getting Configuration Information

- [fetchRequest](fetchrequest.md) — The fetch request used to do the fetching.
- [managedObjectContext](managedobjectcontext.md) — The managed object context used to fetch objects.
- [sectionNameKeyPath](sectionnamekeypath.md) — The key path of the attribute that determines which section the fetched entity belongs to.
- [cacheName](cachename.md) — The name of the file used to cache section information.
- [delegate](delegate.md) — The object that is notified when the fetched results changed.
