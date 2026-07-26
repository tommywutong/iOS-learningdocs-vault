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
doc_path: '/documentation/swift/anyhashable/init(_:)'
source_url: 'https://developer.apple.com/documentation/swift/anyhashable/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anyhashable/init%28_%3A%29.json'
content_hash: 'sha256:77d99ac9d528fa1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AnyHashable](../anyhashable.md)

# init(_:)

<sub>Initializer</sub>

Creates a type-erased hashable value that wraps the given instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<H>(_ base: H) where H : Hashable
```

## Parameters

- `base` — A hashable value to wrap.
