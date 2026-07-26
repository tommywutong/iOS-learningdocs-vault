---
title: Summary
framework: Foundation
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/foundation/progressmanager/property/summary
source_url: 'https://developer.apple.com/documentation/foundation/progressmanager/property/summary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressmanager/property/summary.json'
content_hash: 'sha256:61694c37f751d2e6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [ProgressManager](../../progressmanager.md) · [Property](../property.md)

# Summary

<sub>Associated Type</sub>

The type used for aggregated summaries of this property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype Summary : Equatable, Sendable
```

## Discussion

This associated type represents the type used when summarizing property values across multiple progress managers in a subtree. The currently allowed types are `Int`, `Double`, `[String?]`, `[URL?]` or `[UInt64]`.
