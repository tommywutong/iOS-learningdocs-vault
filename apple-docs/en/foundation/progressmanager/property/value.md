---
title: Value
framework: Foundation
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/foundation/progressmanager/property/value
source_url: 'https://developer.apple.com/documentation/foundation/progressmanager/property/value'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressmanager/property/value.json'
content_hash: 'sha256:0f8dd6a89e730245'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [ProgressManager](../../progressmanager.md) · [Property](../property.md)

# Value

<sub>Associated Type</sub>

The type used for individual values of this property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype Value : Equatable, Sendable
```

## Discussion

This associated type represents the type of property values that can be set on progress managers. Must be `Sendable` and `Equatable`. The currently allowed types are `Int`, `Double`, `String?`, `URL?` or `UInt64`.
