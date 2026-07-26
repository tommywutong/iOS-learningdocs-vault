---
title: 'replaceEmpty(with:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/replaceempty(with:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/replaceempty(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/replaceempty%28with%3A%29.json'
content_hash: 'sha256:2c9f98f68ecf4b40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# replaceEmpty(with:)

<sub>Instance Method</sub>

Replaces an empty stream with the provided element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replaceEmpty(with output: Self.Output) -> Publishers.ReplaceEmpty<Self>
```

## Parameters

- `output` — An element to emit when the upstream publisher finishes without emitting any elements.

## Return Value

A publisher that replaces an empty stream with the provided output element.

## Discussion

Use [replaceEmpty(with:)](<replaceempty(with_).md>) to provide a replacement element if the upstream publisher finishes without producing any elements.

In the example below, the empty `Double` array publisher doesn’t produce any elements, so [replaceEmpty(with:)](<replaceempty(with_).md>) publishes `Double.nan` and finishes normally.

```swift
let numbers: [Double] = []
cancellable = numbers.publisher
    .replaceEmpty(with: Double.nan)
    .sink { print("\($0)", terminator: " ") }

// Prints "(nan)".
```

Conversely, providing a non-empty publisher publishes all elements and the publisher then terminates normally:

```swift
let otherNumbers: [Double] = [1.0, 2.0, 3.0]
cancellable2 = otherNumbers.publisher
    .replaceEmpty(with: Double.nan)
    .sink { print("\($0)", terminator: " ") }

// Prints: 1.0 2.0 3.0
```

## See Also

### Filtering elements

- [filter(_:)](<filter(__).md>) — Republishes all elements that match a provided closure.
- [tryFilter(_:)](<tryfilter(__).md>) — Republishes all elements that match a provided error-throwing closure.
- [compactMap(_:)](<compactmap(__).md>) — Calls a closure with each received element and publishes any returned optional that has a value.
- [tryCompactMap(_:)](<trycompactmap(__).md>) — Calls an error-throwing closure with each received element and publishes any returned optional that has a value.
- [removeDuplicates()](<removeduplicates().md>) — Publishes only elements that don’t match the previous element.
- [removeDuplicates(by:)](<removeduplicates(by_).md>) — Publishes only elements that don’t match the previous element, as evaluated by a provided closure.
- [tryRemoveDuplicates(by:)](<tryremoveduplicates(by_).md>) — Publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [replaceError(with:)](<replaceerror(with_).md>) — Replaces any errors in the stream with the provided element.
