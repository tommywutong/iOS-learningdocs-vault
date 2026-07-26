---
title: Adding StandBy and CarPlay support to your widget
framework: WidgetKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/adding-standby-and-carplay-support-to-your-widget
source_url: 'https://developer.apple.com/documentation/widgetkit/adding-standby-and-carplay-support-to-your-widget'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/adding-standby-and-carplay-support-to-your-widget.json'
content_hash: 'sha256:5842447616b99bb7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md) · [Widgets and watch complications](widgets-and-complications-collection.md)

# Adding StandBy and CarPlay support to your widget

<sub>Article</sub>

Ensure that your small system family widget works well in StandBy and CarPlay.

## Overview

People can choose your small system family widgets from the widget gallery in StandBy or CarPlay:

- **On iPhone in StandBy** — The Lock Screen shows two widgets side by side on a dark background. WidgetKit uses your [WidgetFamily.systemSmall](widgetfamily/systemsmall.md) widget and scales it to fit half of the screen.
- **In CarPlay** — Widgets appear in one or more stacks to the left of the CarPlay Home Screen, in full color and with the background removed.

Because widgets in StandBy appear similar to widgets in CarPlay, when you ensure your widget supports one, it automatically supports the other. To support StandBy and CarPlay appearances, update your small widget:

- Make the background removable.
- Focus on showing only glanceable information.
- Use larger typography, and make it easy to read from a distance.

For more information about making a background removable and optimizing your widget for additional contexts, refer to [Update your small widget to support StandBy and CarPlay](preparing-widgets-for-additional-contexts-and-appearances.md#Update-your-small-widget-to-support-StandBy-and-CarPlay).

If your widget isn’t a good fit for StandBy or CarPlay, consider marking the applicable context as a disfavored location as described in [Indicate that a widget might not fit a specific context](preparing-widgets-for-additional-contexts-and-appearances.md#Indicate-that-a-widget-might-not-fit-a-specific-context). Doing so doesn’t exclude your widget from CarPlay or StandBy, but it communicates to people that these locations aren’t the best fit.

### Linking to your app in CarPlay and using buttons or toggles

In CarPlay, the way your widget links to your app depends on the specific context of using your app in a vehicle:

- If the vehicle supports touch input and your app supports CarPlay integration, tapping the widget opens the app’s CarPlay template, and tapping a button or toggle performs its action.
- If the vehicle supports touch input but your app doesn’t integrate with CarPlay, people can’t open your app from the widget and the system dims it to indicate that a tap doesn’t have an effect.
- If the vehicle doesn’t support touch input, people can’t open your app from the widget.

For additional information about linking to your app from your widget, refer to [Review linking behavior in CarPlay](linking-to-specific-app-scenes-from-your-widget-or-live-activity.md#Review-linking-behavior-in-CarPlay).

| Vehicle features | Buttons and toggles functional | Open the app from a tap |
|---|---|---|
| Touchscreen display available | Yes | Yes, requires your app to offer CarPlay integration |
| Display without touchscreen capabilities | No | No |

Additionally, your widget’s buttons and toggles behave differently to match the CarPlay context:

- If the vehicle supports touch input, people tap a widget’s buttons and toggles to perform their functionality.
- If the vehicle doesn’t have a touchscreen, widgets and buttons are inactive, and people can’t tap the widget to open your app in CarPlay or on their phone.

> [!note] Note
> CarPlay integration is only available to apps with specific functionality. For more information, see [CarPlay](../carplay.md).

### Test widgets in CarPlay

To test widgets in CarPlay, preview your widget in Xcode to verify that your widget works in StandBy and the CarPlay Simulator. For more information, refer to [Previewing widgets and Live Activities in Xcode](previewing-widgets-and-live-activities-in-xcode.md) and [Using the CarPlay Simulator](../carplay/using-the-carplay-simulator.md).

## See Also

### Layout and presentation

- [Supporting additional widget sizes](supporting-additional-widget-sizes.md) — Offer widgets in additional contexts by adding support for various widget sizes.
- [Displaying the right widget background](displaying-the-right-widget-background.md) — Group your widget’s background views and mark them as removable to ensure your widget appears correctly for each context and platform.
- [Optimizing your widget for accented rendering mode and Liquid Glass](optimizing-your-widget-for-accented-rendering-mode-and-liquid-glass.md) — Make your widget feel at home on Apple platforms and Liquid Glass by using accented rendering mode.
- [WidgetRenderingMode](widgetrenderingmode.md) — Constants that indicate the rendering mode for a widget.
- [WidgetAccentedRenderingMode](widgetaccentedrenderingmode.md) — Constants that indicate the rendering mode for an `Image` in when displayed in a widget in [accented](widgetrenderingmode/accented.md) mode.
- [AccessoryWidgetBackground](accessorywidgetbackground.md) — An adaptive background view that provides a standard appearance based on the the widget’s environment.
- [WidgetLocation](widgetlocation.md) — Values that indicate different widget locations.
