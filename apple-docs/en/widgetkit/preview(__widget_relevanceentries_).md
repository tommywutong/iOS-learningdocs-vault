---
title: 'Preview(_:widget:relevanceEntries:)'
framework: WidgetKit
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/preview(_:widget:relevanceentries:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/preview(_:widget:relevanceentries:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/preview%28_%3Awidget%3Arelevanceentries%3A%29.json'
content_hash: 'sha256:0d6671e44a2ffee5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# Preview(_:widget:relevanceEntries:)

<sub>Macro</sub>

Preview a relevance configuration widget.

<sub>watchOS</sub>

```swift
@freestanding(declaration) macro Preview<Widget, Entry>(_ name: String? = nil, widget: @escaping @MainActor () -> Widget, @PreviewRelevanceEntryBuilder<Entry> relevanceEntries: @escaping @MainActor () async -> [Entry]) where Widget : Widget, Entry : RelevanceEntry
```

## Parameters

- `name` — An optional display name for the preview that appears in the Xcode preview canvas.

- `widget` — A closure producing the widget to be previewed.

- `relevanceEntries` — A closure building the entries to be previewed.

## Overview

Provide the preview with sample data and use it to step through the timeline while ignoring the dates of the entries, and test out the transitions between them.

> [!note] Note
> The relevance entries must be of the type that the widget expects.

## See Also

### Generating a widget preview

- [Preview(_:as:widget:timelineProvider:)](<preview(__as_widget_timelineprovider_).md>) — Preview a widget with a static configuration, using the specified timeline provider.
- [Preview(_:as:using:widget:timelineProvider:)](<preview(__as_using_widget_timelineprovider_)-4ljg1.md>) — Preview a widget with an app intent configuration, using the specified timeline provider.
- [Preview(_:as:using:widget:timelineProvider:)](<preview(__as_using_widget_timelineprovider_)-3df1l.md>) — Preview a widget with an intent configuration, using the specified timeline provider.
- [Preview(_:as:widget:timeline:)](<preview(__as_widget_timeline_).md>) — Preview a timeline-style widget.
- [Preview(_:widget:relevanceProvider:)](<preview(__widget_relevanceprovider_).md>) — Preview a widget with a relevance configuration, using the specified relevance provider.
- [Preview(_:widget:relevanceProvider:relevance:)](<preview(__widget_relevanceprovider_relevance_).md>) — Preview a widget with a relevance configuration, using the specified relevances.
