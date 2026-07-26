---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/subscript(_:)-4h7s3'
source_url: 'https://developer.apple.com/documentation/swift/string/subscript(_:)-4h7s3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/subscript%28_%3A%29-4h7s3.json'
content_hash: 'sha256:9fe35b3afffb8c4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the contiguous subrange of the collection’s elements specified by a range expression.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<R>(r: R) -> Self.SubSequence where R : RangeExpression, Self.Index == R.Bound { get }
```

## Overview

The range expression is converted to a concrete subrange relative to this collection. For example, using a `PartialRangeFrom` range expression with an array accesses the subrange from the start of the range expression until the end of the array.

```swift
let streets = ["Adams", "Bryant", "Channing", "Douglas", "Evarts"]
let streetsSlice = streets[2...]
print(streetsSlice)
// ["Channing", "Douglas", "Evarts"]
```

The accessed slice uses the same indices for the same elements as the original collection uses. This example searches `streetsSlice` for one of the strings in the slice, and then uses that index in the original array.

```swift
let index = streetsSlice.firstIndex(of: "Evarts")    // 4
print(streets[index!])
// "Evarts"
```

Always use the slice’s `startIndex` property instead of assuming that its indices start at a particular value. Attempting to access an element by using an index outside the bounds of the slice’s indices may result in a runtime error, even if that index is valid for the original collection.

```swift
print(streetsSlice.startIndex)
// 2
print(streetsSlice[2])
// "Channing"

print(streetsSlice[0])
// error: Index out of bounds
```

> [!abstract] Complexity
> O(1)

## See Also

### Getting Substrings

- [subscript(_:)](<subscript(__)-2so14.md>) — Accesses a contiguous subrange of the collection’s elements.
- [subscript(_:)](<subscript(__)-4al9c.md>)
- [prefix(_:)](<prefix(__).md>) — Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [prefix(through:)](<prefix(through_).md>) — Returns a subsequence from the start of the collection through the specified position.
- [prefix(upTo:)](<prefix(upto_).md>) — Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [prefix(while:)](<prefix(while_).md>) — Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [suffix(_:)](<suffix(__).md>) — Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [suffix(from:)](<suffix(from_).md>) — Returns a subsequence from the specified position to the end of the collection.
