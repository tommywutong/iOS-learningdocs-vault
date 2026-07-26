---
title: 'prefix(upTo:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/substring/utf8view/prefix(upto:)'
source_url: 'https://developer.apple.com/documentation/swift/substring/utf8view/prefix(upto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/utf8view/prefix%28upto%3A%29.json'
content_hash: 'sha256:edd9f0d21a885ba0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Substring](../../substring.md) · [UTF8View](../utf8view.md)

# prefix(upTo:)

<sub>Instance Method</sub>

Returns a subsequence from the start of the collection up to, but not including, the specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func prefix(upTo end: Self.Index) -> Self.SubSequence
```

## Parameters

- `end` — The “past the end” index of the resulting subsequence. `end` must be a valid index of the collection.

## Return Value

A subsequence up to, but not including, the `end` position.

## Discussion

The resulting subsequence _does not include_ the element at the position `end`. The following example searches for the index of the number `40` in an array of integers, and then prints the prefix of the array up to, but not including, that index:

```swift
let numbers = [10, 20, 30, 40, 50, 60]
if let i = numbers.firstIndex(of: 40) {
    print(numbers.prefix(upTo: i))
}
// Prints "[10, 20, 30]"
```

Passing the collection’s starting index as the `end` parameter results in an empty subsequence.

```swift
print(numbers.prefix(upTo: numbers.startIndex))
// Prints "[]"
```

Using the `prefix(upTo:)` method is equivalent to using a partial half-open range as the collection’s subscript. The subscript notation is preferred over `prefix(upTo:)`.

```swift
if let i = numbers.firstIndex(of: 40) {
    print(numbers[..<i])
}
// Prints "[10, 20, 30]"
```

> [!abstract] Complexity
> O(1)
