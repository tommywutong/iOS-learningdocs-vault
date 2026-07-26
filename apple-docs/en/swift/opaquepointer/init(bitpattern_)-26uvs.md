---
title: 'init(bitPattern:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/opaquepointer/init(bitpattern:)-26uvs'
source_url: 'https://developer.apple.com/documentation/swift/opaquepointer/init(bitpattern:)-26uvs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/opaquepointer/init%28bitpattern%3A%29-26uvs.json'
content_hash: 'sha256:2b305837118c5431'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [OpaquePointer](../opaquepointer.md)

# init(bitPattern:)

<sub>Initializer</sub>

Creates a new `OpaquePointer` from the given address, specified as a bit pattern.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(bitPattern: Int)
```

## Parameters

- `bitPattern` — A bit pattern to use for the address of the new pointer. If `bitPattern` is zero, the result is `nil`.
