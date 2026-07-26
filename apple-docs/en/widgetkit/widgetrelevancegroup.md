---
title: WidgetRelevanceGroup
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 26.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/widgetrelevancegroup
source_url: 'https://developer.apple.com/documentation/widgetkit/widgetrelevancegroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetrelevancegroup.json'
content_hash: 'sha256:97df9e5ac145c0dc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# WidgetRelevanceGroup

<sub>Structure</sub>

A type for configuring widget behavior in the watchOS Smart Stack.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
struct WidgetRelevanceGroup
```

## Overview

Use `WidgetRelevanceGroup` alongside [WidgetRelevanceAttribute](widgetrelevanceattribute.md) to tell the system how it should group your widgets in the watchOS Smart Stack. The system may provide a default grouping mechanism for widgets in the Smart Stack; for example, per-app grouping. Creating a relevance group and choosing the `.ungrouped` option opts out of default grouping behavior. For additional information about widgets in Smart Stacks, refer to [Increasing the visibility of widgets in Smart Stacks](widget-suggestions-in-smart-stacks.md).

## Topics

### Type Properties

- [automatic](widgetrelevancegroup/automatic.md) — Specifies that the widget group should use the automatic grouping behavior provided the system.
- [ungrouped](widgetrelevancegroup/ungrouped.md) — Don’t use the system’s default behavior for grouping widgets.

### Type Methods

- [named(_:)](<widgetrelevancegroup/named(__).md>) — Creates a group with the provided name.

## See Also

### Smart Stacks

- [Increasing the visibility of widgets in Smart Stacks](widget-suggestions-in-smart-stacks.md) — Provide contextual information and donate intents to the system to make sure your widget appears prominently in Smart Stacks.
- [TimelineEntryRelevance](timelineentryrelevance.md) — An object that describes the relative importance of a timeline entry compared to other entries in the current and past timelines.
- [RelevanceConfiguration](relevanceconfiguration.md) — A type that describes the content of a widget that uses relevance clues.
- [RelevanceEntriesProvider](relevanceentriesprovider.md) — A type that provides the content for a widget that uses relevance clues to display information in the Smart Stack.
- [RelevanceEntry](relevanceentry.md) — A type that specifies the information to render a widget at a specific relevance configuration.
- [WidgetRelevance](widgetrelevance.md) — A type collecting the relevances for a widget kind.
- [WidgetRelevanceAttribute](widgetrelevanceattribute.md) — A type that describes when a specific widget could be relevant.
- [AppIntentRecommendation](appintentrecommendation.md) — An object that describes a recommended intent configuration for a user-customizable widget.
- [IntentConfiguration](intentconfiguration.md) — An object describing the content of a widget that uses a custom intent definition to provide user-configurable options.
- [IntentRecommendation](intentrecommendation.md) — An object that describes a recommended intent configuration for a user-customizable widget.
