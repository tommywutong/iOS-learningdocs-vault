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
doc_path: /documentation/swift/arrayslice/poplast()-225tk
source_url: 'https://developer.apple.com/documentation/swift/arrayslice/poplast()-225tk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/arrayslice/poplast%28%29-225tk.json'
content_hash: 'sha256:b440b9eb125cd1ee'
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

The last element of the collection if the collection is not empty; otherwise, `nil`.

## Discussion

Calling this method may invalidate all saved indices of this collection. Do not rely on a previously stored index value after altering a collection with any operation that can change its length.

> [!abstract] Complexity
> O(1)
