---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsaferawpointer/init(_:)-1z2cc'
source_url: 'https://developer.apple.com/documentation/swift/unsaferawpointer/init(_:)-1z2cc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsaferawpointer/init%28_%3A%29-1z2cc.json'
content_hash: 'sha256:28a9437a30e5c455'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeRawPointer](../unsaferawpointer.md)

# init(_:)

<sub>Initializer</sub>

Creates a new raw pointer from an `AutoreleasingUnsafeMutablePointer` instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<T>(_ other: AutoreleasingUnsafeMutablePointer<T>)
```

## Parameters

- `other` — The pointer to convert.
