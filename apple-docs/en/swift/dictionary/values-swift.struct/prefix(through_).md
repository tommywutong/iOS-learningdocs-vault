---
title: 'prefix(through:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/dictionary/values-swift.struct/prefix(through:)'
source_url: 'https://developer.apple.com/documentation/swift/dictionary/values-swift.struct/prefix(through:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/values-swift.struct/prefix%28through%3A%29.json'
content_hash: 'sha256:cf3644b2d1777c8a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Dictionary](../../dictionary.md) · [Values](../values-swift.struct.md)

# prefix(through:)

<sub>Instance Method</sub>

Returns a subsequence from the start of the collection through the specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func prefix(through position: Self.Index) -> Self.SubSequence
```

## Parameters

- `position` — The index of the last element to include in the resulting subsequence. `position` must be a valid index of the collection that is not equal to the `endIndex` property.

## Return Value

A subsequence up to, and including, the given position.

## Discussion

The resulting subsequence _includes_ the element at the position specified by the `through` parameter. The following example searches for the index of the number `40` in an array of integers, and then prints the prefix of the array up to, and including, that index:

```swift
let numbers = [10, 20, 30, 40, 50, 60]
if let i = numbers.firstIndex(of: 40) {
    print(numbers.prefix(through: i))
}
// Prints "[10, 20, 30, 40]"
```

Using the `prefix(through:)` method is equivalent to using a partial closed range as the collection’s subscript. The subscript notation is preferred over `prefix(through:)`.

```swift
if let i = numbers.firstIndex(of: 40) {
    print(numbers[...i])
}
// Prints "[10, 20, 30, 40]"
```

> [!abstract] Complexity
> O(1)
