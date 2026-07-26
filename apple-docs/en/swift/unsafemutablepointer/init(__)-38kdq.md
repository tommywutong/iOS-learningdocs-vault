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
doc_path: '/documentation/swift/unsafemutablepointer/init(_:)-38kdq'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablepointer/init(_:)-38kdq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablepointer/init%28_%3A%29-38kdq.json'
content_hash: 'sha256:ec3381581bf2e0a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutablePointer](../unsafemutablepointer.md)

# init(_:)

<sub>Initializer</sub>

Creates a mutable typed pointer referencing the same memory as the given mutable pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(_ other: UnsafeMutablePointer<Pointee>?)
```

## Parameters

- `other` — The pointer to convert. If `other` is `nil`, the result is `nil`.
