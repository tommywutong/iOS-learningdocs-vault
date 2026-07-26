---
title: 'sortedArray(_:context:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/sortedarray(_:context:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/sortedarray(_:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/sortedarray%28_%3Acontext%3A%29.json'
content_hash: 'sha256:7a3bcfc4fe6c1647'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# sortedArray(_:context:)

<sub>Instance Method</sub>

Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sortedArray(_ comparator: (Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?) -> [Any]
```

## Discussion

The new array contains references to the receiving array’s elements, not copies of them.

The comparison function is used to compare two elements at a time and should return `NSOrderedAscending` if the first element is smaller than the second, `NSOrderedDescending` if the first element is larger than the second, and `NSOrderedSame` if the elements are equal. Each time the comparison function is called, it’s passed `context` as its third argument. This allows the comparison to be based on some outside parameter, such as whether character sorting is case-sensitive or case-insensitive.

Given `anArray` (an array of `NSNumber` objects) and a comparison function of this type:

```objc
NSInteger intSort(id num1, id num2, void *context)
{
    int v1 = [num1 intValue];
    int v2 = [num2 intValue];
    if (v1 < v2)
        return NSOrderedAscending;
    else if (v1 > v2)
        return NSOrderedDescending;
    else
        return NSOrderedSame;
}
```

A sorted version of `anArray` is created in this way:

```objc
NSArray *sortedArray; sortedArray = [anArray sortedArrayUsingFunction:intSort context:NULL];
```

## See Also

### Sorting

- [sortedArrayHint](sortedarrayhint.md) — Analyzes the array and returns a “hint” that speeds the sorting of the array when the hint is supplied to [- sortedArrayUsingFunction:context:hint:](<sortedarray(__context_hint_).md>).
- [- sortedArrayUsingFunction:context:hint:](<sortedarray(__context_hint_).md>) — Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.
- [- sortedArrayUsingDescriptors:](<sortedarray(using_)-82wi1.md>) — Returns a copy of the receiving array sorted as specified by a given array of sort descriptors.
- [- sortedArrayUsingSelector:](<sortedarray(using_)-9nhh9.md>) — Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given selector.
- [- sortedArrayUsingComparator:](<sortedarray(comparator_).md>) — Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.
- [- sortedArrayWithOptions:usingComparator:](<sortedarray(options_usingcomparator_).md>) — Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.
- [Comparator](../comparator.md) — Defines the signature for a block object used for comparison operations.
