---
title: 'Preview(_:as:widget:timelineProvider:)'
framework: WidgetKit
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 26.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/preview(_:as:widget:timelineprovider:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/preview(_:as:widget:timelineprovider:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/preview%28_%3Aas%3Awidget%3Atimelineprovider%3A%29.json'
content_hash: 'sha256:448049b566cb7c6d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# Preview(_:as:widget:timelineProvider:)

<sub>Macro</sub>

Preview a widget with a static configuration, using the specified timeline provider.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@freestanding(declaration) macro Preview<Widget, Provider>(_ name: String? = nil, as family: WidgetFamily, widget: @escaping () -> Widget, timelineProvider: @escaping () -> Provider) where Widget : Widget, Provider : TimelineProvider
```

## Parameters

- `name` — An optional display name for the preview that appears in the Xcode preview canvas.

- `family` — The widget family to display.

- `widget` — A closure producing the widget to be previewed.

- `timelineProvider` — A closure producing the timeline provider that generates the preview’s timeline.

## Overview

Provide the preview with sample data and use it to step through the timeline while ignoring the dates of the entries, and test out the transitions between them.

> [!note] Note
> The timeline provider must be of the type that the widget expects.

## See Also

### Generating a widget preview

- [Preview(_:as:using:widget:timelineProvider:)](<preview(__as_using_widget_timelineprovider_)-4ljg1.md>) — Preview a widget with an app intent configuration, using the specified timeline provider.
- [Preview(_:as:using:widget:timelineProvider:)](<preview(__as_using_widget_timelineprovider_)-3df1l.md>) — Preview a widget with an intent configuration, using the specified timeline provider.
- [Preview(_:as:widget:timeline:)](<preview(__as_widget_timeline_).md>) — Preview a timeline-style widget.
- [Preview(_:widget:relevanceEntries:)](<preview(__widget_relevanceentries_).md>) — Preview a relevance configuration widget.
- [Preview(_:widget:relevanceProvider:)](<preview(__widget_relevanceprovider_).md>) — Preview a widget with a relevance configuration, using the specified relevance provider.
- [Preview(_:widget:relevanceProvider:relevance:)](<preview(__widget_relevanceprovider_relevance_).md>) — Preview a widget with a relevance configuration, using the specified relevances.
