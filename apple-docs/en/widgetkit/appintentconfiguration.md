---
title: AppIntentConfiguration
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 26.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/appintentconfiguration
source_url: 'https://developer.apple.com/documentation/widgetkit/appintentconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/appintentconfiguration.json'
content_hash: 'sha256:dafbb56d350959de'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# AppIntentConfiguration

<sub>Structure</sub>

An object describing the content of a widget that uses a custom intent to provide user-configurable options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct AppIntentConfiguration<Intent, Content> where Intent : WidgetConfigurationIntent, Content : View
```

## Overview

The following example shows the configuration for a game widget that displays details about a chosen character.

```swift
struct CharacterDetailWidget: Widget {
    var body: some WidgetConfiguration {
        AppIntentConfiguration(
            kind: "com.mygame.character-detail",
            intent: SelectCharacterIntent.self,
            provider: CharacterDetailProvider(),
        ) { entry in
            CharacterDetailView(entry: entry)
        }
        .supportedFamilies([.systemSmall, .systemMedium, .systemLarge])
    }
}
```

Every widget has a unique `kind`, a string that you choose. You use this string to identify your widget when reloading its timeline with [WidgetCenter](widgetcenter.md).

The `intent` is a custom App Intent containing user-editable parameters.

The timeline provider is an object that determines the timeline for refreshing your widget. Providing future dates for updating your widget allows the system to optimize the refresh process.

The content closure contains the SwiftUI views that WidgetKit needs to render the widget. When WidgetKit invokes the content closure, it passes a timeline entry created by the widget provider’s [snapshot(for:in:)](<appintenttimelineprovider/snapshot(for_in_).md>) or [timeline(for:in:)](<appintenttimelineprovider/timeline(for_in_).md>) method.

Modifiers let you specify the families your widget supports, and the details shown when users add or edit their widgets.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [WidgetConfiguration](../swiftui/widgetconfiguration.md)

## Topics

### Creating a widget configuration

- [init(kind:intent:provider:content:)](<appintentconfiguration/init(kind_intent_provider_content_).md>) — Creates a configuration for a widget by using a custom intent to provide user-configurable options.
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

### Configurable widgets

- [Making a configurable widget](making-a-configurable-widget.md) — Give people the option to customize their widgets by adding a custom app intent to your project.
- [Migrating widgets from SiriKit Intents to App Intents](migrating-from-sirikit-intents-to-app-intents.md) — Configure your widgets for backward compatibility.
- [WidgetInfo](widgetinfo.md) — A structure that contains information about user-configured widgets.
