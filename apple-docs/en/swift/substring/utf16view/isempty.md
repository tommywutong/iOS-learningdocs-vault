---
title: isEmpty
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/substring/utf16view/isempty
source_url: 'https://developer.apple.com/documentation/swift/substring/utf16view/isempty'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/utf16view/isempty.json'
content_hash: 'sha256:8bfd1bda6a77d198'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Substring](../../substring.md) · [UTF16View](../utf16view.md)

# isEmpty

<sub>Instance Property</sub>

A Boolean value indicating whether the collection is empty.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isEmpty: Bool { get }
```

## Discussion

When you need to check whether your collection is empty, use the `isEmpty` property instead of checking that the `count` property is equal to zero. For collections that don’t conform to `RandomAccessCollection`, accessing the `count` property iterates through the elements of the collection.

```swift
let horseName = "Silver"
if horseName.isEmpty {
    print("My horse has no name.")
} else {
    print("Hi ho, \(horseName)!")
}
// Prints "Hi ho, Silver!")
```

> [!abstract] Complexity
> O(1)
