---
title: Preview macros
framework: WidgetKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/preview-macros
source_url: 'https://developer.apple.com/documentation/widgetkit/preview-macros'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/preview-macros.json'
content_hash: 'sha256:2cf87dcc9955bae4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# Preview macros

<sub>API Collection</sub>

Use Swift macros to create widget previews in Xcode.

## Topics

### Generating a widget preview

- [Preview(_:as:widget:timelineProvider:)](<preview(__as_widget_timelineprovider_).md>) — Preview a widget with a static configuration, using the specified timeline provider.
- [Preview(_:as:using:widget:timelineProvider:)](<preview(__as_using_widget_timelineprovider_)-4ljg1.md>) — Preview a widget with an app intent configuration, using the specified timeline provider.
- [Preview(_:as:using:widget:timelineProvider:)](<preview(__as_using_widget_timelineprovider_)-3df1l.md>) — Preview a widget with an intent configuration, using the specified timeline provider.
- [Preview(_:as:widget:timeline:)](<preview(__as_widget_timeline_).md>) — Preview a timeline-style widget.
- [Preview(_:widget:relevanceEntries:)](<preview(__widget_relevanceentries_).md>) — Preview a relevance configuration widget.
- [Preview(_:widget:relevanceProvider:)](<preview(__widget_relevanceprovider_).md>) — Preview a widget with a relevance configuration, using the specified relevance provider.
- [Preview(_:widget:relevanceProvider:relevance:)](<preview(__widget_relevanceprovider_relevance_).md>) — Preview a widget with a relevance configuration, using the specified relevances.

### Generating a Live Activity preview

- [Preview(_:as:using:widget:contentStates:)](<preview(__as_using_widget_contentstates_).md>) — Preview a widget with an activity configuration, using the specified attributes and content states.

### Generated structures

- [PreviewActivityBuilder](previewactivitybuilder.md)
- [PreviewRelevanceEntryBuilder](previewrelevanceentrybuilder.md) — A builder that allows you to construct a list of relevance entries to preview your widget.
- [PreviewTimelineBuilder](previewtimelinebuilder.md)

## See Also

### Previews and debugging

- [Previewing widgets and Live Activities in Xcode](previewing-widgets-and-live-activities-in-xcode.md) — Use Xcode previews to iteratively develop, fine-tune, and troubleshoot widgets and Live Activities.
- [WidgetPreviewContext](widgetpreviewcontext.md) — A specification for the context of a widget preview.
