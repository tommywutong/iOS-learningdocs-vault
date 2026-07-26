---
title: 'random(using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, tvOS 26.4+, visionOS 26.4+, watchOS 26.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/uuid/random(using:)'
source_url: 'https://developer.apple.com/documentation/foundation/uuid/random(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/uuid/random%28using%3A%29.json'
content_hash: 'sha256:f861cbde19b90117'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UUID](../uuid.md)

# random(using:)

<sub>Type Method</sub>

Generates a new random UUID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func random(using generator: inout some RandomNumberGenerator) -> UUID
```

## Parameters

- `generator` — The random number generator to use when creating the new random value.

## Return Value

A random UUID.
