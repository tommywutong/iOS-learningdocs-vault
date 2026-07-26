---
title: header
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/managedbuffer/header
source_url: 'https://developer.apple.com/documentation/swift/managedbuffer/header'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/managedbuffer/header.json'
content_hash: 'sha256:e9059370f6cee2f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ManagedBuffer](../managedbuffer.md)

# header

<sub>Instance Property</sub>

The stored `Header` instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var header: Header
```

## Discussion

During instance creation, in particular during `ManagedBuffer.create`’s call to initialize, `ManagedBuffer`’s `header` property is as-yet uninitialized, and therefore reading the `header` property during `ManagedBuffer.create` is undefined.
