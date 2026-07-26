---
title: 'Preview(_:widget:relevanceProvider:relevance:)'
framework: WidgetKit
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/preview(_:widget:relevanceprovider:relevance:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/preview(_:widget:relevanceprovider:relevance:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/preview%28_%3Awidget%3Arelevanceprovider%3Arelevance%3A%29.json'
content_hash: 'sha256:6bc00c38452ee7bf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# Preview(_:widget:relevanceProvider:relevance:)

<sub>Macro</sub>

Preview a widget with a relevance configuration, using the specified relevances.

<sub>watchOS</sub>

```swift
@freestanding(declaration) macro Preview<Widget, Provider>(_ name: String? = nil, widget: @escaping @MainActor () -> Widget, relevanceProvider: @escaping @MainActor () -> Provider, relevance: @escaping @MainActor () async -> WidgetRelevance<Provider.Configuration>) where Widget : Widget, Provider : RelevanceEntriesProvider
```

## Parameters

- `name` — An optional display name for the preview that appears in the Xcode preview canvas.

- `widget` — A closure producing the widget to be previewed.

- `relevanceProvider` — A closure producing the relevance provider that generates the preview’s entries.

- `relevance` — A closure producing the relevance that the relevance provider uses.

## Overview

Provide the relevance provider with sample data and use it to step through relevance entries in the Xcode proview canvas.

> [!note] Note
> The relevance provider must be of the type that the widget expects.

## See Also

### Generating a widget preview

- [Preview(_:as:widget:timelineProvider:)](<preview(__as_widget_timelineprovider_).md>) — Preview a widget with a static configuration, using the specified timeline provider.
- [Preview(_:as:using:widget:timelineProvider:)](<preview(__as_using_widget_timelineprovider_)-4ljg1.md>) — Preview a widget with an app intent configuration, using the specified timeline provider.
- [Preview(_:as:using:widget:timelineProvider:)](<preview(__as_using_widget_timelineprovider_)-3df1l.md>) — Preview a widget with an intent configuration, using the specified timeline provider.
- [Preview(_:as:widget:timeline:)](<preview(__as_widget_timeline_).md>) — Preview a timeline-style widget.
- [Preview(_:widget:relevanceEntries:)](<preview(__widget_relevanceentries_).md>) — Preview a relevance configuration widget.
- [Preview(_:widget:relevanceProvider:)](<preview(__widget_relevanceprovider_).md>) — Preview a widget with a relevance configuration, using the specified relevance provider.
