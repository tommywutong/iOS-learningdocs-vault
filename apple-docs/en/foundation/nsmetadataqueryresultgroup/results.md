---
title: results
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmetadataqueryresultgroup/results
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup/results'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataqueryresultgroup/results.json'
content_hash: 'sha256:bcd07d6df8478d29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMetadataQueryResultGroup](../nsmetadataqueryresultgroup.md)

# results

<sub>Instance Property</sub>

An array containing the result group’s result objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var results: [Any] { get }
```

## Discussion

The results array is a proxy object that is primarily intended for use with Cocoa bindings. While it is possible to copy the proxy array to get a “snapshot” of the complete current query results, it is generally not recommended due to performance and memory issues. To access individual result array elements you should instead use the [resultCount](resultcount.md) property and the [- resultAtIndex:](<result(at_).md>) method.

## See Also

### Getting Query Results

- [attribute](attribute.md) — The result group’s attribute name.
- [value](value.md) — The result group’s value.
- [resultCount](resultcount.md) — The number of results returned by the result group.
- [- resultAtIndex:](<result(at_).md>) — Returns the query result at a specific index.
- [subgroups](subgroups.md) — An array containing the result group’s subgroups.
