---
title: 'init(kind:intent:provider:content:)'
framework: WidgetKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 26.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/appintentconfiguration/init(kind:intent:provider:content:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/appintentconfiguration/init(kind:intent:provider:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/appintentconfiguration/init%28kind%3Aintent%3Aprovider%3Acontent%3A%29.json'
content_hash: 'sha256:31d2c89623a56b92'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [AppIntentConfiguration](../appintentconfiguration.md)

# init(kind:intent:provider:content:)

<sub>Initializer</sub>

Creates a configuration for a widget by using a custom intent to provide user-configurable options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init<Provider>(kind: String, intent: Intent.Type = Intent.self, provider: Provider, @ViewBuilder content: @escaping (Provider.Entry) -> Content) where Intent == Provider.Intent, Provider : AppIntentTimelineProvider
```

## Parameters

- `kind` — A unique string that you choose.

- `intent` — A custom intent containing user-editable parameters.

- `provider` — An object that determines the timing of updates to the widget’s views.

- `content` — A view that renders the widget.

## See Also

### Creating a widget configuration

- [body](../../swiftui/widgetconfiguration/body-swift.property.md) — The content and behavior of this widget.
