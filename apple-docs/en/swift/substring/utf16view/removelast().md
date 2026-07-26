---
title: removeLast()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/substring/utf16view/removelast()
source_url: 'https://developer.apple.com/documentation/swift/substring/utf16view/removelast()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/utf16view/removelast%28%29.json'
content_hash: 'sha256:d1981b450ee861f5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Substring](../../substring.md) · [UTF16View](../utf16view.md)

# removeLast()

<sub>Instance Method</sub>

Removes and returns the last element of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func removeLast() -> Self.Element
```

## Return Value

The last element of the collection.

## Discussion

The collection must not be empty. To remove the last element of a collection that might be empty, use the `popLast()` method instead.

> [!abstract] Complexity
> O(1)
