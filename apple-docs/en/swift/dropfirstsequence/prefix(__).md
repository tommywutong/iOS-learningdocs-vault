---
title: 'prefix(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/dropfirstsequence/prefix(_:)'
source_url: 'https://developer.apple.com/documentation/swift/dropfirstsequence/prefix(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dropfirstsequence/prefix%28_%3A%29.json'
content_hash: 'sha256:90805ef83c247cde'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [DropFirstSequence](../dropfirstsequence.md)

# prefix(_:)

<sub>Instance Method</sub>

Returns a sequence, up to the specified maximum length, containing the initial elements of the sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func prefix(_ maxLength: Int) -> PrefixSequence<Self>
```

## Parameters

- `maxLength` — The maximum number of elements to return. The value of `maxLength` must be greater than or equal to zero.

## Return Value

A sequence starting at the beginning of this sequence with at most `maxLength` elements.

## Discussion

If the maximum length exceeds the number of elements in the sequence, the result contains all the elements in the sequence.

```swift
let numbers = [1, 2, 3, 4, 5]
print(numbers.prefix(2))
// Prints "[1, 2]"
print(numbers.prefix(10))
// Prints "[1, 2, 3, 4, 5]"
```

> [!abstract] Complexity
> O(1)
