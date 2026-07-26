---
title: 'prefix(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/prefix(_:)'
source_url: 'https://developer.apple.com/documentation/swift/string/prefix(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/prefix%28_%3A%29.json'
content_hash: 'sha256:8c946e6dea45dcb2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# prefix(_:)

<sub>Instance Method</sub>

Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func prefix(_ maxLength: Int) -> Self.SubSequence
```

## Parameters

- `maxLength` — The maximum number of elements to return. `maxLength` must be greater than or equal to zero.

## Return Value

A subsequence starting at the beginning of this collection with at most `maxLength` elements.

## Discussion

If the maximum length exceeds the number of elements in the collection, the result contains all the elements in the collection.

```swift
let numbers = [1, 2, 3, 4, 5]
print(numbers.prefix(2))
// Prints "[1, 2]"
print(numbers.prefix(10))
// Prints "[1, 2, 3, 4, 5]"
```

> [!abstract] Complexity
> O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(_k_), where _k_ is the number of elements to select from the beginning of the collection.

## See Also

### Getting Substrings

- [subscript(_:)](<subscript(__)-2so14.md>) — Accesses a contiguous subrange of the collection’s elements.
- [subscript(_:)](<subscript(__)-4h7s3.md>) — Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(_:)](<subscript(__)-4al9c.md>)
- [prefix(through:)](<prefix(through_).md>) — Returns a subsequence from the start of the collection through the specified position.
- [prefix(upTo:)](<prefix(upto_).md>) — Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [prefix(while:)](<prefix(while_).md>) — Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [suffix(_:)](<suffix(__).md>) — Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [suffix(from:)](<suffix(from_).md>) — Returns a subsequence from the specified position to the end of the collection.
