---
title: 'init(kind:intent:provider:content:)'
framework: WidgetKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/intentconfiguration/init(kind:intent:provider:content:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/intentconfiguration/init(kind:intent:provider:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/intentconfiguration/init%28kind%3Aintent%3Aprovider%3Acontent%3A%29.json'
content_hash: 'sha256:9fff35d319d5aa40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [IntentConfiguration](../intentconfiguration.md)

# init(kind:intent:provider:content:)

<sub>Initializer</sub>

Creates a configuration for a widget by using a custom intent definition to provide user-configurable options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init<Provider>(kind: String, intent: Intent.Type, provider: Provider, @ViewBuilder content: @escaping (Provider.Entry) -> Content) where Intent == Provider.Intent, Provider : IntentTimelineProvider
```

## Parameters

- `kind` — A unique string that you choose.

- `intent` — A custom intent definition containing user-editable parameters.

- `provider` — An object that determines the timing of updates to the widget’s views.

- `content` — A view that renders the widget.

## See Also

### Creating a widget configuration

- [body](../../swiftui/widgetconfiguration/body-swift.property.md) — The content and behavior of this widget.
