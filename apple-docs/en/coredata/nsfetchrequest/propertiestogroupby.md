---
title: propertiesToGroupBy
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchrequest/propertiestogroupby
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchrequest/propertiestogroupby'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchrequest/propertiestogroupby.json'
content_hash: 'sha256:29e4ed7c49c78edf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchRequest](../nsfetchrequest.md)

# propertiesToGroupBy

<sub>Instance Property</sub>

An array of objects that indicates how data should be grouped before a select statement is run in a SQL database.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var propertiesToGroupBy: [Any]? { get set }
```

## Discussion

An array of [NSPropertyDescription](../nspropertydescription.md) or  [NSExpressionDescription](../nsexpressiondescription.md) objects or key-path strings that indicate how data should be grouped before a select statement is run in an SQL database.

If you use this setting, you must set the [resultType](resulttype.md) to [NSDictionaryResultType](../nsfetchrequestresulttype/dictionaryresulttype.md), and the SELECT values must be literals, aggregates, or columns specified in `propertiesToGroupBy`.

Aggregates will operate on the groups specified in `propertiesToGroupBy`

rather than the whole table. If you set `propertiesToGroupBy`, you can also set a predicate to filter rows that are returned by `propertiesToGroupBy`.

See [havingPredicate](havingpredicate.md).

## See Also

### Grouping and Filtering Dictionary Results

- [havingPredicate](havingpredicate.md) — The predicate used to filter rows being returned by a query containing a GROUP BY directive.
