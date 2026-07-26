---
title: 'tryFilter(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/tryfilter(_:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/tryfilter(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/tryfilter%28_%3A%29.json'
content_hash: 'sha256:62d8ed8894632166'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# tryFilter(_:)

<sub>Instance Method</sub>

Republishes all elements that match a provided error-throwing closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tryFilter(_ isIncluded: @escaping (Self.Output) throws -> Bool) -> Publishers.TryFilter<Self>
```

## Parameters

- `isIncluded` — A closure that takes one element and returns a Boolean value that indicated whether to republish the element or throws an error.

## Return Value

A publisher that republishes all elements that satisfy the closure.

## Discussion

Use [tryFilter(_:)](<tryfilter(__).md>) to filter elements evaluated in an error-throwing closure. If the `isIncluded` closure throws an error, the publisher fails with that error.

In the example below, [tryFilter(_:)](<tryfilter(__).md>) checks to see if the element provided by the publisher is zero, and throws a `ZeroError` before terminating the publisher with the thrown error. Otherwise, it republishes the element only if it’s even:

```swift
struct ZeroError: Error {}

let numbers: [Int] = [1, 2, 3, 4, 0, 5]
cancellable = numbers.publisher
    .tryFilter{
        if $0 == 0 {
            throw ZeroError()
        } else {
            return $0 % 2 == 0
        }
    }
    .sink(
        receiveCompletion: { print ("\($0)") },
        receiveValue: { print ("\($0)", terminator: " ") }
     )

// Prints: "2 4 failure(DivisionByZeroError())".
```

## See Also

### Filtering elements

- [filter(_:)](<filter(__).md>) — Republishes all elements that match a provided closure.
- [compactMap(_:)](<compactmap(__).md>) — Calls a closure with each received element and publishes any returned optional that has a value.
- [tryCompactMap(_:)](<trycompactmap(__).md>) — Calls an error-throwing closure with each received element and publishes any returned optional that has a value.
- [removeDuplicates()](<removeduplicates().md>) — Publishes only elements that don’t match the previous element.
- [removeDuplicates(by:)](<removeduplicates(by_).md>) — Publishes only elements that don’t match the previous element, as evaluated by a provided closure.
- [tryRemoveDuplicates(by:)](<tryremoveduplicates(by_).md>) — Publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [replaceEmpty(with:)](<replaceempty(with_).md>) — Replaces an empty stream with the provided element.
- [replaceError(with:)](<replaceerror(with_).md>) — Replaces any errors in the stream with the provided element.
