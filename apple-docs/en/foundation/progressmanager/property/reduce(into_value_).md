---
title: 'reduce(into:value:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/foundation/progressmanager/property/reduce(into:value:)'
source_url: 'https://developer.apple.com/documentation/foundation/progressmanager/property/reduce(into:value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressmanager/property/reduce%28into%3Avalue%3A%29.json'
content_hash: 'sha256:6c4d2b7c3eea7012'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [ProgressManager](../../progressmanager.md) · [Property](../property.md)

# reduce(into:value:)

<sub>Type Method</sub>

Reduces a property value into an accumulating summary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func reduce(into summary: inout Self.Summary, value: Self.Value)
```

## Parameters

- `summary` — The accumulating summary value to modify.

- `value` — The individual property value to incorporate into the summary.

## Discussion

This method is called to incorporate individual property values into a summary that represents the aggregated state across multiple progress managers.
