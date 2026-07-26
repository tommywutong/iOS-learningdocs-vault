---
title: shouldRefreshRefetchedObjects
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchrequest/shouldrefreshrefetchedobjects
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchrequest/shouldrefreshrefetchedobjects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchrequest/shouldrefreshrefetchedobjects.json'
content_hash: 'sha256:54aed57986acef26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchRequest](../nsfetchrequest.md)

# shouldRefreshRefetchedObjects

<sub>Instance Property</sub>

A Boolean value that indicates whether the property values of fetched objects will be updated with the current values in the persistent store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var shouldRefreshRefetchedObjects: Bool { get set }
```

## Discussion

This value is [true](../../swift/true.md) if the property values of fetched objects will be updated with the current values in the persistent store; otherwise, it is [false](../../swift/false.md).

By default when you fetch objects, they maintain their current property values, even if the values in the persistent store have changed. Invoking this method with the parameter [true](../../swift/true.md) means that when the fetch is executed, the property values of fetched objects are updated with the current values in the persistent store. This is a more convenient way to ensure that managed object property values are consistent with the store than by using [- refreshObject:mergeChanges:](<../nsmanagedobjectcontext/refresh(__mergechanges_).md>) (`NSManagedObjetContext`) for multiple objects in turn.

## See Also

### Managing How Results Are Returned

- [resultType](resulttype.md) — The result type of the fetch request.
- [includesPendingChanges](includespendingchanges.md) — A Boolean value that indicates whether, when the fetch is executed, it matches against currently unsaved changes in the managed object context.
- [propertiesToFetch](propertiestofetch.md) — A collection of either property descriptions or string property names that specify which properties should be returned by the fetch.
- [returnsDistinctResults](returnsdistinctresults.md) — A Boolean value that indicates whether the fetch request returns only distinct values for the fields specified by [propertiesToFetch](propertiestofetch.md).
- [includesPropertyValues](includespropertyvalues.md) — A Boolean value that indicates whether, when the fetch is executed, property data is obtained from the persistent store.
- [returnsObjectsAsFaults](returnsobjectsasfaults.md) — A Boolean value that indicates whether the objects resulting from a fetch request are faults.
- [NSFetchRequestResultType](../nsfetchrequestresulttype.md) — Constants that specify the possible result types a fetch request can return.
- [NSFetchRequestResult](../nsfetchrequestresult.md) — An abstract protocol used with parameterized fetch requests.
