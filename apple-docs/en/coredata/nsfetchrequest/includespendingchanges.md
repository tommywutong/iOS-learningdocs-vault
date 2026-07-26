---
title: includesPendingChanges
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchrequest/includespendingchanges
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchrequest/includespendingchanges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchrequest/includespendingchanges.json'
content_hash: 'sha256:2fb8486bbacd7cb3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchRequest](../nsfetchrequest.md)

# includesPendingChanges

<sub>Instance Property</sub>

A Boolean value that indicates whether, when the fetch is executed, it matches against currently unsaved changes in the managed object context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var includesPendingChanges: Bool { get set }
```

## Discussion

This value is [true](../../swift/true.md) if when the fetch is executed, the fetch will match against currently unsaved changes in the managed object context; otherwise the value is [false](../../swift/false.md). The default value is [true](../../swift/true.md).

If the value is [false](../../swift/false.md), the fetch request doesn’t check unsaved changes and only returns objects that matched the predicate in the persistent store.

### Special Considerations

A value of [true](../../swift/true.md) is not supported in conjunction with the result type [NSDictionaryResultType](../nsfetchrequestresulttype/dictionaryresulttype.md), including calculation of aggregate results (such as `max` and `min`). For dictionaries, the array returned from the fetch reflects the current state in the persistent store, and does not take into account any pending changes, insertions, or deletions in the context.

If you need to take pending changes into account for some simple aggregations like `max` and `min`, you can instead use a normal fetch request, sorted on the attribute you want, with a fetch limit of 1.

## See Also

### Managing How Results Are Returned

- [resultType](resulttype.md) — The result type of the fetch request.
- [propertiesToFetch](propertiestofetch.md) — A collection of either property descriptions or string property names that specify which properties should be returned by the fetch.
- [returnsDistinctResults](returnsdistinctresults.md) — A Boolean value that indicates whether the fetch request returns only distinct values for the fields specified by [propertiesToFetch](propertiestofetch.md).
- [includesPropertyValues](includespropertyvalues.md) — A Boolean value that indicates whether, when the fetch is executed, property data is obtained from the persistent store.
- [shouldRefreshRefetchedObjects](shouldrefreshrefetchedobjects.md) — A Boolean value that indicates whether the property values of fetched objects will be updated with the current values in the persistent store.
- [returnsObjectsAsFaults](returnsobjectsasfaults.md) — A Boolean value that indicates whether the objects resulting from a fetch request are faults.
- [NSFetchRequestResultType](../nsfetchrequestresulttype.md) — Constants that specify the possible result types a fetch request can return.
- [NSFetchRequestResult](../nsfetchrequestresult.md) — An abstract protocol used with parameterized fetch requests.
