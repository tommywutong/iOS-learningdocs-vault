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
doc_path: /documentation/foundation/progressmanager/fractioncompleted
source_url: 'https://developer.apple.com/documentation/foundation/progressmanager/fractioncompleted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressmanager/fractioncompleted.json'
content_hash: 'sha256:7513653a94821c6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProgressManager](../progressmanager.md)

# fractionCompleted

<sub>Instance Property</sub>

The proportion of work completed. This takes into account the fraction completed in its children instances if children are present. If `self` is indeterminate, the value will be 0.0.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var fractionCompleted: Double { get }
```
