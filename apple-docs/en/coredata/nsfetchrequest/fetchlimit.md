---
title: fetchLimit
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchrequest/fetchlimit
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchrequest/fetchlimit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchrequest/fetchlimit.json'
content_hash: 'sha256:3e6094933cef782d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchRequest](../nsfetchrequest.md)

# fetchLimit

<sub>Instance Property</sub>

The fetch limit of the fetch request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fetchLimit: Int { get set }
```

## Discussion

The fetch limit specifies the maximum number of objects that a request should return when executed.

If you set a fetch limit, the framework makes a best effort to improve efficiency, but does not guarantee it. For every object store except the SQL store, a fetch request executed with a fetch limit in effect simply performs an unlimited fetch and throws away the unasked for rows.

## See Also

### Specifying Fetch Constraints

- [predicate](predicate.md) — The predicate of the fetch request.
- [fetchOffset](fetchoffset.md) — The fetch offset of the fetch request.
- [fetchBatchSize](fetchbatchsize.md) — The batch size of the objects specified in the fetch request.
- [affectedStores](affectedstores.md) — An array of persistent stores specified for the fetch request.
- [NSFetchRequestExpression](../nsfetchrequestexpression.md) — An expression that evaluates the result of a fetch request on a managed object context.
- [NSExpressionDescription](../nsexpressiondescription.md) — An object that describes an expression to include with a fetch request.
- [NSFetchedPropertyDescription](../nsfetchedpropertydescription.md) — A description object used to define which properties are fetched from Core Data.
