---
title: fetchOffset
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchrequest/fetchoffset
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchrequest/fetchoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchrequest/fetchoffset.json'
content_hash: 'sha256:a94d5fe56d6f250e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchRequest](../nsfetchrequest.md)

# fetchOffset

<sub>Instance Property</sub>

The fetch offset of the fetch request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fetchOffset: Int { get set }
```

## Discussion

The default value is `0`.

This setting allows you to specify an offset at which rows will begin being returned. Effectively, the request skips the specified number of matching entries. For example, given a fetch that typically returns `a, b, c, d`, specifying an offset of 1 will return `b, c, d`, and an offset of 4  will return an empty array. Offsets are ignored in nested requests such as subqueries.

This property can be used to restrict the working set of data.  In combination with [fetchLimit](fetchlimit.md), you can create a subrange of an arbitrary result set.

## See Also

### Specifying Fetch Constraints

- [predicate](predicate.md) — The predicate of the fetch request.
- [fetchLimit](fetchlimit.md) — The fetch limit of the fetch request.
- [fetchBatchSize](fetchbatchsize.md) — The batch size of the objects specified in the fetch request.
- [affectedStores](affectedstores.md) — An array of persistent stores specified for the fetch request.
- [NSFetchRequestExpression](../nsfetchrequestexpression.md) — An expression that evaluates the result of a fetch request on a managed object context.
- [NSExpressionDescription](../nsexpressiondescription.md) — An object that describes an expression to include with a fetch request.
- [NSFetchedPropertyDescription](../nsfetchedpropertydescription.md) — A description object used to define which properties are fetched from Core Data.
