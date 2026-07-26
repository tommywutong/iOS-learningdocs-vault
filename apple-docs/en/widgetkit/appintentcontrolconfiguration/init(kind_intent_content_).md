---
title: 'init(kind:intent:content:)'
framework: WidgetKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/appintentcontrolconfiguration/init(kind:intent:content:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/appintentcontrolconfiguration/init(kind:intent:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/appintentcontrolconfiguration/init%28kind%3Aintent%3Acontent%3A%29.json'
content_hash: 'sha256:dad6fdc43d5d6f39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [AppIntentControlConfiguration](../appintentcontrolconfiguration.md)

# init(kind:intent:content:)

<sub>Initializer</sub>

Creates a configuration for a control that uses a custom app intent to provide user-configurable options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(kind: String, intent: Configuration.Type = Configuration.self, @ControlWidgetTemplateBuilder content: @escaping (Configuration) -> Content)
```

## Parameters

- `kind` — A string that uniquely identifies the type of control.

- `intent` — A custom intent containing user-editable parameters.

- `content` — A template that renders the control.
