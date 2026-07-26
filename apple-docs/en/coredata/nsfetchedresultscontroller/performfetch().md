---
title: performFetch()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchedresultscontroller/performfetch()
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/performfetch()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchedresultscontroller/performfetch%28%29.json'
content_hash: 'sha256:64c0f6d8102d67d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchedResultsController](../nsfetchedresultscontroller.md)

# performFetch()

<sub>Instance Method</sub>

Executes the controller’s fetch request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func performFetch() throws
```

## Discussion

After you execute this method, access the controller’s fetched objects using the [fetchedObjects](fetchedobjects.md) property.

> [!important] Important
> If you specify a value for the `sectionNameKeyPath` parameter when you initialize the fetched results controller, the fetch request must include a sort descriptor for the corresponding key path; otherwise, the fetch fails.

## See Also

### Initializing a Fetched Results Controller

- [- initWithFetchRequest:managedObjectContext:sectionNameKeyPath:cacheName:](<init(fetchrequest_managedobjectcontext_sectionnamekeypath_cachename_).md>) — Returns a fetch request controller initialized using the given arguments.
