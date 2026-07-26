---
title: popLast()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/unicodescalarview/poplast()
source_url: 'https://developer.apple.com/documentation/swift/string/unicodescalarview/poplast()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/unicodescalarview/poplast%28%29.json'
content_hash: 'sha256:86b389ca44135574'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [UnicodeScalarView](../unicodescalarview.md)

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
