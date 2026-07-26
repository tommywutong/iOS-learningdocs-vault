---
title: 'entry(configuration:context:)'
framework: WidgetKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/relevanceentriesprovider/entry(configuration:context:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/relevanceentriesprovider/entry(configuration:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/relevanceentriesprovider/entry%28configuration%3Acontext%3A%29.json'
content_hash: 'sha256:161921df5e2ca36d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [RelevanceEntriesProvider](../relevanceentriesprovider.md)

# entry(configuration:context:)

<sub>Instance Method</sub>

Provides the entry used to render a widget for a specific relevance configuration.

<sub>watchOS</sub>

```swift
func entry(configuration: Self.Configuration, context: Self.Context) async throws -> Self.Entry
```

## Parameters

- `configuration` — The configuration for when this widget is relevant.

- `context` — An object describing the context to show the widget in.

## Return Value

A relevance entry representing the widget in this configuration.

## See Also

### Generating relevance entries

- [relevance()](<relevance().md>) — Provides a collection of conditions under which a specific widget could be relevant.
- [placeholder(context:)](<placeholder(context_).md>) — Provides the entry representing a placeholder version of the widget.
- [RelevanceEntriesProviderContext](../relevanceentriesprovidercontext.md) — An object that contains details about how a widget is rendered, including its size.
