---
title: predicate
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchrequest/predicate
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchrequest/predicate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchrequest/predicate.json'
content_hash: 'sha256:ac16aa5d8f373794'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchRequest](../nsfetchrequest.md)

# predicate

<sub>Instance Property</sub>

The predicate of the fetch request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var predicate: NSPredicate? { get set }
```

## Discussion

The predicate instance constrains the selection of objects the [NSFetchRequest](../nsfetchrequest.md) instance is to fetch.

If the predicate is empty—for example, if it is an `AND` predicate whose array of elements contains no predicates—the request has its predicate set to `nil`. For more about predicates, see [Predicate Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html#//apple_ref/doc/uid/TP40001789).

## See Also

### Specifying Fetch Constraints

- [fetchLimit](fetchlimit.md) — The fetch limit of the fetch request.
- [fetchOffset](fetchoffset.md) — The fetch offset of the fetch request.
- [fetchBatchSize](fetchbatchsize.md) — The batch size of the objects specified in the fetch request.
- [affectedStores](affectedstores.md) — An array of persistent stores specified for the fetch request.
- [NSFetchRequestExpression](../nsfetchrequestexpression.md) — An expression that evaluates the result of a fetch request on a managed object context.
- [NSExpressionDescription](../nsexpressiondescription.md) — An object that describes an expression to include with a fetch request.
- [NSFetchedPropertyDescription](../nsfetchedpropertydescription.md) — A description object used to define which properties are fetched from Core Data.
