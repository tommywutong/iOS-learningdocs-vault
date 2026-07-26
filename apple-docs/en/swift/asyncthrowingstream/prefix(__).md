---
title: 'prefix(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asyncthrowingstream/prefix(_:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingstream/prefix(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingstream/prefix%28_%3A%29.json'
content_hash: 'sha256:1c0d2457b8ded177'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncThrowingStream](../asyncthrowingstream.md)

# prefix(_:)

<sub>Instance Method</sub>

Returns an asynchronous sequence, up to the specified maximum length, containing the initial elements of the base asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func prefix(_ count: Int) -> AsyncPrefixSequence<Self>
```

## Parameters

- `count` — The maximum number of elements to return. The value of `count` must be greater than or equal to zero.

## Return Value

An asynchronous sequence starting at the beginning of the base sequence with at most `count` elements.

## Discussion

Use `prefix(_:)` to reduce the number of elements produced by the asynchronous sequence.

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `prefix(_:)` method causes the modified sequence to pass through the first six values, then end.

```swift
for await number in Counter(howHigh: 10).prefix(6) {
    print(number, terminator: " ")
}
// Prints "1 2 3 4 5 6 "
```

If the count passed to `prefix(_:)` exceeds the number of elements in the base sequence, the result contains all of the elements in the sequence.

## See Also

### Selecting Elements

- [prefix(while:)](<prefix(while_).md>) — Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given predicate.
