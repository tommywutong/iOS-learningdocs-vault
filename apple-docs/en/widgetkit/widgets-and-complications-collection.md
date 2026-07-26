---
title: Widgets and watch complications
framework: WidgetKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/widgets-and-complications-collection
source_url: 'https://developer.apple.com/documentation/widgetkit/widgets-and-complications-collection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgets-and-complications-collection.json'
content_hash: 'sha256:cfb25b80f8a67e32'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# Widgets and watch complications

<sub>API Collection</sub>

Allow people to personalize their devices, view relevant information, and perform interactions with widgets and watch complications.

## Overview

Use WidgetKit to create widgets and watch complications that elevate a small amount of timely, personally relevant information from your app and allow people to perform quick actions without launching your app:

- On iPhone and iPad, people put widgets in Today View, on the Home Screen, and on the Lock Screen.
- On Mac, people place macOS widgets and widgets from a paired iPhone in locations like the Mac desktop and in Notification Center.
- On Apple Watch, widgets appear in the Smart Stack and as watch complications.
- On Apple Vision Pro, widgets become three-dimensional objects that people pin to horizontal and vertical surfaces.
- In CarPlay, people configure iPhone widgets to appear on the widgets screen.

## Topics

### Widget creation

- [Creating a widget extension](creating-a-widget-extension.md) — Display your app’s content in a convenient, informative widget on various devices.
- [Developing a WidgetKit strategy](developing-a-widgetkit-strategy.md) — Explore features, tasks, related frameworks, and constraints as you make a plan to implement widgets, controls, watch complications, and Live Activities.
- [Emoji Rangers: Supporting Live Activities, interactivity, and animations](emoji-rangers-supporting-live-activities-interactivity-and-animations.md) — Offer Live Activities, controls, animate data updates, and add interactivity to widgets.
- [Preparing widgets for additional platforms, contexts, and appearances](preparing-widgets-for-additional-contexts-and-appearances.md) — Create widgets that support additional platforms and adapt to their context.
- [Widget](../swiftui/widget.md) — The configuration and content of a widget to display on the Home screen or in Notification Center.
- [WidgetFamily](widgetfamily.md) — Values that define the widget’s size and shape.
- [StaticConfiguration](staticconfiguration.md) — An object describing the content of a widget that has no user-configurable options.

### Configurable widgets

- [Making a configurable widget](making-a-configurable-widget.md) — Give people the option to customize their widgets by adding a custom app intent to your project.
- [Migrating widgets from SiriKit Intents to App Intents](migrating-from-sirikit-intents-to-app-intents.md) — Configure your widgets for backward compatibility.
- [AppIntentConfiguration](appintentconfiguration.md) — An object describing the content of a widget that uses a custom intent to provide user-configurable options.
- [WidgetInfo](widgetinfo.md) — A structure that contains information about user-configured widgets.

### Layout and presentation

- [Supporting additional widget sizes](supporting-additional-widget-sizes.md) — Offer widgets in additional contexts by adding support for various widget sizes.
- [Displaying the right widget background](displaying-the-right-widget-background.md) — Group your widget’s background views and mark them as removable to ensure your widget appears correctly for each context and platform.
- [Optimizing your widget for accented rendering mode and Liquid Glass](optimizing-your-widget-for-accented-rendering-mode-and-liquid-glass.md) — Make your widget feel at home on Apple platforms and Liquid Glass by using accented rendering mode.
- [Adding StandBy and CarPlay support to your widget](adding-standby-and-carplay-support-to-your-widget.md) — Ensure that your small system family widget works well in StandBy and CarPlay.
- [WidgetRenderingMode](widgetrenderingmode.md) — Constants that indicate the rendering mode for a widget.
- [WidgetAccentedRenderingMode](widgetaccentedrenderingmode.md) — Constants that indicate the rendering mode for an `Image` in when displayed in a widget in [accented](widgetrenderingmode/accented.md) mode.
- [AccessoryWidgetBackground](accessorywidgetbackground.md) — An adaptive background view that provides a standard appearance based on the the widget’s environment.
- [WidgetLocation](widgetlocation.md) — Values that indicate different widget locations.

### Timeline updates

- [Keeping a widget up to date](keeping-a-widget-up-to-date.md) — Plan your widget’s timeline to show timely, relevant information using dynamic views, and update the timeline when things change.
- [TimelineProvider](timelineprovider.md) — A type that advises WidgetKit when to update a widget’s display.
- [AppIntentTimelineProvider](appintenttimelineprovider.md) — A type that advises WidgetKit when to update a user-configurable widget’s display.
- [IntentTimelineProvider](intenttimelineprovider.md) — A type that advises WidgetKit when to update a user-configurable widget’s display.
- [TimelineProviderContext](timelineprovidercontext.md) — An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.
- [TimelineEntry](timelineentry.md) — A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [Timeline](timeline.md) — An object that specifies a date for WidgetKit to update a widget’s view.
- [WidgetCenter](widgetcenter.md) — An object that contains a list of user-configured widgets and is used for reloading widget timelines.

### Push notification updates

- [Updating widgets with WidgetKit push notifications](updating-widgets-with-widgetkit-push-notifications.md) — Use WidgetKit to receive push tokens and reload your widgets with remote push notifications.
- [WidgetPushHandler](widgetpushhandler.md) — A type that can receive push information about widget refreshes and relevance refreshes.
- [WidgetPushInfo](widgetpushinfo.md) — A structure that contains information about the push token for updating widgets and widget relevances.

### Capabilities

- [Accessing location information in widgets](accessing-location-information-in-widgets.md) — Incorporate location information into your widget presentation to make it more relevant and contextual.
- [Making network requests in a widget extension](making-network-requests-in-a-widget-extension.md) — Update your widget with new information you fetch with a network request.

### Debugging

- [Previewing widgets and Live Activities in Xcode](previewing-widgets-and-live-activities-in-xcode.md) — Use Xcode previews to iteratively develop, fine-tune, and troubleshoot widgets and Live Activities.
- [Preview macros](preview-macros.md) — Use Swift macros to create widget previews in Xcode.
- [WidgetPreviewContext](widgetpreviewcontext.md) — A specification for the context of a widget preview.
- [Debugging widgets](debugging-widgets.md) — Set environment variables in Xcode to control your widget’s configuration in the debugger.

### visionOS widgets

- [Updating your widgets for visionOS](updating-your-widgets-for-visionos.md) — Choose widget styles specific to visionOS, support recessed and elevated appearances, and add proximity awareness to your widget.
- [widgetTexture(_:)](<../swiftui/widgetconfiguration/widgettexture(__).md>) — Specifies the widget texture for this widget.
- [WidgetTexture](widgettexture.md) — Values that define the texture of the widget’s coating layer.
- [supportedMountingStyles(_:)](<../swiftui/widgetconfiguration/supportedmountingstyles(__).md>) — Specifies the mounting style for this widget.
- [WidgetMountingStyle](widgetmountingstyle.md) — Values that define the widget’s supported mounting style.
- [LevelOfDetail](levelofdetail.md) — The level of detail the view is recommended to have.

### Accessory and watchOS widgets

- [Creating accessory widgets and watch complications](creating-accessory-widgets-and-watch-complications.md) — Support accessory widgets that appear on the Lock Screen and as complications on Apple Watch.
- [AccessoryWidgetGroup](accessorywidgetgroup.md) — A view type that has a label at the top and three content views masked with a circle or rounded square.
- [AccessoryWidgetGroupStyle](accessorywidgetgroupstyle.md) — The style for an [AccessoryWidgetGroup](accessorywidgetgroup.md) view.
- [Migrating ClockKit complications to WidgetKit](converting-a-clockkit-app.md) — Leverage WidgetKit’s API to create watchOS complications using SwiftUI.

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
- [IntentRecommendation](intentrecommendation.md) — An object that describes a recommended intent configuration for a user-customizable widget.

## See Also

### System experiences

- [Live Activities](liveactivities-collection.md) — Let people track updates from your app with Live Activities.
- [Controls](controls-collection.md) — Offer controls that people place in Control Center, on the Lock Screen, and on the Action button to quickly perform an action from your app.
