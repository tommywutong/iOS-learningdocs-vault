---
title: 'merge(_:_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/foundation/progressmanager/property/merge(_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/progressmanager/property/merge(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressmanager/property/merge%28_%3A_%3A%29.json'
content_hash: 'sha256:09d1b393378e7470'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [ProgressManager](../../progressmanager.md) · [Property](../property.md)

# merge(_:_:)

<sub>Type Method</sub>

Merges two summary values into a single combined summary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func merge(_ summary1: Self.Summary, _ summary2: Self.Summary) -> Self.Summary
```

## Parameters

- `summary1` — The first summary to merge.

- `summary2` — The second summary to merge.

## Return Value

A new summary that represents the combination of both input summaries.

## Discussion

This method is called to combine summary values from different branches of the progress manager hierarchy into a unified summary.
