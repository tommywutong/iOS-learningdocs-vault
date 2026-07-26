---
title: 'filter(using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablearray/filter(using:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablearray/filter(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablearray/filter%28using%3A%29.json'
content_hash: 'sha256:002e5e05b40d0f54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableArray](../nsmutablearray.md)

# filter(using:)

<sub>Instance Method</sub>

Evaluates a given predicate against the array’s content and leaves only objects that match.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func filter(using predicate: NSPredicate)
```

## Parameters

- `predicate` — The predicate to evaluate against the array’s elements.

## See Also

### Related Documentation

- [- filteredArrayUsingPredicate:](<../nsarray/filtered(using_).md>) — Evaluates a given predicate against each object in the receiving array and returns a new array containing the objects for which the predicate returns true.
