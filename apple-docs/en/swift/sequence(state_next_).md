---
title: 'sequence(state:next:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/sequence(state:next:)'
source_url: 'https://developer.apple.com/documentation/swift/sequence(state:next:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sequence%28state%3Anext%3A%29.json'
content_hash: 'sha256:0136d7170bd13d3c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# sequence(state:next:)

<sub>Function</sub>

Returns a sequence formed from repeated lazy applications of `next` to a mutable `state`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sequence<T, State>(state: State, next: @escaping (inout State) -> T?) -> UnfoldSequence<T, State>
```

## Parameters

- `state` — The initial state that will be passed to the closure.

- `next` — A closure that accepts an `inout` state and returns the next element of the sequence.

## Return Value

A sequence that yields each successive value from `next`.

## Discussion

The elements of the sequence are obtained by invoking `next` with a mutable state. The same state is passed to all invocations of `next`, so subsequent calls will see any mutations made by previous calls. The sequence ends when `next` returns `nil`. If `next` never returns `nil`, the sequence is infinite.

This function can be used to replace many instances of `AnyIterator` that wrap a closure.

Example:

```swift
// Interleave two sequences that yield the same element type
sequence(state: (false, seq1.makeIterator(), seq2.makeIterator()), next: { iters in
  iters.0 = !iters.0
  return iters.0 ? iters.1.next() : iters.2.next()
})
```

## See Also

### Dynamic Sequences

- [sequence(first:next:)](<sequence(first_next_).md>) — Returns a sequence formed from `first` and repeated lazy applications of `next`.
