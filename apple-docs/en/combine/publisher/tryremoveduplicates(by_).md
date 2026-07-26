---
title: 'tryRemoveDuplicates(by:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/tryremoveduplicates(by:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/tryremoveduplicates(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/tryremoveduplicates%28by%3A%29.json'
content_hash: 'sha256:ce4d78be7834a6eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# tryRemoveDuplicates(by:)

<sub>Instance Method</sub>

Publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tryRemoveDuplicates(by predicate: @escaping (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryRemoveDuplicates<Self>
```

## Parameters

- `predicate` — A closure to evaluate whether two elements are equivalent, for purposes of filtering. Return `true` from this closure to indicate that the second element is a duplicate of the first. If this closure throws an error, the publisher terminates with the thrown error.

## Return Value

A publisher that consumes — rather than publishes — duplicate elements.

## Discussion

Use [tryRemoveDuplicates(by:)](<tryremoveduplicates(by_).md>) to remove repeating elements from an upstream publisher based upon the evaluation of elements using an error-throwing closure you provide. If your closure throws an error, the publisher terminates with the error.

In the example below, the closure provided to [tryRemoveDuplicates(by:)](<tryremoveduplicates(by_).md>) returns `true` when two consecutive elements are equal, thereby filtering out `0`, `1`, `2`, and `3`. However, the closure throws an error when it encounters `4`. The publisher then terminates with this error.

```swift
struct BadValuesError: Error {}
let numbers = [0, 0, 0, 0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
cancellable = numbers.publisher
    .tryRemoveDuplicates { first, second -> Bool in
        if (first == 4 && second == 4) {
            throw BadValuesError()
        }
        return first == second
    }
    .sink(
        receiveCompletion: { print ("\($0)") },
        receiveValue: { print ("\($0)", terminator: " ") }
     )

 // Prints: "0 1 2 3 4 failure(BadValuesError()"
```

## See Also

### Filtering elements

- [filter(_:)](<filter(__).md>) — Republishes all elements that match a provided closure.
- [tryFilter(_:)](<tryfilter(__).md>) — Republishes all elements that match a provided error-throwing closure.
- [compactMap(_:)](<compactmap(__).md>) — Calls a closure with each received element and publishes any returned optional that has a value.
- [tryCompactMap(_:)](<trycompactmap(__).md>) — Calls an error-throwing closure with each received element and publishes any returned optional that has a value.
- [removeDuplicates()](<removeduplicates().md>) — Publishes only elements that don’t match the previous element.
- [removeDuplicates(by:)](<removeduplicates(by_).md>) — Publishes only elements that don’t match the previous element, as evaluated by a provided closure.
- [replaceEmpty(with:)](<replaceempty(with_).md>) — Replaces an empty stream with the provided element.
- [replaceError(with:)](<replaceerror(with_).md>) — Replaces any errors in the stream with the provided element.
