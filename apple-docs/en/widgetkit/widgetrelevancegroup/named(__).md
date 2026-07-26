---
title: 'named(_:)'
framework: WidgetKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 26.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/widgetrelevancegroup/named(_:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/widgetrelevancegroup/named(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetrelevancegroup/named%28_%3A%29.json'
content_hash: 'sha256:ee65a6cc104e2ca2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [WidgetRelevanceGroup](../widgetrelevancegroup.md)

# named(_:)

<sub>Type Method</sub>

Creates a group with the provided name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
static func named(_ name: String) -> WidgetRelevanceGroup
```

## Discussion

The system won’t show more than one relevant widget if they are in the same. A widget group doesn’t affect widgets by other apps.
