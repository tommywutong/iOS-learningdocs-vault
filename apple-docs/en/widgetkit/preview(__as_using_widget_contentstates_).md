---
title: 'Preview(_:as:using:widget:contentStates:)'
framework: WidgetKit
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 17.0+, iPadOS 17.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/preview(_:as:using:widget:contentstates:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/preview(_:as:using:widget:contentstates:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/preview%28_%3Aas%3Ausing%3Awidget%3Acontentstates%3A%29.json'
content_hash: 'sha256:8567dea9dac6be15'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# Preview(_:as:using:widget:contentStates:)

<sub>Macro</sub>

Preview a widget with an activity configuration, using the specified attributes and content states.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@freestanding(declaration) macro Preview<Widget, Attributes>(_ name: String? = nil, as viewKind: ActivityPreviewViewKind, using attributes: Attributes, widget: @escaping () -> Widget, @PreviewActivityBuilder<Attributes> contentStates: @escaping @MainActor () async -> [Attributes.ContentState]) where Widget : Widget, Attributes : ActivityAttributes
```

## Parameters

- `name` — An optional display name for the preview that appears in the preview canvas.

- `viewKind` — The kind of widget view to display.

- `attributes` — The attributes with which to configure the widget.

- `widget` — A closure producing the widget to be previewed.

- `contentStates` — A closure building the content states to be previewed.

## Overview

Provide the preview with sample data and use it to step through the specified content states and test out the transitions between them.

> [!note] Note
> The attributes must be of the type that the widget expects.
