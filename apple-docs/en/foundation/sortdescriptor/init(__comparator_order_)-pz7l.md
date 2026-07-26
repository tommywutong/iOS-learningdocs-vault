---
title: 'init(_:comparator:order:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/sortdescriptor/init(_:comparator:order:)-pz7l'
source_url: 'https://developer.apple.com/documentation/foundation/sortdescriptor/init(_:comparator:order:)-pz7l'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/sortdescriptor/init%28_%3Acomparator%3Aorder%3A%29-pz7l.json'
content_hash: 'sha256:b0579ca5300c190a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [SortDescriptor](../sortdescriptor.md)

# init(_:comparator:order:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ keyPath: any KeyPath<Compared, String?> & Sendable, comparator: String.StandardComparator = .localizedStandard, order: SortOrder)
```
