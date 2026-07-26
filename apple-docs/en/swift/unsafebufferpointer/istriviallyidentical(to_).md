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
doc_path: '/documentation/swift/unsafebufferpointer/istriviallyidentical(to:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafebufferpointer/istriviallyidentical(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafebufferpointer/istriviallyidentical%28to%3A%29.json'
content_hash: 'sha256:e833edf45ad5108e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeBufferPointer](../unsafebufferpointer.md)

# isTriviallyIdentical(to:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether two instances refer to the same memory region.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isTriviallyIdentical(to other: UnsafeBufferPointer<Element>) -> Bool
```

## Discussion

> [!abstract] Complexity
> O(1)
