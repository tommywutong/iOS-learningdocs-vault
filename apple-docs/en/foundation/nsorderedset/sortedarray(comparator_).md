---
title: 'sortedArray(comparator:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedset/sortedarray(comparator:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/sortedarray(comparator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/sortedarray%28comparator%3A%29.json'
content_hash: 'sha256:69614971e84a6af0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# sortedArray(comparator:)

<sub>Instance Method</sub>

Returns an array that lists the receiving ordered set’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sortedArray(comparator cmptr: (Any, Any) -> ComparisonResult) -> [Any]
```

## Parameters

- `cmptr` — A comparator block.

## Return Value

An array that lists the receiving ordered set’s elements in ascending order, as determined by the comparison method specified `cmptr`.

## See Also

### Creating a Sorted Array

- [- sortedArrayUsingDescriptors:](<sortedarray(using_).md>) — Returns an array of the ordered set’s elements sorted as specified by a given array of sort descriptors.
- [- sortedArrayWithOptions:usingComparator:](<sortedarray(options_usingcomparator_).md>) — Returns an array that lists the receiving ordered set’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.
