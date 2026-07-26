---
title: 'keysSortedByValue(comparator:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/keyssortedbyvalue(comparator:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/keyssortedbyvalue(comparator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/keyssortedbyvalue%28comparator%3A%29.json'
content_hash: 'sha256:42e02e7c10cee41b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# keysSortedByValue(comparator:)

<sub>Instance Method</sub>

Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values using a given comparator block.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func keysSortedByValue(comparator cmptr: (Any, Any) -> ComparisonResult) -> [Any]
```

## Parameters

- `cmptr` — A comparator block.

## Return Value

An array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values using `cmptr`.

## See Also

### Sorting Dictionaries

- [- keysSortedByValueUsingSelector:](<keyssortedbyvalue(using_).md>) — Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values.
- [- keysSortedByValueWithOptions:usingComparator:](<keyssortedbyvalue(options_usingcomparator_).md>) — Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values using a given comparator block and a specified set of options.
