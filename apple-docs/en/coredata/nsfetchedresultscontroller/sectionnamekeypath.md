---
title: sectionNameKeyPath
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchedresultscontroller/sectionnamekeypath
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/sectionnamekeypath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchedresultscontroller/sectionnamekeypath.json'
content_hash: 'sha256:34d96b4b712215c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchedResultsController](../nsfetchedresultscontroller.md)

# sectionNameKeyPath

<sub>Instance Property</sub>

The key path of the attribute that determines which section the fetched entity belongs to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sectionNameKeyPath: String? { get }
```

## Discussion

This property returns the value you specify for the `sectionNameKeyPath` parameter when you initialize the fetched results controller.

If the controller generates sections, typically this property’s value matches the specified key path of the first sort descriptor in the controller’s fetch request. If the two key paths don’t match, then they must generate the same relative ordering. For example, the fetch request’s first sort descriptor might specify the key path of a persistent attribute, but [sectionNameKeyPath](sectionnamekeypath.md) might specify the key path of a transient attribute that derives its value from the persistent one.

## See Also

### Getting Configuration Information

- [fetchRequest](fetchrequest.md) — The fetch request used to do the fetching.
- [managedObjectContext](managedobjectcontext.md) — The managed object context used to fetch objects.
- [cacheName](cachename.md) — The name of the file used to cache section information.
- [delegate](delegate.md) — The object that is notified when the fetched results changed.
- [+ deleteCacheWithName:](<deletecache(withname_).md>) — Deletes the cached section information with the given name.
