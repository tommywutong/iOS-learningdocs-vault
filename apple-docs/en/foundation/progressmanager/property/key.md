---
title: key
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/foundation/progressmanager/property/key
source_url: 'https://developer.apple.com/documentation/foundation/progressmanager/property/key'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressmanager/property/key.json'
content_hash: 'sha256:bf9215e8f3b2a661'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [ProgressManager](../../progressmanager.md) · [Property](../property.md)

# key

<sub>Type Property</sub>

A unique identifier for this property type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var key: String { get }
```

## Return Value

A unique string identifier for this property type.

## Discussion

The key should use reverse DNS style notation to ensure uniqueness across different frameworks and applications.
