---
title: 'indexPath(forObject:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsfetchedresultscontroller/indexpath(forobject:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/indexpath(forobject:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchedresultscontroller/indexpath%28forobject%3A%29.json'
content_hash: 'sha256:c63bd071d0c80042'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchedResultsController](../nsfetchedresultscontroller.md)

# indexPath(forObject:)

<sub>Instance Method</sub>

Returns the index path of a given object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func indexPath(forObject object: ResultType) -> IndexPath?
```

## Parameters

- `object` — An object in the receiver’s fetch results.

## Return Value

The index path of `object` in the receiver’s fetch results, or `nil` if `object` could not be found.

## Discussion

In versions of iOS before 3.2, this method raises an exception if `object` is not contained in the receiver’s fetch results.

## See Also

### Accessing Results

- [fetchedObjects](fetchedobjects.md) — The results of the fetch.
- [- objectAtIndexPath:](<object(at_).md>) — Returns the object at the given index path in the fetch results.
