---
title: TimelineEntryRelevance
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/timelineentryrelevance
source_url: 'https://developer.apple.com/documentation/widgetkit/timelineentryrelevance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/timelineentryrelevance.json'
content_hash: 'sha256:49859eb59b5299ea'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# TimelineEntryRelevance

<sub>Structure</sub>

An object that describes the relative importance of a timeline entry compared to other entries in the current and past timelines.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
struct TimelineEntryRelevance
```

## Overview

When users put widgets into a Smart Stack, WidgetKit uses the [relevance](timelineentry/relevance.md) property of the entries your timeline provider generates to determine how relevant they are to the user. For each timeline entry that your provider creates, you may assign relevance that contains a [score](timelineentryrelevance/score.md) and a [duration](timelineentryrelevance/duration.md). The score is a value you choose that indicates the relevance of the widget, relative to entries across timelines that the provider creates. When the date of an entry arrives, and for the duration you specify, WidgetKit may rotate your widget to the top of the stack so it becomes visible.

A timeline entry’s assigned relevance isn’t the only factor that determines whether WidgetKit rotates your widget to the top of the Smart Stack. For more information, see [Increasing the visibility of widgets in Smart Stacks](widget-suggestions-in-smart-stacks.md).

## Relationships

- **Conforms To**: [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a Relevance Object

- [init(score:duration:)](<timelineentryrelevance/init(score_duration_).md>) — Creates an object that represents the importance of a widget and the length of time for WidgetKit to consider it for rotation to the top of the stack.

### Configuring Relevance Properties

- [duration](timelineentryrelevance/duration.md) — The number of seconds, following an entry’s date, that WidgetKit considers the widget for rotation to the top of the stack.
- [score](timelineentryrelevance/score.md) — A value that indicates the relevance of an entry compared to other entries in the current and past timelines.

## See Also

### Smart Stacks

- [Increasing the visibility of widgets in Smart Stacks](widget-suggestions-in-smart-stacks.md) — Provide contextual information and donate intents to the system to make sure your widget appears prominently in Smart Stacks.
- [RelevanceConfiguration](relevanceconfiguration.md) — A type that describes the content of a widget that uses relevance clues.
- [RelevanceEntriesProvider](relevanceentriesprovider.md) — A type that provides the content for a widget that uses relevance clues to display information in the Smart Stack.
- [RelevanceEntry](relevanceentry.md) — A type that specifies the information to render a widget at a specific relevance configuration.
- [WidgetRelevance](widgetrelevance.md) — A type collecting the relevances for a widget kind.
- [WidgetRelevanceAttribute](widgetrelevanceattribute.md) — A type that describes when a specific widget could be relevant.
- [WidgetRelevanceGroup](widgetrelevancegroup.md) — A type for configuring widget behavior in the watchOS Smart Stack.
- [AppIntentRecommendation](appintentrecommendation.md) — An object that describes a recommended intent configuration for a user-customizable widget.
- [IntentConfiguration](intentconfiguration.md) — An object describing the content of a widget that uses a custom intent definition to provide user-configurable options.
- [IntentRecommendation](intentrecommendation.md) — An object that describes a recommended intent configuration for a user-customizable widget.
