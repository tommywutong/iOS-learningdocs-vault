---
title: pointee
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unsafemutablepointer/pointee
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablepointer/pointee'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablepointer/pointee.json'
content_hash: 'sha256:67acde5d36b22fe3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutablePointer](../unsafemutablepointer.md)

# pointee

<sub>Instance Property</sub>

Reads or updates the instance referenced by this pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var pointee: Pointee { get nonmutating set }
```

## Discussion

When reading from the `pointee` property, the instance referenced by this pointer must already be initialized. When `pointee` is used as the left side of an assignment, the instance is updated. The instance must be initialized or this pointer’s `Pointee` type must be a trivial type.

Uninitialized memory cannot be initialized to a nontrivial type using `pointee`. Instead, use an initializing method, such as `initialize(to:)`.
