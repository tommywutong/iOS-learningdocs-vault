---
title: 'init(kind:provider:content:)'
framework: WidgetKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/relevanceconfiguration/init(kind:provider:content:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/relevanceconfiguration/init(kind:provider:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/relevanceconfiguration/init%28kind%3Aprovider%3Acontent%3A%29.json'
content_hash: 'sha256:7f8bc384b36067c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [RelevanceConfiguration](../relevanceconfiguration.md)

# init(kind:provider:content:)

<sub>Initializer</sub>

Creates a configuration for a widget that provides relevance clues to the system.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency init<Provider>(kind: String, provider: Provider, @ViewBuilder content: @escaping @MainActor (Provider.Entry) -> Content) where Provider : RelevanceEntriesProvider
```

## Parameters

- `kind` — A unique string that you choose.

- `provider` — An object that determines the relevance and data of the widget.

- `content` — A view that renders the widget.
