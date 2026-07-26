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
doc_path: '/documentation/swift/anysequence/init(_:)-307a9'
source_url: 'https://developer.apple.com/documentation/swift/anysequence/init(_:)-307a9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anysequence/init%28_%3A%29-307a9.json'
content_hash: 'sha256:7f59a55c7462044f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AnySequence](../anysequence.md)

# init(_:)

<sub>Initializer</sub>

Creates a new sequence that wraps and forwards operations to `base`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S>(_ base: S) where Element == S.Element, S : Sequence
```
