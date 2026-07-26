---
title: fractionCompleted
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/foundation/progressreporter/fractioncompleted
source_url: 'https://developer.apple.com/documentation/foundation/progressreporter/fractioncompleted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressreporter/fractioncompleted.json'
content_hash: 'sha256:1d0be13f41f6866f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProgressReporter](../progressreporter.md)

# fractionCompleted

<sub>Instance Property</sub>

The proportion of work completed. This takes into account the fraction completed in its children instances if children are present. If `self` is indeterminate, the value will be 0.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var fractionCompleted: Double { get }
```
