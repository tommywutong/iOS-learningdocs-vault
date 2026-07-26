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
doc_path: '/documentation/swift/asyncthrowingfiltersequence/drop(while:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingfiltersequence/drop(while:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingfiltersequence/drop%28while%3A%29.json'
content_hash: 'sha256:eecbf266672cfeee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncThrowingFilterSequence](../asyncthrowingfiltersequence.md)

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
