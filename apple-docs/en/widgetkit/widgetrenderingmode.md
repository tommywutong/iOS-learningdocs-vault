---
title: WidgetRenderingMode
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/widgetrenderingmode
source_url: 'https://developer.apple.com/documentation/widgetkit/widgetrenderingmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetrenderingmode.json'
content_hash: 'sha256:0d6294503a62c3e3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# WidgetRenderingMode

<sub>Structure</sub>

Constants that indicate the rendering mode for a widget.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
struct WidgetRenderingMode
```

## Overview

The system can modify the appearance of accessory family widgets. For example, it renders widgets on the Lock Screen on iPhone using the [vibrant](widgetrenderingmode/vibrant.md) mode, while it renders widget-based complications in watchOS using either the [fullColor](widgetrenderingmode/fullcolor.md) or [accented](widgetrenderingmode/accented.md) modes, depending on the watch face and the user’s settings.

You can read the rendering mode from the environment values using the `.widgetRenderingMode` key.

```swift
@Environment(\.widgetRenderingMode) var widgetRenderingMode
```

You can then customize your widget’s design based on the rendering mode.

## Relationships

- **Conforms To**: [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md)

## Topics

### Rendering modes

- [fullColor](widgetrenderingmode/fullcolor.md) — The system renders the widget in full color.
- [accented](widgetrenderingmode/accented.md) — The system divides the widget’s view hierarchy into an accent group and a default group, applying a different color to each group.
- [vibrant](widgetrenderingmode/vibrant.md) — The system desaturates the widget, making a monochrome version that it uses to create an adaptive, vibrant effect.

## See Also

### Layout and presentation

- [Supporting additional widget sizes](supporting-additional-widget-sizes.md) — Offer widgets in additional contexts by adding support for various widget sizes.
- [Displaying the right widget background](displaying-the-right-widget-background.md) — Group your widget’s background views and mark them as removable to ensure your widget appears correctly for each context and platform.
- [Optimizing your widget for accented rendering mode and Liquid Glass](optimizing-your-widget-for-accented-rendering-mode-and-liquid-glass.md) — Make your widget feel at home on Apple platforms and Liquid Glass by using accented rendering mode.
- [Adding StandBy and CarPlay support to your widget](adding-standby-and-carplay-support-to-your-widget.md) — Ensure that your small system family widget works well in StandBy and CarPlay.
- [WidgetAccentedRenderingMode](widgetaccentedrenderingmode.md) — Constants that indicate the rendering mode for an `Image` in when displayed in a widget in [accented](widgetrenderingmode/accented.md) mode.
- [AccessoryWidgetBackground](accessorywidgetbackground.md) — An adaptive background view that provides a standard appearance based on the the widget’s environment.
- [WidgetLocation](widgetlocation.md) — Values that indicate different widget locations.
