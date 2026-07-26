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
doc_path: '/documentation/swift/unsaferawbufferpointer/suffix(_:)'
source_url: 'https://developer.apple.com/documentation/swift/unsaferawbufferpointer/suffix(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsaferawbufferpointer/suffix%28_%3A%29.json'
content_hash: 'sha256:7b156170f970667f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeRawBufferPointer](../unsaferawbufferpointer.md)

# suffix(_:)

<sub>Instance Method</sub>

Returns a subsequence, up to the given maximum length, containing the final elements of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func suffix(_ maxLength: Int) -> Self.SubSequence
```

## Parameters

- `maxLength` — The maximum number of elements to return. `maxLength` must be greater than or equal to zero.

## Return Value

A subsequence terminating at the end of the collection with at most `maxLength` elements.

## Discussion

If the maximum length exceeds the number of elements in the collection, the result contains the entire collection.

```swift
let numbers = [1, 2, 3, 4, 5]
print(numbers.suffix(2))
// Prints "[4, 5]"
print(numbers.suffix(10))
// Prints "[1, 2, 3, 4, 5]"
```

> [!abstract] Complexity
> O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(_k_), where _k_ is equal to `maxLength`.
