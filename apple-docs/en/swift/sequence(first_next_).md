---
title: 'sequence(first:next:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/sequence(first:next:)'
source_url: 'https://developer.apple.com/documentation/swift/sequence(first:next:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sequence%28first%3Anext%3A%29.json'
content_hash: 'sha256:794da8fef9d64285'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# sequence(first:next:)

<sub>Function</sub>

Returns a sequence formed from `first` and repeated lazy applications of `next`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sequence<T>(first: T, next: @escaping (T) -> T?) -> UnfoldFirstSequence<T>
```

## Parameters

- `first` — The first element to be returned from the sequence.

- `next` — A closure that accepts the previous sequence element and returns the next element.

## Return Value

A sequence that starts with `first` and continues with every value returned by passing the previous element to `next`.

## Discussion

The first element in the sequence is always `first`, and each successive element is the result of invoking `next` with the previous element. The sequence ends when `next` returns `nil`. If `next` never returns `nil`, the sequence is infinite.

This function can be used to replace many cases that were previously handled using C-style `for` loops.

Example:

```swift
// Walk the elements of a tree from a node up to the root
for node in sequence(first: leaf, next: { $0.parent }) {
  // node is leaf, then leaf.parent, then leaf.parent.parent, etc.
}

// Iterate over all powers of two (ignoring overflow)
for value in sequence(first: 1, next: { $0 * 2 }) {
  // value is 1, then 2, then 4, then 8, etc.
}
```

## See Also

### Dynamic Sequences

- [sequence(state:next:)](<sequence(state_next_).md>) — Returns a sequence formed from repeated lazy applications of `next` to a mutable `state`.
