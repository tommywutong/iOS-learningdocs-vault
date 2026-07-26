---
title: removeDuplicates()
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publisher/removeduplicates()
source_url: 'https://developer.apple.com/documentation/combine/publisher/removeduplicates()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/removeduplicates%28%29.json'
content_hash: 'sha256:cc09a63ef1656023'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# removeDuplicates()

<sub>Instance Method</sub>

Publishes only elements that don’t match the previous element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeDuplicates() -> Publishers.RemoveDuplicates<Self>
```

## Return Value

A publisher that consumes — rather than publishes — duplicate elements.

## Discussion

Use [removeDuplicates()](<removeduplicates().md>) to remove repeating elements from an upstream publisher. This operator has a two-element memory: the operator uses the current and previously published elements as the basis for its comparison.

In the example below, [removeDuplicates()](<removeduplicates().md>) triggers on the doubled, tripled, and quadrupled occurrences of `1`, `3`, and `4` respectively. Because the two-element memory considers only the current element and the previous element, the operator prints the final `0` in the example data since its immediate predecessor is `4`.

```swift
let numbers = [0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 0]
cancellable = numbers.publisher
    .removeDuplicates()
    .sink { print("\($0)", terminator: " ") }

// Prints: "0 1 2 3 4 0"
```

## See Also

### Filtering elements

- [filter(_:)](<filter(__).md>) — Republishes all elements that match a provided closure.
- [tryFilter(_:)](<tryfilter(__).md>) — Republishes all elements that match a provided error-throwing closure.
- [compactMap(_:)](<compactmap(__).md>) — Calls a closure with each received element and publishes any returned optional that has a value.
- [tryCompactMap(_:)](<trycompactmap(__).md>) — Calls an error-throwing closure with each received element and publishes any returned optional that has a value.
- [removeDuplicates(by:)](<removeduplicates(by_).md>) — Publishes only elements that don’t match the previous element, as evaluated by a provided closure.
- [tryRemoveDuplicates(by:)](<tryremoveduplicates(by_).md>) — Publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [replaceEmpty(with:)](<replaceempty(with_).md>) — Replaces an empty stream with the provided element.
- [replaceError(with:)](<replaceerror(with_).md>) — Replaces any errors in the stream with the provided element.
