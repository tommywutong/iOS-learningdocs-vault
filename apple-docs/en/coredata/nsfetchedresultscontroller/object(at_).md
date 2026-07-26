---
title: 'object(at:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsfetchedresultscontroller/object(at:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/object(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchedresultscontroller/object%28at%3A%29.json'
content_hash: 'sha256:24d18a7acefab5cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchedResultsController](../nsfetchedresultscontroller.md)

# object(at:)

<sub>Instance Method</sub>

Returns the object at the given index path in the fetch results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func object(at indexPath: IndexPath) -> ResultType
```

## Parameters

- `indexPath` — An index path in the fetch results. If `indexPath` does not describe a valid index path in the fetch results, an exception is raised.

## Return Value

The object at a given index path in the fetch results.

## See Also

### Accessing Results

- [fetchedObjects](fetchedobjects.md) — The results of the fetch.
- [- indexPathForObject:](<indexpath(forobject_).md>) — Returns the index path of a given object.
