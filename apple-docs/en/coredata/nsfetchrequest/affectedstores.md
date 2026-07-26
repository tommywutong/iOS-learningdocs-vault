---
title: affectedStores
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchrequest/affectedstores
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchrequest/affectedstores'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchrequest/affectedstores.json'
content_hash: 'sha256:539f2e151edb619f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchRequest](../nsfetchrequest.md)

# affectedStores

<sub>Instance Property</sub>

An array of persistent stores specified for the fetch request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var affectedStores: [NSPersistentStore]? { get set }
```

## Discussion

The contents of the array are the identifiers for the stores to be searched when the fetch request is executed.

## See Also

### Specifying Fetch Constraints

- [predicate](predicate.md) — The predicate of the fetch request.
- [fetchLimit](fetchlimit.md) — The fetch limit of the fetch request.
- [fetchOffset](fetchoffset.md) — The fetch offset of the fetch request.
- [fetchBatchSize](fetchbatchsize.md) — The batch size of the objects specified in the fetch request.
- [NSFetchRequestExpression](../nsfetchrequestexpression.md) — An expression that evaluates the result of a fetch request on a managed object context.
- [NSExpressionDescription](../nsexpressiondescription.md) — An object that describes an expression to include with a fetch request.
- [NSFetchedPropertyDescription](../nsfetchedpropertydescription.md) — A description object used to define which properties are fetched from Core Data.
