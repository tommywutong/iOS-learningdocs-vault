---
title: 'init(configuration:context:)'
framework: WidgetKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 26.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/widgetrelevanceattribute/init(configuration:context:)-8325r'
source_url: 'https://developer.apple.com/documentation/widgetkit/widgetrelevanceattribute/init(configuration:context:)-8325r'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetrelevanceattribute/init%28configuration%3Acontext%3A%29-8325r.json'
content_hash: 'sha256:484a87b3285c9544'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [WidgetRelevanceAttribute](../widgetrelevanceattribute.md)

# init(configuration:context:)

<sub>Initializer</sub>

Creates a new widget relevance for a specific configuration that is relevant in a specific context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
init(configuration: Configuration, context: RelevantContext)
```

## Parameters

- `configuration` — The specific configuration

- `context` — The relevant context where this widget is relevant.

## Discussion

For example, a weather widget could specify that a configuration for a specific location is relevant for a the relevant context at that specific location.
