---
title: 'init(_:strategy:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/init(_:strategy:)-2oqi'
source_url: 'https://developer.apple.com/documentation/foundation/date/init(_:strategy:)-2oqi'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/init%28_%3Astrategy%3A%29-2oqi.json'
content_hash: 'sha256:b322e8297be32f31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Date](../date.md)

# init(_:strategy:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<T>(_ value: T.ParseInput, strategy: T) throws where T : ParseStrategy, T.ParseOutput == Date
```
