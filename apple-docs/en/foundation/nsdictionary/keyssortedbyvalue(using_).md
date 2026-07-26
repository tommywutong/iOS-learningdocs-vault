---
title: 'keysSortedByValue(using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/keyssortedbyvalue(using:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/keyssortedbyvalue(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/keyssortedbyvalue%28using%3A%29.json'
content_hash: 'sha256:51ced78fd6e0d24e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# keysSortedByValue(using:)

<sub>Instance Method</sub>

Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func keysSortedByValue(using comparator: Selector) -> [Any]
```

## Parameters

- `comparator` — A selector that specifies the method to use to compare the values in the dictionary. The `comparator` method should return `NSOrderedAscending` if the dictionary value is smaller than the argument, `NSOrderedDescending` if the dictionary value is larger than the argument, and `NSOrderedSame` if they are equal.

## Return Value

An array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values.

## Discussion

Pairs of dictionary values are compared using the comparison method specified by `comparator`; the `comparator` message is sent to one of the values and has as its single argument the other value from the dictionary.

## See Also

### Related Documentation

- [allKeys](allkeys.md) — A new array containing the dictionary’s keys, or an empty array if the dictionary has no entries.
- [- sortedArrayUsingSelector:](<../nsarray/sortedarray(using_)-9nhh9.md>) — Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given selector.

### Sorting Dictionaries

- [- keysSortedByValueUsingComparator:](<keyssortedbyvalue(comparator_).md>) — Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values using a given comparator block.
- [- keysSortedByValueWithOptions:usingComparator:](<keyssortedbyvalue(options_usingcomparator_).md>) — Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values using a given comparator block and a specified set of options.
