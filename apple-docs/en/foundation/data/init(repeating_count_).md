---
title: 'init(repeating:count:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/data/init(repeating:count:)'
source_url: 'https://developer.apple.com/documentation/foundation/data/init(repeating:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/init%28repeating%3Acount%3A%29.json'
content_hash: 'sha256:9cc8c59369772bb7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# init(repeating:count:)

<sub>Initializer</sub>

Initialize a `Data` with a repeating byte pattern

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(repeating repeatedValue: UInt8, count: Int)
```

## Parameters

- `repeatedValue` — A byte to initialize the pattern

- `count` — The number of bytes the data initially contains initialized to the repeatedValue
