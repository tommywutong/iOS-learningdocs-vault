---
title: 'isTriviallyIdentical(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablebufferpointer/istriviallyidentical(to:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/istriviallyidentical(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablebufferpointer/istriviallyidentical%28to%3A%29.json'
content_hash: 'sha256:fd22bd3aae3f73ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableBufferPointer](../unsafemutablebufferpointer.md)

# isTriviallyIdentical(to:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether two instances refer to the same memory region.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isTriviallyIdentical(to other: UnsafeMutableBufferPointer<Element>) -> Bool
```

## Discussion

> [!abstract] Complexity
> O(1)
