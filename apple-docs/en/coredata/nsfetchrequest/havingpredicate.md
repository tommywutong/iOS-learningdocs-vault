---
title: havingPredicate
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchrequest/havingpredicate
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchrequest/havingpredicate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchrequest/havingpredicate.json'
content_hash: 'sha256:bdf408b58c5c5ff9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchRequest](../nsfetchrequest.md)

# havingPredicate

<sub>Instance Property</sub>

The predicate used to filter rows being returned by a query containing a GROUP BY directive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var havingPredicate: NSPredicate? { get set }
```

## Discussion

If a `havingPredicate` value is supplied, the predicate will be run after. Specifying a `havingPredicate` requires that [propertiesToGroupBy](propertiestogroupby.md) also be specified.

## See Also

### Related Documentation

- [NSFetchRequest](../nsfetchrequest.md) — A description of search criteria used to retrieve data from a persistent store.

### Grouping and Filtering Dictionary Results

- [propertiesToGroupBy](propertiestogroupby.md) — An array of objects that indicates how data should be grouped before a select statement is run in a SQL database.
