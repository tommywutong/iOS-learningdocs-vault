---
title: 'init(_:comparator:order:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/sortdescriptor/init(_:comparator:order:)-4qaip'
source_url: 'https://developer.apple.com/documentation/foundation/sortdescriptor/init(_:comparator:order:)-4qaip'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/sortdescriptor/init%28_%3Acomparator%3Aorder%3A%29-4qaip.json'
content_hash: 'sha256:61ef8f0789d9043e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [SortDescriptor](../sortdescriptor.md)

# init(_:comparator:order:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ keyPath: any KeyPath<Compared, String> & Sendable, comparator: String.StandardComparator = .localizedStandard, order: SortOrder) where Compared : NSObject
```
