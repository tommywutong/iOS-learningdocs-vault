---
title: WidgetRelevanceAttribute
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 26.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/widgetrelevanceattribute
source_url: 'https://developer.apple.com/documentation/widgetkit/widgetrelevanceattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetrelevanceattribute.json'
content_hash: 'sha256:e7979b42bacd413e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# WidgetRelevanceAttribute

<sub>Structure</sub>

A type that describes when a specific widget could be relevant.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
struct WidgetRelevanceAttribute<Configuration>
```

## Overview

Use the relevance attribute’s `RelevantContext` to describe when a specific widget might be relevant.

## Topics

### Initializers

- [init(configuration:context:)](<widgetrelevanceattribute/init(configuration_context_)-8325r.md>) — Creates a new widget relevance for a specific configuration that is relevant in a specific context.
- [init(configuration:context:)](<widgetrelevanceattribute/init(configuration_context_)-8jxhs.md>) — Creates a new widget relevance for a specific configuration that is relevant in a specific context.
- [init(configuration:group:)](<widgetrelevanceattribute/init(configuration_group_)-5yh17.md>) — Associates the widget kind with a group. When multiple widgets are in the same group, the system will only suggest one member of the group simultaneously. Widgets in the same group are interpreted to contain redundant information, and therefore should not be presented together.
- [init(configuration:group:)](<widgetrelevanceattribute/init(configuration_group_)-93jm5.md>) — Associates the widget kind with a group. When multiple widgets are in the same group, the system will only suggest one member of the group simultaneously. Widgets in the same group are interpreted to contain redundant information, and therefore should not be presented together.
- [init(context:)](<widgetrelevanceattribute/init(context_).md>) — Creates a new widget relevance that is relevant in a specific context.
- [init(group:)](<widgetrelevanceattribute/init(group_).md>) — Associates the widget kind with a group. When multiple widgets are in the same group, the system only suggests one member of the group simultaneously. Widgets in the same group are interpreted to contain redundant information, and therefore should not be presented together.

## See Also

### Smart Stacks

- [Increasing the visibility of widgets in Smart Stacks](widget-suggestions-in-smart-stacks.md) — Provide contextual information and donate intents to the system to make sure your widget appears prominently in Smart Stacks.
- [TimelineEntryRelevance](timelineentryrelevance.md) — An object that describes the relative importance of a timeline entry compared to other entries in the current and past timelines.
- [RelevanceConfiguration](relevanceconfiguration.md) — A type that describes the content of a widget that uses relevance clues.
- [RelevanceEntriesProvider](relevanceentriesprovider.md) — A type that provides the content for a widget that uses relevance clues to display information in the Smart Stack.
- [RelevanceEntry](relevanceentry.md) — A type that specifies the information to render a widget at a specific relevance configuration.
- [WidgetRelevance](widgetrelevance.md) — A type collecting the relevances for a widget kind.
- [WidgetRelevanceGroup](widgetrelevancegroup.md) — A type for configuring widget behavior in the watchOS Smart Stack.
- [AppIntentRecommendation](appintentrecommendation.md) — An object that describes a recommended intent configuration for a user-customizable widget.
- [IntentConfiguration](intentconfiguration.md) — An object describing the content of a widget that uses a custom intent definition to provide user-configurable options.
- [IntentRecommendation](intentrecommendation.md) — An object that describes a recommended intent configuration for a user-customizable widget.
