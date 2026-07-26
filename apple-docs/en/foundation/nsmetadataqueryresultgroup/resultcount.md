---
title: resultCount
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmetadataqueryresultgroup/resultcount
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup/resultcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataqueryresultgroup/resultcount.json'
content_hash: 'sha256:5382ed6e0da2cd6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMetadataQueryResultGroup](../nsmetadataqueryresultgroup.md)

# resultCount

<sub>Instance Property</sub>

The number of results returned by the result group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var resultCount: Int { get }
```

## Discussion

For performance reasons, you should use this property rather than checking the `count` property on [results](results.md).

## See Also

### Getting Query Results

- [attribute](attribute.md) — The result group’s attribute name.
- [value](value.md) — The result group’s value.
- [results](results.md) — An array containing the result group’s result objects.
- [- resultAtIndex:](<result(at_).md>) — Returns the query result at a specific index.
- [subgroups](subgroups.md) — An array containing the result group’s subgroups.
