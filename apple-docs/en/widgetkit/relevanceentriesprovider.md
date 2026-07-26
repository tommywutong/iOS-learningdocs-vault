---
title: RelevanceEntriesProvider
framework: WidgetKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/relevanceentriesprovider
source_url: 'https://developer.apple.com/documentation/widgetkit/relevanceentriesprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/relevanceentriesprovider.json'
content_hash: 'sha256:04158206ff34eb1d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# RelevanceEntriesProvider

<sub>Protocol</sub>

A type that provides the content for a widget that uses relevance clues to display information in the Smart Stack.

<sub>watchOS</sub>

```swift
protocol RelevanceEntriesProvider
```

## Topics

### Generating relevance entries

- [entry(configuration:context:)](<relevanceentriesprovider/entry(configuration_context_).md>) — Provides the entry used to render a widget for a specific relevance configuration.
- [relevance()](<relevanceentriesprovider/relevance().md>) — Provides a collection of conditions under which a specific widget could be relevant.
- [placeholder(context:)](<relevanceentriesprovider/placeholder(context_).md>) — Provides the entry representing a placeholder version of the widget.
- [RelevanceEntriesProviderContext](relevanceentriesprovidercontext.md) — An object that contains details about how a widget is rendered, including its size.

### Associated Types

- [Configuration](relevanceentriesprovider/configuration.md) — The type of configuration associated with a specific relevance.
- [Entry](relevanceentriesprovider/entry.md) — A type that specifies the information to render a widget at a specific relevance configuration.

### Type Aliases

- [Context](relevanceentriesprovider/context.md) — An object that contains details about how a widget is rendered.

## See Also

### Smart Stacks

- [Increasing the visibility of widgets in Smart Stacks](widget-suggestions-in-smart-stacks.md) — Provide contextual information and donate intents to the system to make sure your widget appears prominently in Smart Stacks.
- [TimelineEntryRelevance](timelineentryrelevance.md) — An object that describes the relative importance of a timeline entry compared to other entries in the current and past timelines.
- [RelevanceConfiguration](relevanceconfiguration.md) — A type that describes the content of a widget that uses relevance clues.
- [RelevanceEntry](relevanceentry.md) — A type that specifies the information to render a widget at a specific relevance configuration.
- [WidgetRelevance](widgetrelevance.md) — A type collecting the relevances for a widget kind.
- [WidgetRelevanceAttribute](widgetrelevanceattribute.md) — A type that describes when a specific widget could be relevant.
- [WidgetRelevanceGroup](widgetrelevancegroup.md) — A type for configuring widget behavior in the watchOS Smart Stack.
- [AppIntentRecommendation](appintentrecommendation.md) — An object that describes a recommended intent configuration for a user-customizable widget.
- [IntentConfiguration](intentconfiguration.md) — An object describing the content of a widget that uses a custom intent definition to provide user-configurable options.
- [IntentRecommendation](intentrecommendation.md) — An object that describes a recommended intent configuration for a user-customizable widget.
