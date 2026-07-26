---
title: 'prefix(while:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/dropwhilesequence/prefix(while:)'
source_url: 'https://developer.apple.com/documentation/swift/dropwhilesequence/prefix(while:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dropwhilesequence/prefix%28while%3A%29.json'
content_hash: 'sha256:b79aaf74768a368b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [DropWhileSequence](../dropwhilesequence.md)

# prefix(while:)

<sub>Instance Method</sub>

Returns a sequence containing the initial, consecutive elements that satisfy the given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func prefix(while predicate: (Self.Element) throws -> Bool) rethrows -> [Self.Element]
```

## Parameters

- `predicate` — A closure that takes an element of the sequence as its argument and returns a Boolean value indicating whether the element should be included in the result.

## Return Value

A sequence of the initial, consecutive elements that satisfy `predicate`.

## Discussion

The following example uses the `prefix(while:)` method to find the positive numbers at the beginning of the `numbers` array. Every element of `numbers` up to, but not including, the first negative value is included in the result.

```swift
let numbers = [3, 7, 4, -2, 9, -6, 10, 1]
let positivePrefix = numbers.prefix(while: { $0 > 0 })
// positivePrefix == [3, 7, 4]
```

If `predicate` matches every element in the sequence, the resulting sequence contains every element of the sequence.

> [!abstract] Complexity
> O(_k_), where _k_ is the length of the result.
