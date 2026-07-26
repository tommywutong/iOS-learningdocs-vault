---
title: 'init(_:strategy:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/datecomponents/init(_:strategy:)-62hv8'
source_url: 'https://developer.apple.com/documentation/foundation/datecomponents/init(_:strategy:)-62hv8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponents/init%28_%3Astrategy%3A%29-62hv8.json'
content_hash: 'sha256:c6f133cf8e22365c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponents](../datecomponents.md)

# init(_:strategy:)

<sub>Initializer</sub>

Creates a new `DateComponents` by parsing the given string representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<T, Value>(_ value: Value, strategy: T) throws where T : ParseStrategy, Value : StringProtocol, T.ParseInput == String, T.ParseOutput == DateComponents
```
