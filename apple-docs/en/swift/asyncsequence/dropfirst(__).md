---
title: 'dropFirst(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asyncsequence/dropfirst(_:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncsequence/dropfirst(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncsequence/dropfirst%28_%3A%29.json'
content_hash: 'sha256:b9577f5dfc9bd071'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncSequence](../asyncsequence.md)

# dropFirst(_:)

<sub>Instance Method</sub>

Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dropFirst(_ count: Int = 1) -> AsyncDropFirstSequence<Self>
```

## Parameters

- `count` — The number of elements to drop from the beginning of the sequence. `count` must be greater than or equal to zero.

## Return Value

An asynchronous sequence that drops the first `count` elements from the base sequence.

## Discussion

Use `dropFirst(_:)` when you want to drop the first _n_ elements from the base sequence and pass through the remaining elements.

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `dropFirst(_:)` method causes the modified sequence to ignore the values `1` through `3`, and instead emit `4` through `10`:

```swift
for await number in Counter(howHigh: 10).dropFirst(3) {
    print(number, terminator: " ")
}
// Prints "4 5 6 7 8 9 10 "
```

If the number of elements to drop exceeds the number of elements in the sequence, the result is an empty sequence.

## See Also

### Excluding Elements

- [AsyncDropFirstSequence](../asyncdropfirstsequence.md) — An asynchronous sequence which omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [drop(while:)](<drop(while_)-9sp3b.md>) — Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.
- [AsyncDropWhileSequence](../asyncdropwhilesequence.md) — An asynchronous sequence which omits elements from the base sequence until a given closure returns false, after which it passes through all remaining elements.
- [drop(while:)](<drop(while_)-67kgo.md>) — Omits elements from the base sequence until a given error-throwing closure returns false, after which it passes through all remaining elements.
- [AsyncThrowingDropWhileSequence](../asyncthrowingdropwhilesequence.md) — An asynchronous sequence which omits elements from the base sequence until a given error-throwing closure returns false, after which it passes through all remaining elements.
- [filter(_:)](<filter(__)-435af.md>) — Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.
- [AsyncFilterSequence](../asyncfiltersequence.md) — An asynchronous sequence that contains, in order, the elements of the base sequence that satisfy a given predicate.
- [filter(_:)](<filter(__)-2cc0l.md>) — Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given error-throwing predicate.
- [AsyncThrowingFilterSequence](../asyncthrowingfiltersequence.md) — An asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given error-throwing predicate.
