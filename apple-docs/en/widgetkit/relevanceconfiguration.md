---
title: RelevanceConfiguration
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/relevanceconfiguration
source_url: 'https://developer.apple.com/documentation/widgetkit/relevanceconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/relevanceconfiguration.json'
content_hash: 'sha256:76ef83ab328abad1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# RelevanceConfiguration

<sub>Structure</sub>

A type that describes the content of a widget that uses relevance clues.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency struct RelevanceConfiguration<Content> where Content : View
```

## Overview

In watchOS, widgets can provide the system with relevance clues to indicate that the widget is relevant to a person and should appear prominently in the Smart Stack. To provide relevance clues to watchOS, use `RelevanceConfiguration` or implement the `relevance()` requirement in your timeline provider.

For more information, refer to [Increasing the visibility of widgets in Smart Stacks](widget-suggestions-in-smart-stacks.md).

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [WidgetConfiguration](../swiftui/widgetconfiguration.md)

## Topics

### Creating a relevance configuration

- [init(kind:provider:content:)](<relevanceconfiguration/init(kind_provider_content_).md>) — Creates a configuration for a widget that provides relevance clues to the system.

## See Also

### Smart Stacks

- [Increasing the visibility of widgets in Smart Stacks](widget-suggestions-in-smart-stacks.md) — Provide contextual information and donate intents to the system to make sure your widget appears prominently in Smart Stacks.
- [TimelineEntryRelevance](timelineentryrelevance.md) — An object that describes the relative importance of a timeline entry compared to other entries in the current and past timelines.
- [RelevanceEntriesProvider](relevanceentriesprovider.md) — A type that provides the content for a widget that uses relevance clues to display information in the Smart Stack.
- [RelevanceEntry](relevanceentry.md) — A type that specifies the information to render a widget at a specific relevance configuration.
- [WidgetRelevance](widgetrelevance.md) — A type collecting the relevances for a widget kind.
- [WidgetRelevanceAttribute](widgetrelevanceattribute.md) — A type that describes when a specific widget could be relevant.
- [WidgetRelevanceGroup](widgetrelevancegroup.md) — A type for configuring widget behavior in the watchOS Smart Stack.
- [AppIntentRecommendation](appintentrecommendation.md) — An object that describes a recommended intent configuration for a user-customizable widget.
- [IntentConfiguration](intentconfiguration.md) — An object describing the content of a widget that uses a custom intent definition to provide user-configurable options.
- [IntentRecommendation](intentrecommendation.md) — An object that describes a recommended intent configuration for a user-customizable widget.
