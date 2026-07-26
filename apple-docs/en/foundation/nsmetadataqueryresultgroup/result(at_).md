---
title: 'result(at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmetadataqueryresultgroup/result(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup/result(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataqueryresultgroup/result%28at%3A%29.json'
content_hash: 'sha256:d8392c74fe6096d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMetadataQueryResultGroup](../nsmetadataqueryresultgroup.md)

# result(at:)

<sub>Instance Method</sub>

Returns the query result at a specific index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func result(at idx: Int) -> Any
```

## Parameters

- `idx` — The index of the desired result.

## Return Value

The query result at a specific index.

## Discussion

For performance reasons, you should use this method when retrieving a specific result, rather than they array contained in [results](results.md).

## See Also

### Getting Query Results

- [attribute](attribute.md) — The result group’s attribute name.
- [value](value.md) — The result group’s value.
- [results](results.md) — An array containing the result group’s result objects.
- [resultCount](resultcount.md) — The number of results returned by the result group.
- [subgroups](subgroups.md) — An array containing the result group’s subgroups.
