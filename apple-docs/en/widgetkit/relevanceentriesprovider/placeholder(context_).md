---
title: 'placeholder(context:)'
framework: WidgetKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/relevanceentriesprovider/placeholder(context:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/relevanceentriesprovider/placeholder(context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/relevanceentriesprovider/placeholder%28context%3A%29.json'
content_hash: 'sha256:cfd8cf17fada2297'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [RelevanceEntriesProvider](../relevanceentriesprovider.md)

# placeholder(context:)

<sub>Instance Method</sub>

Provides the entry representing a placeholder version of the widget.

<sub>watchOS</sub>

```swift
func placeholder(context: Self.Context) -> Self.Entry
```

## Parameters

- `context` — An object describing the context to show the widget in.

## Return Value

A relevance entry that represents a placeholder version of the widget.

## See Also

### Generating relevance entries

- [entry(configuration:context:)](<entry(configuration_context_).md>) — Provides the entry used to render a widget for a specific relevance configuration.
- [relevance()](<relevance().md>) — Provides a collection of conditions under which a specific widget could be relevant.
- [RelevanceEntriesProviderContext](../relevanceentriesprovidercontext.md) — An object that contains details about how a widget is rendered, including its size.
