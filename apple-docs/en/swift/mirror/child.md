---
title: Mirror.Child
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/mirror/child
source_url: 'https://developer.apple.com/documentation/swift/mirror/child'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mirror/child.json'
content_hash: 'sha256:2e51a05528787c28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Mirror](../mirror.md)

# Mirror.Child

<sub>Type Alias</sub>

An element of the reflected instance’s structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Child = (label: String?, value: Any)
```

## Discussion

When the `label` component in not `nil`, it may represent the name of a stored property or an active `enum` case. If you pass strings to the `descendant(_:_:)` method, labels are used for lookup.
