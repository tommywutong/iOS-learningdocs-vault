---
title: debugDescription
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/foundation/progressreporter/debugdescription
source_url: 'https://developer.apple.com/documentation/foundation/progressreporter/debugdescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressreporter/debugdescription.json'
content_hash: 'sha256:02db9d456d497467'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProgressReporter](../progressreporter.md)

# debugDescription

<sub>Instance Property</sub>

A textual representation of the progress reporter suitable for debugging.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var debugDescription: String { get }
```

## Discussion

This property returns the same value as `description`, providing detailed information about the progress reporter’s state for debugging purposes.
