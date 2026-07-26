---
title: 'init(_:order:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/sortdescriptor/init(_:order:)-9noh7'
source_url: 'https://developer.apple.com/documentation/foundation/sortdescriptor/init(_:order:)-9noh7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/sortdescriptor/init%28_%3Aorder%3A%29-9noh7.json'
content_hash: 'sha256:fae2bfbb418a51b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [SortDescriptor](../sortdescriptor.md)

# init(_:order:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ keyPath: any KeyPath<Compared, Int16?> & Sendable, order: SortOrder = .forward) where Compared : NSObject
```
