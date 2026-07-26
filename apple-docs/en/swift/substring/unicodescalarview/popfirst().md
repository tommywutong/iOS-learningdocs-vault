---
title: popFirst()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/substring/unicodescalarview/popfirst()
source_url: 'https://developer.apple.com/documentation/swift/substring/unicodescalarview/popfirst()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/unicodescalarview/popfirst%28%29.json'
content_hash: 'sha256:3b6407d37920c10d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Substring](../../substring.md) · [UnicodeScalarView](../unicodescalarview.md)

# popFirst()

<sub>Instance Method</sub>

Removes and returns the first element of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func popFirst() -> Self.Element?
```

## Return Value

The first element of the collection if the collection is not empty; otherwise, `nil`.

## Discussion

> [!abstract] Complexity
> O(1)
