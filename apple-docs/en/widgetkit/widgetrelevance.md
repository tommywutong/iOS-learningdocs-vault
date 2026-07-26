---
title: WidgetRelevance
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 26.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/widgetrelevance
source_url: 'https://developer.apple.com/documentation/widgetkit/widgetrelevance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetrelevance.json'
content_hash: 'sha256:6e8433f4e60efb12'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# WidgetRelevance

<sub>Structure</sub>

A type collecting the relevances for a widget kind.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
struct WidgetRelevance<Configuration>
```

## Overview

Return this type from the `relevance()` requirement of your [TimelineProvider](timelineprovider.md), [AppIntentTimelineProvider](appintenttimelineprovider.md), or [IntentTimelineProvider](intenttimelineprovider.md) to inform the system of when a widget might be relevant and in which configuration.

Make sure to return the relevances ordered by priority because the system might decide to utilize only a subset of the provided relevances.

## Topics

### Initializers

- [init(_:)](<widgetrelevance/init(__).md>) — Creates a type collecting the relevances for a widget kind.

## See Also

### Smart Stacks

- [Increasing the visibility of widgets in Smart Stacks](widget-suggestions-in-smart-stacks.md) — Provide contextual information and donate intents to the system to make sure your widget appears prominently in Smart Stacks.
- [TimelineEntryRelevance](timelineentryrelevance.md) — An object that describes the relative importance of a timeline entry compared to other entries in the current and past timelines.
- [RelevanceConfiguration](relevanceconfiguration.md) — A type that describes the content of a widget that uses relevance clues.
- [RelevanceEntriesProvider](relevanceentriesprovider.md) — A type that provides the content for a widget that uses relevance clues to display information in the Smart Stack.
- [RelevanceEntry](relevanceentry.md) — A type that specifies the information to render a widget at a specific relevance configuration.
- [WidgetRelevanceAttribute](widgetrelevanceattribute.md) — A type that describes when a specific widget could be relevant.
- [WidgetRelevanceGroup](widgetrelevancegroup.md) — A type for configuring widget behavior in the watchOS Smart Stack.
- [AppIntentRecommendation](appintentrecommendation.md) — An object that describes a recommended intent configuration for a user-customizable widget.
- [IntentConfiguration](intentconfiguration.md) — An object describing the content of a widget that uses a custom intent definition to provide user-configurable options.
- [IntentRecommendation](intentrecommendation.md) — An object that describes a recommended intent configuration for a user-customizable widget.
