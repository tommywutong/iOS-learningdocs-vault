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
doc_path: '/documentation/swift/asyncsequence/prefix(while:)-6yp5n'
source_url: 'https://developer.apple.com/documentation/swift/asyncsequence/prefix(while:)-6yp5n'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncsequence/prefix%28while%3A%29-6yp5n.json'
content_hash: 'sha256:d8b6af29e2ec8da5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncSequence](../asyncsequence.md)

# prefix(while:)

<sub>Instance Method</sub>

Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given error-throwing predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency func prefix(while predicate: @escaping @Sendable (Self.Element) async throws -> Bool) rethrows -> AsyncThrowingPrefixWhileSequence<Self>
```

## Parameters

- `predicate` — A error-throwing closure that takes an element of the asynchronous sequence as its argument and returns a Boolean value that indicates whether to include the element in the modified sequence.

## Return Value

An asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate. If the predicate throws an error, the sequence contains only values produced prior to the error.

## Discussion

Use `prefix(while:)` to produce values while elements from the base sequence meet a condition you specify. The modified sequence ends when the predicate closure returns `false` or throws an error.

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `prefix(_:)` method causes the modified sequence to pass through values less than `8`, but throws an error when it receives a value that’s divisible by `5`:

```swift
do {
    let stream = try Counter(howHigh: 10)
        .prefix {
            if $0 % 5 == 0 {
                throw MyError()
            }
            return $0 < 8
        }
    for try await number in stream {
        print(number, terminator: " ")
    }
} catch {
    print("Error: \(error)")
}
// Prints "1 2 3 4 Error: MyError() "
```

## See Also

### Selecting Elements

- [prefix(_:)](<prefix(__).md>) — Returns an asynchronous sequence, up to the specified maximum length, containing the initial elements of the base asynchronous sequence.
- [AsyncPrefixSequence](../asyncprefixsequence.md) — An asynchronous sequence, up to a specified maximum length, containing the initial elements of a base asynchronous sequence.
- [prefix(while:)](<prefix(while_)-2xy95.md>) — Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given predicate.
- [AsyncPrefixWhileSequence](../asyncprefixwhilesequence.md) — An asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy a given predicate.
- [AsyncThrowingPrefixWhileSequence](../asyncthrowingprefixwhilesequence.md) — An asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given error-throwing predicate.
