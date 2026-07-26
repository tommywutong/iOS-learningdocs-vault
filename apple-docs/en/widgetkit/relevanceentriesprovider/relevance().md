---
title: relevance()
framework: WidgetKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/relevanceentriesprovider/relevance()
source_url: 'https://developer.apple.com/documentation/widgetkit/relevanceentriesprovider/relevance()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/relevanceentriesprovider/relevance%28%29.json'
content_hash: 'sha256:ee47be3653c761b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [RelevanceEntriesProvider](../relevanceentriesprovider.md)

# relevance()

<sub>Instance Method</sub>

Provides a collection of conditions under which a specific widget could be relevant.

<sub>watchOS</sub>

```swift
func relevance() async -> WidgetRelevance<Self.Configuration>
```

## Discussion

The system can use the relevance to show this widget when the conditions for the relevance match the current state.

## See Also

### Generating relevance entries

- [entry(configuration:context:)](<entry(configuration_context_).md>) — Provides the entry used to render a widget for a specific relevance configuration.
- [placeholder(context:)](<placeholder(context_).md>) — Provides the entry representing a placeholder version of the widget.
- [RelevanceEntriesProviderContext](../relevanceentriesprovidercontext.md) — An object that contains details about how a widget is rendered, including its size.
