---
title: 'sortedArray(comparator:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/sortedarray(comparator:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/sortedarray(comparator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/sortedarray%28comparator%3A%29.json'
content_hash: 'sha256:c0ea493bd6a69bb5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# sortedArray(comparator:)

<sub>Instance Method</sub>

Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sortedArray(comparator cmptr: (Any, Any) -> ComparisonResult) -> [Any]
```

## Parameters

- `cmptr` — A comparator block.

## Return Value

An array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified `cmptr`.

## See Also

### Sorting

- [sortedArrayHint](sortedarrayhint.md) — Analyzes the array and returns a “hint” that speeds the sorting of the array when the hint is supplied to [- sortedArrayUsingFunction:context:hint:](<sortedarray(__context_hint_).md>).
- [- sortedArrayUsingFunction:context:](<sortedarray(__context_).md>) — Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.
- [- sortedArrayUsingFunction:context:hint:](<sortedarray(__context_hint_).md>) — Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.
- [- sortedArrayUsingDescriptors:](<sortedarray(using_)-82wi1.md>) — Returns a copy of the receiving array sorted as specified by a given array of sort descriptors.
- [- sortedArrayUsingSelector:](<sortedarray(using_)-9nhh9.md>) — Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given selector.
- [- sortedArrayWithOptions:usingComparator:](<sortedarray(options_usingcomparator_).md>) — Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.
- [Comparator](../comparator.md) — Defines the signature for a block object used for comparison operations.
