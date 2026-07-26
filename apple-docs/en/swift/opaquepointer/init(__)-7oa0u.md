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
doc_path: '/documentation/swift/opaquepointer/init(_:)-7oa0u'
source_url: 'https://developer.apple.com/documentation/swift/opaquepointer/init(_:)-7oa0u'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/opaquepointer/init%28_%3A%29-7oa0u.json'
content_hash: 'sha256:186388b5b346686d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [OpaquePointer](../opaquepointer.md)

# init(_:)

<sub>Initializer</sub>

Converts a typed `UnsafeMutablePointer` to an opaque C pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<T>(_ from: UnsafeMutablePointer<T>) where T : ~Copyable
```
