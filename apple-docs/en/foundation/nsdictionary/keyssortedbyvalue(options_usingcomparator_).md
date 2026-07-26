---
title: 'keysSortedByValue(options:usingComparator:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/keyssortedbyvalue(options:usingcomparator:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/keyssortedbyvalue(options:usingcomparator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/keyssortedbyvalue%28options%3Ausingcomparator%3A%29.json'
content_hash: 'sha256:84dff5363ce24b28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# keysSortedByValue(options:usingComparator:)

<sub>Instance Method</sub>

Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values using a given comparator block and a specified set of options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func keysSortedByValue(options opts: NSSortOptions = [], usingComparator cmptr: (Any, Any) -> ComparisonResult) -> [Any]
```

## Parameters

- `opts` — A bitmask of sort options.

- `cmptr` — A comparator block.

## Return Value

An array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values using `cmptr` with the options given in `opts`.

## See Also

### Sorting Dictionaries

- [- keysSortedByValueUsingSelector:](<keyssortedbyvalue(using_).md>) — Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values.
- [- keysSortedByValueUsingComparator:](<keyssortedbyvalue(comparator_).md>) — Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values using a given comparator block.
