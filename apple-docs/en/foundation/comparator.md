---
title: Comparator
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/comparator
source_url: 'https://developer.apple.com/documentation/foundation/comparator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/comparator.json'
content_hash: 'sha256:ca48c037d6dc746d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# Comparator

<sub>Type Alias</sub>

Defines the signature for a block object used for comparison operations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Comparator = (Any, Any) -> ComparisonResult
```

## Discussion

The arguments to the [Block object](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3) are two objects to compare. The block returns an [ComparisonResult](comparisonresult.md) value to denote the ordering of the two objects.

You use `NSComparator` blocks in comparison operations such as `NSArray`’s [- sortedArrayUsingComparator:](<nsarray/sortedarray(comparator_).md>), for example:

```objc
NSArray *sortedArray = [array sortedArrayUsingComparator: ^(id obj1, id obj2) {
 
    if ([obj1 integerValue] > [obj2 integerValue]) {
        return (NSComparisonResult)NSOrderedDescending;
    }
 
    if ([obj1 integerValue] < [obj2 integerValue]) {
        return (NSComparisonResult)NSOrderedAscending;
    }
    return (NSComparisonResult)NSOrderedSame;
}];
```

## See Also

### Sorting

- [sortedArrayHint](nsarray/sortedarrayhint.md) — Analyzes the array and returns a “hint” that speeds the sorting of the array when the hint is supplied to [- sortedArrayUsingFunction:context:hint:](<nsarray/sortedarray(__context_hint_).md>).
- [- sortedArrayUsingFunction:context:](<nsarray/sortedarray(__context_).md>) — Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.
- [- sortedArrayUsingFunction:context:hint:](<nsarray/sortedarray(__context_hint_).md>) — Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.
- [- sortedArrayUsingDescriptors:](<nsarray/sortedarray(using_)-82wi1.md>) — Returns a copy of the receiving array sorted as specified by a given array of sort descriptors.
- [- sortedArrayUsingSelector:](<nsarray/sortedarray(using_)-9nhh9.md>) — Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given selector.
- [- sortedArrayUsingComparator:](<nsarray/sortedarray(comparator_).md>) — Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.
- [- sortedArrayWithOptions:usingComparator:](<nsarray/sortedarray(options_usingcomparator_).md>) — Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.
