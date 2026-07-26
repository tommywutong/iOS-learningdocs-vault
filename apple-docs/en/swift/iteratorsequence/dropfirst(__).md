---
title: 'dropFirst(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/iteratorsequence/dropfirst(_:)'
source_url: 'https://developer.apple.com/documentation/swift/iteratorsequence/dropfirst(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/iteratorsequence/dropfirst%28_%3A%29.json'
content_hash: 'sha256:8e6d6a92eaf2d097'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [IteratorSequence](../iteratorsequence.md)

# dropFirst(_:)

<sub>Instance Method</sub>

Returns a sequence containing all but the given number of initial elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dropFirst(_ k: Int = 1) -> DropFirstSequence<Self>
```

## Parameters

- `k` — The number of elements to drop from the beginning of the sequence. `k` must be greater than or equal to zero.

## Return Value

A sequence starting after the specified number of elements.

## Discussion

If the number of elements to drop exceeds the number of elements in the sequence, the result is an empty sequence.

```swift
let numbers = [1, 2, 3, 4, 5]
print(numbers.dropFirst(2))
// Prints "[3, 4, 5]"
print(numbers.dropFirst(10))
// Prints "[]"
```

> [!abstract] Complexity
> O(1), with O(_k_) deferred to each iteration of the result, where _k_ is the number of elements to drop from the beginning of the sequence.
