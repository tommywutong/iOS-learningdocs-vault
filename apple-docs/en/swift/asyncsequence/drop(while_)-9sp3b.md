---
title: 'drop(while:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asyncsequence/drop(while:)-9sp3b'
source_url: 'https://developer.apple.com/documentation/swift/asyncsequence/drop(while:)-9sp3b'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncsequence/drop%28while%3A%29-9sp3b.json'
content_hash: 'sha256:64235d97de2c3f2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncSequence](../asyncsequence.md)

# drop(while:)

<sub>Instance Method</sub>

Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency func drop(while predicate: @escaping @Sendable (Self.Element) async -> Bool) -> AsyncDropWhileSequence<Self>
```

## Parameters

- `predicate` — A closure that takes an element as a parameter and returns a Boolean value indicating whether to drop the element from the modified sequence.

## Return Value

An asynchronous sequence that skips over values from the base sequence until the provided closure returns `false`.

## Discussion

Use `drop(while:)` to omit elements from an asynchronous sequence until the element received meets a condition you specify.

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `drop(while:)` method causes the modified sequence to ignore received values until it encounters one that is divisible by `3`:

```swift
let stream = Counter(howHigh: 10)
    .drop { $0 % 3 != 0 }
for await number in stream {
    print(number, terminator: " ")
}
// Prints "3 4 5 6 7 8 9 10 "
```

After the predicate returns `false`, the sequence never executes it again, and from then on the sequence passes through elements from its underlying sequence as-is.

## See Also

### Excluding Elements

- [dropFirst(_:)](<dropfirst(__).md>) — Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [AsyncDropFirstSequence](../asyncdropfirstsequence.md) — An asynchronous sequence which omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [AsyncDropWhileSequence](../asyncdropwhilesequence.md) — An asynchronous sequence which omits elements from the base sequence until a given closure returns false, after which it passes through all remaining elements.
- [drop(while:)](<drop(while_)-67kgo.md>) — Omits elements from the base sequence until a given error-throwing closure returns false, after which it passes through all remaining elements.
- [AsyncThrowingDropWhileSequence](../asyncthrowingdropwhilesequence.md) — An asynchronous sequence which omits elements from the base sequence until a given error-throwing closure returns false, after which it passes through all remaining elements.
- [filter(_:)](<filter(__)-435af.md>) — Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.
- [AsyncFilterSequence](../asyncfiltersequence.md) — An asynchronous sequence that contains, in order, the elements of the base sequence that satisfy a given predicate.
- [filter(_:)](<filter(__)-2cc0l.md>) — Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given error-throwing predicate.
- [AsyncThrowingFilterSequence](../asyncthrowingfiltersequence.md) — An asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given error-throwing predicate.
