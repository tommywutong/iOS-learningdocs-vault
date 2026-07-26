---
title: Displaying the right widget background
framework: WidgetKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/displaying-the-right-widget-background
source_url: 'https://developer.apple.com/documentation/widgetkit/displaying-the-right-widget-background'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/displaying-the-right-widget-background.json'
content_hash: 'sha256:7c1cc23618de94de'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md) · [Widgets and watch complications](widgets-and-complications-collection.md)

# Displaying the right widget background

<sub>Article</sub>

Group your widget’s background views and mark them as removable to ensure your widget appears correctly for each context and platform.

## Overview

Widgets appear differently based on their context, including their background view, for example:

- In the [vibrant](widgetrenderingmode/vibrant.md) appearance, the system removes the background of your widget or renders it with semi-translucent appearance.
- In StandBy on iPhone, the system removes the background of your widget.

To make sure your widget appears correctly, mark your background views as removable for every widget size.

> [!important] Important
> If a widget doesn’t support removable background views or doesn’t explicitly mark a background as nonremovable, the system displays a warning message that overlays the widget during development with Xcode.

To mark your background views as removable:

1. Add the [containerBackground(_:for:)](<../swiftui/view/containerbackground(__for_).md>) modifier to your background views to define the background appearance of your widget and tell WidgetKit that it can remove the view where applicable.
2. Move code that declares any background color or views inside the `containerBackground(for:)` view modifier and pass [widget](../swiftui/containerbackgroundplacement/widget.md) to it. This makes sure WidgetKit automatically removes the background as needed.

The following code snippet from the [Emoji Rangers: Supporting Live Activities, interactivity, and animations](emoji-rangers-supporting-live-activities-interactivity-and-animations.md) sample code project defines a `gameBackground` color for the widget’s container background to make sure WidgetKit renders it with or without the background color as applicable.

```swift
var body: some View {
    switch family {
    // Logic for additional widget sizes.
    case .accessoryRectangular:
        HStack(alignment: .center, spacing: 0) {
            VStack(alignment: .leading) {
                Text(entry.hero.name)
                    .font(.headline)
                    .widgetAccentable()
                Text("Level \(entry.hero.level)")
                Text(entry.hero.fullHealthDate, style: .timer)
            }.frame(maxWidth: .infinity, alignment: .leading)
            Avatar(hero: entry.hero, includeBackground: false)
        }
        .containerBackground(for: .widget) {
            Color.gameBackground
        }
		// Logic for additional widget sizes.
}
```

Marking background views as removable by defining a background container so you can use the same layout and views for your widget across contexts. For example, if you support the rectangular accessory widget size as shown in the code snippet above, WidgetKit renders it with a rich, full-color background in the Smart Stack on Apple Watch and without a background as a watch complication or on the Lock Screen of iPhone and iPad.

On Apple Watch, rectangular widgets in the Smart Stack use a default dark material background. By adding a container background, the widget renders with a background that visually ties it to your app and makes it more recognizable to people.

To detect whether a widget appears with or without a background, use the [showsWidgetContainerBackground](../swiftui/environmentvalues/showswidgetcontainerbackground.md) environment variable.

### Explicitly opt out of background removal

Some widgets don’t have distinct foreground content, and background removal can negatively impact their functionality. For example, a widget might display a photo or map that takes up the entirety of the widget’s bounds. Removing the photo or map removes the functionality of the widget. If this case applies to your widget, set the [containerBackgroundRemovable(_:)](<../swiftui/widgetconfiguration/containerbackgroundremovable(__).md>) modifier to `false` for your widget configuration.

> [!important] Important
> Marking a background as nonremovable excludes your widget from the widget gallery in contexts that require a removable background; for example, on the iPad Lock Screen and in StandBy.

### Set the background color of accessory widgets

Depending on your accessory widget or complication, you may need to set a consistent background for your accessory widget. Use [AccessoryWidgetBackground](accessorywidgetbackground.md) to draw a consistent background for your widget, as shown in the following example. It creates a view that’s similar to the circular Lock Screen widget that the Calendar app offers:

```swift
ZStack {
     AccessoryWidgetBackground()
     VStack {
        Text(“MON”)
        Text(“6”)
         .font(.title)
    }
}
```

## See Also

### Layout and presentation

- [Supporting additional widget sizes](supporting-additional-widget-sizes.md) — Offer widgets in additional contexts by adding support for various widget sizes.
- [Optimizing your widget for accented rendering mode and Liquid Glass](optimizing-your-widget-for-accented-rendering-mode-and-liquid-glass.md) — Make your widget feel at home on Apple platforms and Liquid Glass by using accented rendering mode.
- [Adding StandBy and CarPlay support to your widget](adding-standby-and-carplay-support-to-your-widget.md) — Ensure that your small system family widget works well in StandBy and CarPlay.
- [WidgetRenderingMode](widgetrenderingmode.md) — Constants that indicate the rendering mode for a widget.
- [WidgetAccentedRenderingMode](widgetaccentedrenderingmode.md) — Constants that indicate the rendering mode for an `Image` in when displayed in a widget in [accented](widgetrenderingmode/accented.md) mode.
- [AccessoryWidgetBackground](accessorywidgetbackground.md) — An adaptive background view that provides a standard appearance based on the the widget’s environment.
- [WidgetLocation](widgetlocation.md) — Values that indicate different widget locations.
