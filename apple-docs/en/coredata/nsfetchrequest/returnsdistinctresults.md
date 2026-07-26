---
title: returnsDistinctResults
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchrequest/returnsdistinctresults
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchrequest/returnsdistinctresults'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchrequest/returnsdistinctresults.json'
content_hash: 'sha256:73cc8e4451e1e442'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchRequest](../nsfetchrequest.md)

# returnsDistinctResults

<sub>Instance Property</sub>

A Boolean value that indicates whether the fetch request returns only distinct values for the fields specified by [propertiesToFetch](propertiestofetch.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var returnsDistinctResults: Bool { get set }
```

## Discussion

This value is used only if a value has been set for [propertiesToFetch](propertiestofetch.md).

This value is [true](../../swift/true.md) if when the fetch is executed, it returns only distinct values for the fields specified by [propertiesToFetch](propertiestofetch.md); otherwise, the value is [false](../../swift/false.md). The default value is [false](../../swift/false.md).

## See Also

### Managing How Results Are Returned

- [resultType](resulttype.md) — The result type of the fetch request.
- [includesPendingChanges](includespendingchanges.md) — A Boolean value that indicates whether, when the fetch is executed, it matches against currently unsaved changes in the managed object context.
- [propertiesToFetch](propertiestofetch.md) — A collection of either property descriptions or string property names that specify which properties should be returned by the fetch.
- [includesPropertyValues](includespropertyvalues.md) — A Boolean value that indicates whether, when the fetch is executed, property data is obtained from the persistent store.
- [shouldRefreshRefetchedObjects](shouldrefreshrefetchedobjects.md) — A Boolean value that indicates whether the property values of fetched objects will be updated with the current values in the persistent store.
- [returnsObjectsAsFaults](returnsobjectsasfaults.md) — A Boolean value that indicates whether the objects resulting from a fetch request are faults.
- [NSFetchRequestResultType](../nsfetchrequestresulttype.md) — Constants that specify the possible result types a fetch request can return.
- [NSFetchRequestResult](../nsfetchrequestresult.md) — An abstract protocol used with parameterized fetch requests.
