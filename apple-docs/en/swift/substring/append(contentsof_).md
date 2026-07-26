---
title: 'append(contentsOf:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/substring/append(contentsof:)'
source_url: 'https://developer.apple.com/documentation/swift/substring/append(contentsof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/append%28contentsof%3A%29.json'
content_hash: 'sha256:3a75a71acb98f198'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Substring](../substring.md)

# append(contentsOf:)

<sub>Instance Method</sub>

Adds the elements of a sequence or collection to the end of this collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func append<S>(contentsOf elements: S) where S : Sequence, S.Element == Character
```

## Discussion

The collection being appended to allocates any additional necessary storage to hold the new elements.

The following example appends the elements of a `Range<Int>` instance to an array of integers:

```swift
var numbers = [1, 2, 3, 4, 5]
numbers.append(contentsOf: 10...15)
print(numbers)
// Prints "[1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15]"
```

> [!abstract] Complexity
> O(_m_), where _m_ is the length of `newElements`.
