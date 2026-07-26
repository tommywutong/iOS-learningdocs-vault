---
title: 'suffix(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/lazydropwhilesequence/suffix(_:)'
source_url: 'https://developer.apple.com/documentation/swift/lazydropwhilesequence/suffix(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazydropwhilesequence/suffix%28_%3A%29.json'
content_hash: 'sha256:e8e69c71ba263f52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazyDropWhileSequence](../lazydropwhilesequence.md)

# suffix(_:)

<sub>Instance Method</sub>

Returns a subsequence, up to the given maximum length, containing the final elements of the sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func suffix(_ maxLength: Int) -> [Self.Element]
```

## Parameters

- `maxLength` — The maximum number of elements to return. The value of `maxLength` must be greater than or equal to zero.

## Discussion

The sequence must be finite. If the maximum length exceeds the number of elements in the sequence, the result contains all the elements in the sequence.

```swift
let numbers = [1, 2, 3, 4, 5]
print(numbers.suffix(2))
// Prints "[4, 5]"
print(numbers.suffix(10))
// Prints "[1, 2, 3, 4, 5]"
```

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the sequence.
