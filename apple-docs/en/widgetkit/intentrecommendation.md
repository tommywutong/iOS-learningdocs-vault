---
title: IntentRecommendation
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/intentrecommendation
source_url: 'https://developer.apple.com/documentation/widgetkit/intentrecommendation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/intentrecommendation.json'
content_hash: 'sha256:88f3a535a33aaf42'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# IntentRecommendation

<sub>Structure</sub>

An object that describes a recommended intent configuration for a user-customizable widget.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
struct IntentRecommendation<T> where T : INIntent
```

## Overview

By adding a custom SiriKit intent definition to your project and using an [IntentTimelineProvider](intenttimelineprovider.md), you allow users to configure widgets to show data that’s most relevant to them. Some platforms don’t have a dedicated user interface to configure all of your intent parameters. For example, watchOS doesn’t offer a dedicated user interface to configure data that appears on a complication. Use intent recommendations in watchOS to offer preconfigured complications that show data that’s most relevant to the user.

> [!note] Note
> On platforms that offer a dedicated user interface for configuring widgets — for example, iOS or macOS — `IntentRecommendation` is inactive.

For example, say you develop a game app that allows users to view their in-game character. With intent recommendations, you can recommend an intent configuration for a watch complication that displays character information.

The following example shows a function to create a list of recommended configurations for a game widget that shows current energy levels for a game character.

```swift
public func recommendations() -> [IntentRecommendation<DynamicCharacterSelectionIntent>] {
    return CharacterDetail.availableCharacters.
        map { character in
            let hero = Hero(identifier: character.name, display: character.name)
            let intent = DynamicCharacterSelectionIntent()
            intent.hero = hero

            return IntentRecommendation(intent: intent, description: Text(character.name))
        }
    }
```

## Topics

### Creating a Recommended Widget Configuration

- [init(intent:description:)](<intentrecommendation/init(intent_description_)-1zh33.md>) — Creates a recommended configuration for a widget on platforms that don’t offer a dedicated user interface to customize widgets with a localized description.
- [init(intent:description:)](<intentrecommendation/init(intent_description_)-4epo2.md>) — Creates a recommended configuration for a widget on platforms that don’t offer a dedicated user interface to customize widgets.
- [init(intent:description:)](<intentrecommendation/init(intent_description_)-6v7dj.md>) — Creates a recommended configuration for a widget on platforms that don’t offer a dedicated user interface to customize widgets.

### Initializers

- [init(intent:description:)](<intentrecommendation/init(intent_description_)-6o8yy.md>) — Creates a recommended configuration for a widget on platforms that don’t offer a dedicated user interface to customize widgets with a localized description.

## See Also

### Smart Stacks

- [Increasing the visibility of widgets in Smart Stacks](widget-suggestions-in-smart-stacks.md) — Provide contextual information and donate intents to the system to make sure your widget appears prominently in Smart Stacks.
- [TimelineEntryRelevance](timelineentryrelevance.md) — An object that describes the relative importance of a timeline entry compared to other entries in the current and past timelines.
- [RelevanceConfiguration](relevanceconfiguration.md) — A type that describes the content of a widget that uses relevance clues.
- [RelevanceEntriesProvider](relevanceentriesprovider.md) — A type that provides the content for a widget that uses relevance clues to display information in the Smart Stack.
- [RelevanceEntry](relevanceentry.md) — A type that specifies the information to render a widget at a specific relevance configuration.
- [WidgetRelevance](widgetrelevance.md) — A type collecting the relevances for a widget kind.
- [WidgetRelevanceAttribute](widgetrelevanceattribute.md) — A type that describes when a specific widget could be relevant.
- [WidgetRelevanceGroup](widgetrelevancegroup.md) — A type for configuring widget behavior in the watchOS Smart Stack.
- [AppIntentRecommendation](appintentrecommendation.md) — An object that describes a recommended intent configuration for a user-customizable widget.
- [IntentConfiguration](intentconfiguration.md) — An object describing the content of a widget that uses a custom intent definition to provide user-configurable options.
