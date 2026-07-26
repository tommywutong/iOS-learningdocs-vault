---
title: 'removeDuplicates(by:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/removeduplicates(by:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/removeduplicates(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/removeduplicates%28by%3A%29.json'
content_hash: 'sha256:47d3a7fffb552b7f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# removeDuplicates(by:)

<sub>Instance Method</sub>

Publishes only elements that don’t match the previous element, as evaluated by a provided closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeDuplicates(by predicate: @escaping (Self.Output, Self.Output) -> Bool) -> Publishers.RemoveDuplicates<Self>
```

## Parameters

- `predicate` — A closure to evaluate whether two elements are equivalent, for purposes of filtering. Return `true` from this closure to indicate that the second element is a duplicate of the first.

## Return Value

A publisher that consumes — rather than publishes — duplicate elements.

## Discussion

Use [removeDuplicates(by:)](<removeduplicates(by_).md>) to remove repeating elements from an upstream publisher based upon the evaluation of the current and previously published elements using a closure you provide.

Use the [removeDuplicates(by:)](<removeduplicates(by_).md>) operator when comparing types that don’t themselves implement `Equatable`, or if you need to compare values differently than the type’s `Equatable` implementation.

In the example below, the [removeDuplicates(by:)](<removeduplicates(by_).md>) functionality triggers when the `x` property of the current and previous elements are equal, otherwise the operator publishes the current `Point` to the downstream subscriber:

```swift
struct Point {
    let x: Int
    let y: Int
}

let points = [Point(x: 0, y: 0), Point(x: 0, y: 1),
              Point(x: 1, y: 1), Point(x: 2, y: 1)]
cancellable = points.publisher
    .removeDuplicates { prev, current in
        // Considers points to be duplicate if the x coordinate
        // is equal, and ignores the y coordinate
        prev.x == current.x
    }
    .sink { print("\($0)", terminator: " ") }

// Prints: Point(x: 0, y: 0) Point(x: 1, y: 1) Point(x: 2, y: 1)
```

## See Also

### Filtering elements

- [filter(_:)](<filter(__).md>) — Republishes all elements that match a provided closure.
- [tryFilter(_:)](<tryfilter(__).md>) — Republishes all elements that match a provided error-throwing closure.
- [compactMap(_:)](<compactmap(__).md>) — Calls a closure with each received element and publishes any returned optional that has a value.
- [tryCompactMap(_:)](<trycompactmap(__).md>) — Calls an error-throwing closure with each received element and publishes any returned optional that has a value.
- [removeDuplicates()](<removeduplicates().md>) — Publishes only elements that don’t match the previous element.
- [tryRemoveDuplicates(by:)](<tryremoveduplicates(by_).md>) — Publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [replaceEmpty(with:)](<replaceempty(with_).md>) — Replaces an empty stream with the provided element.
- [replaceError(with:)](<replaceerror(with_).md>) — Replaces any errors in the stream with the provided element.
