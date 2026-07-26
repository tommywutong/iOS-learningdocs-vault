---
title: IntentConfiguration
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/intentconfiguration
source_url: 'https://developer.apple.com/documentation/widgetkit/intentconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/intentconfiguration.json'
content_hash: 'sha256:a7a2dd4441f93455'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# IntentConfiguration

<sub>Structure</sub>

An object describing the content of a widget that uses a custom intent definition to provide user-configurable options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct IntentConfiguration<Intent, Content> where Intent : INIntent, Content : View
```

## Overview

The following example shows the configuration for a game widget that displays details about a chosen character.

```swift
struct CharacterDetailWidget: Widget {
    var body: some WidgetConfiguration {
        IntentConfiguration(
            kind: "com.mygame.character-detail",
            intent: SelectCharacterIntent.self,
            provider: CharacterDetailProvider(),
        ) { entry in
            CharacterDetailView(entry: entry)
        }
        .configurationDisplayName("Character Details")
        .description("Displays a character's health and other details")
        .supportedFamilies([.systemSmall, .systemMedium, .systemLarge])
    }
}
```

Every widget has a unique `kind`, a string that you choose. You use this string to identify your widget when reloading its timeline with [WidgetCenter](widgetcenter.md).

The `intent` is a custom SiriKit intent definition containing user-editable parameters.

The timeline provider is an object that determines the timeline for refreshing your widget. Providing future dates for updating your widget allows the system to optimize the refresh process.

The content closure contains the SwiftUI views that WidgetKit needs to render the widget. When WidgetKit invokes the content closure, it passes a timeline entry created by the widget provider’s [getSnapshot(for:in:completion:)](<intenttimelineprovider/getsnapshot(for_in_completion_).md>) or [getTimeline(for:in:completion:)](<intenttimelineprovider/gettimeline(for_in_completion_).md>) method.

Modifiers let you specify the families your widget supports, and the details shown when users add or edit their widgets.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [WidgetConfiguration](../swiftui/widgetconfiguration.md)

## Topics

### Creating a widget configuration

- [init(kind:intent:provider:content:)](<intentconfiguration/init(kind_intent_provider_content_).md>) — Creates a configuration for a widget by using a custom intent definition to provide user-configurable options.
- [body](../swiftui/widgetconfiguration/body-swift.property.md) — The content and behavior of this widget.

### Setting the display name

- [configurationDisplayName(_:)](<../swiftui/widgetconfiguration/configurationdisplayname(__)-2c3zv.md>) — Sets the name shown for a widget when a user adds or edits it using the specified string.
- [configurationDisplayName(_:)](<../swiftui/widgetconfiguration/configurationdisplayname(__)-3sbn4.md>) — Sets the name shown for a widget when a user adds or edits it using the contents of a text view.
- [configurationDisplayName(_:)](<../swiftui/widgetconfiguration/configurationdisplayname(__)-4v9q.md>) — Sets the localized name shown for a widget when a user adds or edits the widget.

### Setting the description

- [description(_:)](<../swiftui/widgetconfiguration/description(__)-1bvuj.md>) — Sets the description shown for a widget when a user adds or edits it using the contents of a text view.
- [description(_:)](<../swiftui/widgetconfiguration/description(__)-2bfr.md>) — Sets the description shown for a widget when a user adds or edits it using the specified string.
- [description(_:)](<../swiftui/widgetconfiguration/description(__)-4q9pa.md>) — Sets the localized description shown for a widget when a user adds or edits the widget.

### Setting the supported families

- [supportedFamilies(_:)](<../swiftui/widgetconfiguration/supportedfamilies(__).md>) — Sets the sizes that a widget supports.

### Handling background network requests

- [backgroundTask(_:action:)](<../swiftui/widgetconfiguration/backgroundtask(__action_).md>) — Runs the given action when the system provides a background task.
- [onBackgroundURLSessionEvents(matching:_:)](<../swiftui/widgetconfiguration/onbackgroundurlsessionevents(matching___)-2e152.md>) — Adds an action to perform when events related to a URL session identified by a closure are waiting to be processed.
- [onBackgroundURLSessionEvents(matching:_:)](<../swiftui/widgetconfiguration/onbackgroundurlsessionevents(matching___)-fw6x.md>) — Adds an action to perform when events related to a URL session with a matching identifier are waiting to be processed.

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
- [IntentRecommendation](intentrecommendation.md) — An object that describes a recommended intent configuration for a user-customizable widget.
