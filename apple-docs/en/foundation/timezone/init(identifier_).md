---
title: 'init(identifier:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/timezone/init(identifier:)'
source_url: 'https://developer.apple.com/documentation/foundation/timezone/init(identifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timezone/init%28identifier%3A%29.json'
content_hash: 'sha256:04040ddfa7b58ed2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [TimeZone](../timezone.md)

# init(identifier:)

<sub>Initializer</sub>

Returns a time zone initialized with a given identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(identifier: String)
```

## Discussion

An example identifier is “America/Los_Angeles”.

If `identifier` is an unknown identifier, then returns `nil`.
