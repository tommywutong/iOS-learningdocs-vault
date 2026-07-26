---
title: NSFetchRequestResult
framework: Core Data
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchrequestresult
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchrequestresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchrequestresult.json'
content_hash: 'sha256:a0810606578f8e84'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSFetchRequestResult

<sub>Protocol</sub>

An abstract protocol used with parameterized fetch requests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NSFetchRequestResult : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [NSManagedObject](nsmanagedobject.md), [NSManagedObjectID](nsmanagedobjectid.md)

## See Also

### Managing How Results Are Returned

- [resultType](nsfetchrequest/resulttype.md) — The result type of the fetch request.
- [includesPendingChanges](nsfetchrequest/includespendingchanges.md) — A Boolean value that indicates whether, when the fetch is executed, it matches against currently unsaved changes in the managed object context.
- [propertiesToFetch](nsfetchrequest/propertiestofetch.md) — A collection of either property descriptions or string property names that specify which properties should be returned by the fetch.
- [returnsDistinctResults](nsfetchrequest/returnsdistinctresults.md) — A Boolean value that indicates whether the fetch request returns only distinct values for the fields specified by [propertiesToFetch](nsfetchrequest/propertiestofetch.md).
- [includesPropertyValues](nsfetchrequest/includespropertyvalues.md) — A Boolean value that indicates whether, when the fetch is executed, property data is obtained from the persistent store.
- [shouldRefreshRefetchedObjects](nsfetchrequest/shouldrefreshrefetchedobjects.md) — A Boolean value that indicates whether the property values of fetched objects will be updated with the current values in the persistent store.
- [returnsObjectsAsFaults](nsfetchrequest/returnsobjectsasfaults.md) — A Boolean value that indicates whether the objects resulting from a fetch request are faults.
- [NSFetchRequestResultType](nsfetchrequestresulttype.md) — Constants that specify the possible result types a fetch request can return.
