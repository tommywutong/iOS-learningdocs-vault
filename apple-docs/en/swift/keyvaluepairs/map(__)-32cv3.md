---
title: 'map(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyvaluepairs/map(_:)-32cv3'
source_url: 'https://developer.apple.com/documentation/swift/keyvaluepairs/map(_:)-32cv3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyvaluepairs/map%28_%3A%29-32cv3.json'
content_hash: 'sha256:651fb6d7874c6305'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyValuePairs](../keyvaluepairs.md)

# map(_:)

<sub>Instance Method</sub>

Returns an array containing the results of mapping the given closure over the sequence’s elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func map<T, E>(_ transform: (Self.Element) throws(E) -> T) throws(E) -> [T] where E : Error
```

## Parameters

- `transform` — A mapping closure. `transform` accepts an element of this sequence as its parameter and returns a transformed value of the same or of a different type.

## Return Value

An array containing the transformed elements of this sequence.

## Discussion

In this example, `map` is used first to convert the names in the array to lowercase strings and then to count their characters.

```swift
let cast = ["Vivien", "Marlon", "Kim", "Karl"]
let lowercaseNames = cast.map { $0.lowercased() }
// 'lowercaseNames' == ["vivien", "marlon", "kim", "karl"]
let letterCounts = cast.map { $0.count }
// 'letterCounts' == [6, 6, 3, 4]
```

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the sequence.
