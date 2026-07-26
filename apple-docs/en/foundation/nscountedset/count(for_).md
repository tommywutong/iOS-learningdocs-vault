---
title: 'count(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscountedset/count(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscountedset/count(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscountedset/count%28for%3A%29.json'
content_hash: 'sha256:1e6f1c6dac92acce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCountedSet](../nscountedset.md)

# count(for:)

<sub>Instance Method</sub>

Returns the count associated with a given object in the set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func count(for object: Any) -> Int
```

## Parameters

- `object` — The object for which to return the count.

## Return Value

The count associated with `object` in the set, which can be thought of as the number of occurrences of `object` present in the set.

## See Also

### Related Documentation

- [count](../nsset/count.md) — The number of members in the set.

### Examining a Counted Set

- [- objectEnumerator](<objectenumerator().md>) — Returns an enumerator object that lets you access each object in the set once, independent of its count.
