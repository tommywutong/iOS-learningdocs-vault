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
doc_path: '/documentation/widgetkit/staticcontrolconfiguration/init(kind:provider:content:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/staticcontrolconfiguration/init(kind:provider:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/staticcontrolconfiguration/init%28kind%3Aprovider%3Acontent%3A%29.json'
content_hash: 'sha256:a7d992ca950e5e25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [StaticControlConfiguration](../staticcontrolconfiguration.md)

# init(kind:provider:content:)

<sub>Initializer</sub>

Creates a configuration for a control, with no user-configurable options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
@MainActor @preconcurrency init<Provider>(kind: String, provider: Provider, @ControlWidgetTemplateBuilder content: @escaping (Provider.Value) -> Content) where Provider : ControlValueProvider
```

## Parameters

- `kind` — A string that uniquely identifies the type of control.

- `provider` — An object that provides a value to the control template.

- `content` — A template that renders the control.
