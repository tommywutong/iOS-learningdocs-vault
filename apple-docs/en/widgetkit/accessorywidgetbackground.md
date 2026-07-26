---
title: AccessoryWidgetBackground
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/accessorywidgetbackground
source_url: 'https://developer.apple.com/documentation/widgetkit/accessorywidgetbackground'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/accessorywidgetbackground.json'
content_hash: 'sha256:c5b6bd9985e3740b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# AccessoryWidgetBackground

<sub>Structure</sub>

An adaptive background view that provides a standard appearance based on the the widget’s environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct AccessoryWidgetBackground
```

## Overview

Use this view to provide a standardized background for your accessory widgets. Place the view in a [ZStack](../swiftui/zstack.md) behind your widget’s content.

```Swift
ZStack {
    AccessoryWidgetBackground()
    VStack {
        Text("MON")
            .font(.caption)
            .widgetAccentable()
        Text("6")
            .font(.title)
    }
}
```

The system only displays this view inside a [WidgetFamily.accessoryCircular](widgetfamily/accessorycircular.md), [WidgetFamily.accessoryCorner](widgetfamily/accessorycorner.md), or [WidgetFamily.accessoryRectangular](widgetfamily/accessoryrectangular.md) widget. In any other context, the system displays an empty view instead.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating accessory widget backgrounds

- [init()](<accessorywidgetbackground/init().md>) — Creates an instance of an accessory widget background.

## See Also

### Layout and presentation

- [Supporting additional widget sizes](supporting-additional-widget-sizes.md) — Offer widgets in additional contexts by adding support for various widget sizes.
- [Displaying the right widget background](displaying-the-right-widget-background.md) — Group your widget’s background views and mark them as removable to ensure your widget appears correctly for each context and platform.
- [Optimizing your widget for accented rendering mode and Liquid Glass](optimizing-your-widget-for-accented-rendering-mode-and-liquid-glass.md) — Make your widget feel at home on Apple platforms and Liquid Glass by using accented rendering mode.
- [Adding StandBy and CarPlay support to your widget](adding-standby-and-carplay-support-to-your-widget.md) — Ensure that your small system family widget works well in StandBy and CarPlay.
- [WidgetRenderingMode](widgetrenderingmode.md) — Constants that indicate the rendering mode for a widget.
- [WidgetAccentedRenderingMode](widgetaccentedrenderingmode.md) — Constants that indicate the rendering mode for an `Image` in when displayed in a widget in [accented](widgetrenderingmode/accented.md) mode.
- [WidgetLocation](widgetlocation.md) — Values that indicate different widget locations.
