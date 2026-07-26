---
title: 'init(_:order:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/sortdescriptor/init(_:order:)-3wozy'
source_url: 'https://developer.apple.com/documentation/foundation/sortdescriptor/init(_:order:)-3wozy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/sortdescriptor/init%28_%3Aorder%3A%29-3wozy.json'
content_hash: 'sha256:ff0a1ce2649a36f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [SortDescriptor](../sortdescriptor.md)

# init(_:order:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Value>(_ keyPath: any KeyPath<Compared, Value?> & Sendable, order: SortOrder = .forward) where Value : Comparable
```
