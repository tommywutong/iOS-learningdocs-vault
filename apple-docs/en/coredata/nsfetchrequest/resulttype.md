---
title: resultType
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchrequest/resulttype
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchrequest/resulttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchrequest/resulttype.json'
content_hash: 'sha256:436693e0024fe2f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchRequest](../nsfetchrequest.md)

# resultType

<sub>Instance Property</sub>

The result type of the fetch request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var resultType: NSFetchRequestResultType { get set }
```

## Discussion

The default value is [NSManagedObjectResultType](../nsfetchrequestresulttype/managedobjectresulttype.md).

If you set the value to [NSManagedObjectIDResultType](../nsfetchrequestresulttype/managedobjectidresulttype.md), and do not include property values in the request, sort orderings are demoted  to “best efforts” hints.

[includesPendingChanges](includespendingchanges.md) discusses with whether pending changes are taken into account when the `resultType` is set to `managedObjectResultType`.

[includesPropertyValues](includespropertyvalues.md) discusses whether property values are included or not by default when the `resultType` is set to `managedObjectResultType`.

## See Also

### Managing How Results Are Returned

- [includesPendingChanges](includespendingchanges.md) — A Boolean value that indicates whether, when the fetch is executed, it matches against currently unsaved changes in the managed object context.
- [propertiesToFetch](propertiestofetch.md) — A collection of either property descriptions or string property names that specify which properties should be returned by the fetch.
- [returnsDistinctResults](returnsdistinctresults.md) — A Boolean value that indicates whether the fetch request returns only distinct values for the fields specified by [propertiesToFetch](propertiestofetch.md).
- [includesPropertyValues](includespropertyvalues.md) — A Boolean value that indicates whether, when the fetch is executed, property data is obtained from the persistent store.
- [shouldRefreshRefetchedObjects](shouldrefreshrefetchedobjects.md) — A Boolean value that indicates whether the property values of fetched objects will be updated with the current values in the persistent store.
- [returnsObjectsAsFaults](returnsobjectsasfaults.md) — A Boolean value that indicates whether the objects resulting from a fetch request are faults.
- [NSFetchRequestResultType](../nsfetchrequestresulttype.md) — Constants that specify the possible result types a fetch request can return.
- [NSFetchRequestResult](../nsfetchrequestresult.md) — An abstract protocol used with parameterized fetch requests.
