---
title: 'init(kind:provider:content:)'
framework: WidgetKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/staticconfiguration/init(kind:provider:content:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/staticconfiguration/init(kind:provider:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/staticconfiguration/init%28kind%3Aprovider%3Acontent%3A%29.json'
content_hash: 'sha256:2fb1252cb94dc4e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [StaticConfiguration](../staticconfiguration.md)

# init(kind:provider:content:)

<sub>Initializer</sub>

Creates a configuration for a widget, with no user-configurable options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init<Provider>(kind: String, provider: Provider, @ViewBuilder content: @escaping (Provider.Entry) -> Content) where Provider : TimelineProvider
```

## Parameters

- `kind` — A unique string that you choose.

- `provider` — An object that determines the timing of updates to the widget’s views.

- `content` — A view that renders the widget.

## See Also

### Creating a widget configuration

- [body](../../swiftui/widgetconfiguration/body-swift.property.md) — The content and behavior of this widget.
