---
title: 'init(kind:provider:content:)'
framework: WidgetKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/appintentcontrolconfiguration/init(kind:provider:content:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/appintentcontrolconfiguration/init(kind:provider:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/appintentcontrolconfiguration/init%28kind%3Aprovider%3Acontent%3A%29.json'
content_hash: 'sha256:0623cc46725f57a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [AppIntentControlConfiguration](../appintentcontrolconfiguration.md)

# init(kind:provider:content:)

<sub>Initializer</sub>

Creates a configuration for a control that uses a custom app intent to provide user-configurable options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
@MainActor @preconcurrency init<Provider>(kind: String, provider: Provider, @ControlWidgetTemplateBuilder content: @escaping (Provider.Value) -> Content) where Configuration == Provider.Configuration, Provider : AppIntentControlValueProvider
```

## Parameters

- `kind` — A string that uniquely identifies the type of control.

- `provider` — An object that provides a value to the control template. The provider uses your custom intent to prepare this value.

- `content` — A template that renders the control.
