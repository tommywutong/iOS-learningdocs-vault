---
title: 'init(_:)'
framework: WidgetKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 26.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/widgetrelevance/init(_:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/widgetrelevance/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetrelevance/init%28_%3A%29.json'
content_hash: 'sha256:29f200d3ef8453e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [WidgetRelevance](../widgetrelevance.md)

# init(_:)

<sub>Initializer</sub>

Creates a type collecting the relevances for a widget kind.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
init(_ attributes: [WidgetRelevanceAttribute<Configuration>])
```

## Parameters

- `attributes` — A collection of `WidgetRelevanceAttribute` describing when this type of widget could be relevant.
