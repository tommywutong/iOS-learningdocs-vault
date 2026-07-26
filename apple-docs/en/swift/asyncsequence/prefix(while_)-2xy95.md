---
title: 'prefix(while:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asyncsequence/prefix(while:)-2xy95'
source_url: 'https://developer.apple.com/documentation/swift/asyncsequence/prefix(while:)-2xy95'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncsequence/prefix%28while%3A%29-2xy95.json'
content_hash: 'sha256:62c338a48add02f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncSequence](../asyncsequence.md)

# prefix(while:)

<sub>Instance Method</sub>

Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency func prefix(while predicate: @escaping @Sendable (Self.Element) async -> Bool) rethrows -> AsyncPrefixWhileSequence<Self>
```

## Parameters

- `predicate` — A closure that takes an element as a parameter and returns a Boolean value indicating whether the element should be included in the modified sequence.

## Return Value

An asynchronous sequence of the initial, consecutive elements that satisfy `predicate`.

## Discussion

Use `prefix(while:)` to produce values while elements from the base sequence meet a condition you specify. The modified sequence ends when the predicate closure returns `false`.

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `prefix(while:)` method causes the modified sequence to pass along values so long as they aren’t divisible by `2` and `3`. Upon reaching `6`, the sequence ends:

```swift
let stream = Counter(howHigh: 10)
    .prefix { $0 % 2 != 0 || $0 % 3 != 0 }
for try await number in stream {
    print(number, terminator: " ")
}
// Prints "1 2 3 4 5 "
```

## See Also

### Selecting Elements

- [prefix(_:)](<prefix(__).md>) — Returns an asynchronous sequence, up to the specified maximum length, containing the initial elements of the base asynchronous sequence.
- [AsyncPrefixSequence](../asyncprefixsequence.md) — An asynchronous sequence, up to a specified maximum length, containing the initial elements of a base asynchronous sequence.
- [AsyncPrefixWhileSequence](../asyncprefixwhilesequence.md) — An asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy a given predicate.
- [prefix(while:)](<prefix(while_)-6yp5n.md>) — Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given error-throwing predicate.
- [AsyncThrowingPrefixWhileSequence](../asyncthrowingprefixwhilesequence.md) — An asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given error-throwing predicate.
