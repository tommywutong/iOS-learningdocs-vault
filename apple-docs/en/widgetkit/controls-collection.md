---
title: Controls
framework: WidgetKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/controls-collection
source_url: 'https://developer.apple.com/documentation/widgetkit/controls-collection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/controls-collection.json'
content_hash: 'sha256:32110c43899cfe53'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# Controls

<sub>API Collection</sub>

Offer controls that people place in Control Center, on the Lock Screen, and on the Action button to quickly perform an action from your app.

## Overview

Controls act as a button that initiates an action from your app or opens your app to a specific view, or as a toggle. A toggle can turn a light on and off, or open and close a garage door. People place controls in prominent locations to personalize how they use their devices:

- On devices with an Action button, people can place a controls action in the Action button.
- On iPhone and iPad, people place controls in Control Center and on the Lock Screen.
- On Mac, people place controls from your macOS app in Control Center or as menu bar items.
- On Apple Watch, people place controls from your watchOS app or from a paired iPhone in Control Center or the Smart Stack. If you offer watchOS app in addition to an iPhone app and both apps offer controls, people can only place controls from your watchOS app in Control Center or the Smart Stack.

To offer a control for your app, use WidgetKit API to configure and update the control,  create its layout with [SwiftUI](../swiftui.md), and perform its action using [App Intents](../appintents.md). For more information about the App Intents framework, refer to [Getting started with the App Intents framework](../appintents/getting-started-with-the-app-intents-framework.md).

## Topics

### Essentials

- [Developing a WidgetKit strategy](developing-a-widgetkit-strategy.md) — Explore features, tasks, related frameworks, and constraints as you make a plan to implement widgets, controls, watch complications, and Live Activities.
- [Creating a widget extension](creating-a-widget-extension.md) — Display your app’s content in a convenient, informative widget on various devices.
- [Emoji Rangers: Supporting Live Activities, interactivity, and animations](emoji-rangers-supporting-live-activities-interactivity-and-animations.md) — Offer Live Activities, controls, animate data updates, and add interactivity to widgets.

### Setup and configuration

- [Creating controls to perform actions across the system](creating-controls-to-perform-actions-across-the-system.md) — Perform your app’s actions from Control Center, the Lock Screen, and the Action button.
- [Adding refinements and configuration to controls](adding-refinements-and-configuration-to-controls.md) — Customize the way controls display across the system and offer people the ability to configure them.
- [StaticControlConfiguration](staticcontrolconfiguration.md) — The description of a control that has no user-configurable options.
- [AppIntentControlConfiguration](appintentcontrolconfiguration.md) — The description of a control that uses a custom app intent to provide user-configurable options.
- [ControlCenter](controlcenter.md) — An object you use to access configuration information for controls and reload them.
- [ControlInfo](controlinfo.md) — A structure that contains information about user-configured controls.
- [ControlWidgetButton](controlwidgetbutton.md) — A control template representing a button.
- [ControlWidgetToggle](controlwidgettoggle.md) — A control template representing a toggle.

### Updates

- [Updating controls locally and remotely](updating-controls-locally-and-remotely.md) — Update and reload controls from your app or using push notifications.
- [ControlPushHandler](controlpushhandler.md) — A type that can receive push information about user-configured controls.
- [ControlPushInfo](controlpushinfo.md) — A structure that contains information about the push token of a user-configured control.

### Previews

- [ControlValueProvider](controlvalueprovider.md) — A type that provides a value to a control template.
- [AppIntentControlValueProvider](appintentcontrolvalueprovider.md) — A type that uses a custom intent to provide a value to a control template.

## See Also

### System experiences

- [Widgets and watch complications](widgets-and-complications-collection.md) — Allow people to personalize their devices, view relevant information, and perform interactions with widgets and watch complications.
- [Live Activities](liveactivities-collection.md) — Let people track updates from your app with Live Activities.
