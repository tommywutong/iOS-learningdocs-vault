---
title: 'init(mutating:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablepointer/init(mutating:)-9gvv3'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablepointer/init(mutating:)-9gvv3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablepointer/init%28mutating%3A%29-9gvv3.json'
content_hash: 'sha256:9464ad0648bf4746'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutablePointer](../unsafemutablepointer.md)

# init(mutating:)

<sub>Initializer</sub>

Creates a mutable typed pointer referencing the same memory as the given immutable pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(mutating other: UnsafePointer<Pointee>)
```

## Parameters

- `other` — The immutable pointer to convert.
