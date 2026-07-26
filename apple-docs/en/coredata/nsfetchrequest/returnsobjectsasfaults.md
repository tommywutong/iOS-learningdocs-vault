---
title: returnsObjectsAsFaults
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchrequest/returnsobjectsasfaults
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchrequest/returnsobjectsasfaults'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchrequest/returnsobjectsasfaults.json'
content_hash: 'sha256:1dc2cf2d4d978f93'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchRequest](../nsfetchrequest.md)

# returnsObjectsAsFaults

<sub>Instance Property</sub>

A Boolean value that indicates whether the objects resulting from a fetch request are faults.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var returnsObjectsAsFaults: Bool { get set }
```

## Discussion

This value is [true](../../swift/true.md) if the objects resulting from a fetch using the [NSFetchRequest](../nsfetchrequest.md) are faults; otherwise, it is [false](../../swift/false.md). The default value is [true](../../swift/true.md). This setting is not used if the result type (see [resultType](resulttype.md)) is `NSManagedObjectIDResultType`, as object IDs do not have property values. You can set [returnsObjectsAsFaults](returnsobjectsasfaults.md) to [false](../../swift/false.md) to gain a performance benefit if you know you will need to access the property values from the returned objects.

When you execute a fetch, by default [returnsObjectsAsFaults](returnsobjectsasfaults.md) is [true](../../swift/true.md); Core Data fetches the object data for the matching records, fills the row cache with the information, and returns managed object as faults. These faults are managed objects, but all of their property data resides in the row cache until the fault is fired. When the fault is fired, Core Data retrieves the data from the row cache. Although the overhead for this operation is small, for large datasets it may not be trivial. If you _need_ to access the property values from the returned objects (for example, if you iterate over all the objects to calculate the average value of a particular attribute), then it is more efficient to set [returnsObjectsAsFaults](returnsobjectsasfaults.md) to [false](../../swift/false.md) to avoid the additional overhead.

## See Also

### Managing How Results Are Returned

- [resultType](resulttype.md) — The result type of the fetch request.
- [includesPendingChanges](includespendingchanges.md) — A Boolean value that indicates whether, when the fetch is executed, it matches against currently unsaved changes in the managed object context.
- [propertiesToFetch](propertiestofetch.md) — A collection of either property descriptions or string property names that specify which properties should be returned by the fetch.
- [returnsDistinctResults](returnsdistinctresults.md) — A Boolean value that indicates whether the fetch request returns only distinct values for the fields specified by [propertiesToFetch](propertiestofetch.md).
- [includesPropertyValues](includespropertyvalues.md) — A Boolean value that indicates whether, when the fetch is executed, property data is obtained from the persistent store.
- [shouldRefreshRefetchedObjects](shouldrefreshrefetchedobjects.md) — A Boolean value that indicates whether the property values of fetched objects will be updated with the current values in the persistent store.
- [NSFetchRequestResultType](../nsfetchrequestresulttype.md) — Constants that specify the possible result types a fetch request can return.
- [NSFetchRequestResult](../nsfetchrequestresult.md) — An abstract protocol used with parameterized fetch requests.
