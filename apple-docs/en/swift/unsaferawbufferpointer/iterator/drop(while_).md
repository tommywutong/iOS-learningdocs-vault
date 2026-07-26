---
title: 'drop(while:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsaferawbufferpointer/iterator/drop(while:)'
source_url: 'https://developer.apple.com/documentation/swift/unsaferawbufferpointer/iterator/drop(while:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsaferawbufferpointer/iterator/drop%28while%3A%29.json'
content_hash: 'sha256:e52b23c04deeb2f4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [UnsafeRawBufferPointer](../../unsaferawbufferpointer.md) · [Iterator](../iterator.md)

# drop(while:)

<sub>Instance Method</sub>

Returns a sequence by skipping the initial, consecutive elements that satisfy the given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func drop(while predicate: (Self.Element) throws -> Bool) rethrows -> DropWhileSequence<Self>
```

## Parameters

- `predicate` — A closure that takes an element of the sequence as its argument and returns a Boolean value indicating whether the element should be included in the result.

## Return Value

A sequence starting after the initial, consecutive elements that satisfy `predicate`.

## Discussion

The following example uses the `drop(while:)` method to skip over the positive numbers at the beginning of the `numbers` array. The result begins with the first element of `numbers` that does not satisfy `predicate`.

```swift
let numbers = [3, 7, 4, -2, 9, -6, 10, 1]
let startingWithNegative = numbers.drop(while: { $0 > 0 })
// startingWithNegative == [-2, 9, -6, 10, 1]
```

If `predicate` matches every element in the sequence, the result is an empty sequence.

> [!abstract] Complexity
> O(_k_), where _k_ is the number of elements to drop from the beginning of the sequence.
