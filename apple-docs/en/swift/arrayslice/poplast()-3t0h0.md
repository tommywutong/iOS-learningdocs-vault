---
title: popLast()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/arrayslice/poplast()-3t0h0
source_url: 'https://developer.apple.com/documentation/swift/arrayslice/poplast()-3t0h0'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/arrayslice/poplast%28%29-3t0h0.json'
content_hash: 'sha256:8ddf2fe76346f75c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ArraySlice](../arrayslice.md)

# popLast()

<sub>Instance Method</sub>

Removes and returns the last element of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func popLast() -> Self.Element?
```

## Return Value

The last element of the collection if the collection has one or more elements; otherwise, `nil`.

## Discussion

You can use `popLast()` to remove the last element of a collection that might be empty. The `removeLast()` method must be used only on a nonempty collection.

> [!abstract] Complexity
> O(1)
