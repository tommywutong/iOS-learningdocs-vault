---
title: includesPropertyValues
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchrequest/includespropertyvalues
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchrequest/includespropertyvalues'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchrequest/includespropertyvalues.json'
content_hash: 'sha256:0278c1dd59a1e719'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchRequest](../nsfetchrequest.md)

# includesPropertyValues

<sub>Instance Property</sub>

A Boolean value that indicates whether, when the fetch is executed, property data is obtained from the persistent store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var includesPropertyValues: Bool { get set }
```

## Discussion

This value is [true](../../swift/true.md) if when the fetch is executed, property data is obtained from the persistent store; otherwise it is [false](../../swift/false.md). The default value is [true](../../swift/true.md).

You can set [includesPropertyValues](includespropertyvalues.md) to [false](../../swift/false.md) to avoid creating objects to represent property values and thereby reduce memory overhead. You typically should only do so, however, if you are sure that you will not need the actual property data, or you already have the information in the row cache. Otherwise, you will incur multiple trips to the database.

During a normal fetch ([includesPropertyValues](includespropertyvalues.md) is [true](../../swift/true.md)), Core Data fetches the object ID _and_ property data for the matching records, fills the row cache with the information, and returns managed objects as faults (see [returnsObjectsAsFaults](returnsobjectsasfaults.md)). Although these faults are managed objects, all of their property data still resides in the row cache until the fault is fired. When the fault is fired, Core Data retrieves the data from the row cache—there is no need to go back to the database.

If [includesPropertyValues](includespropertyvalues.md) is [false](../../swift/false.md), then Core Data fetches _only_ the object ID information for the matching records—it does not populate the row cache. Core Data still returns managed objects because it only needs managed object IDs to create faults. However, if you subsequently fire the fault, Core Data looks in the (empty) row cache, doesn’t find any data, and then goes back to the store a second time for the data.

If [includesPropertyValues](includespropertyvalues.md) is [true](../../swift/true.md) and [resultType](resulttype.md) is set to [NSManagedObjectIDResultType](../nsfetchrequestresulttype/managedobjectidresulttype.md), the properties are fetched even though they are not being presented to the application and can result in a significant performance penalty.

## See Also

### Managing How Results Are Returned

- [resultType](resulttype.md) — The result type of the fetch request.
- [includesPendingChanges](includespendingchanges.md) — A Boolean value that indicates whether, when the fetch is executed, it matches against currently unsaved changes in the managed object context.
- [propertiesToFetch](propertiestofetch.md) — A collection of either property descriptions or string property names that specify which properties should be returned by the fetch.
- [returnsDistinctResults](returnsdistinctresults.md) — A Boolean value that indicates whether the fetch request returns only distinct values for the fields specified by [propertiesToFetch](propertiestofetch.md).
- [shouldRefreshRefetchedObjects](shouldrefreshrefetchedobjects.md) — A Boolean value that indicates whether the property values of fetched objects will be updated with the current values in the persistent store.
- [returnsObjectsAsFaults](returnsobjectsasfaults.md) — A Boolean value that indicates whether the objects resulting from a fetch request are faults.
- [NSFetchRequestResultType](../nsfetchrequestresulttype.md) — Constants that specify the possible result types a fetch request can return.
- [NSFetchRequestResult](../nsfetchrequestresult.md) — An abstract protocol used with parameterized fetch requests.
