---
title: WidgetLocation
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/widgetlocation
source_url: 'https://developer.apple.com/documentation/widgetkit/widgetlocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetlocation.json'
content_hash: 'sha256:6196e756b0ff5f73'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# WidgetLocation

<sub>Structure</sub>

Values that indicate different widget locations.

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
struct WidgetLocation
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Specifying a location style

- [carPlay](widgetlocation/carplay.md) — The CarPlay location for a widget.
- [iPhoneWidgetsOnMac](widgetlocation/iphonewidgetsonmac.md) — The widget originates from another device and appears on the Mac.
- [homeScreen](widgetlocation/homescreen.md) — The widget appears on the Home Screen or in Today View.
- [lockScreen](widgetlocation/lockscreen.md) — The widget appears on the Lock Screen.
- [smartStack](widgetlocation/smartstack.md)
- [standBy](widgetlocation/standby.md) — The widget appears in StandBy.
- [watchFace](widgetlocation/watchface.md)

## See Also

### Layout and presentation

- [Supporting additional widget sizes](supporting-additional-widget-sizes.md) — Offer widgets in additional contexts by adding support for various widget sizes.
- [Displaying the right widget background](displaying-the-right-widget-background.md) — Group your widget’s background views and mark them as removable to ensure your widget appears correctly for each context and platform.
- [Optimizing your widget for accented rendering mode and Liquid Glass](optimizing-your-widget-for-accented-rendering-mode-and-liquid-glass.md) — Make your widget feel at home on Apple platforms and Liquid Glass by using accented rendering mode.
- [Adding StandBy and CarPlay support to your widget](adding-standby-and-carplay-support-to-your-widget.md) — Ensure that your small system family widget works well in StandBy and CarPlay.
- [WidgetRenderingMode](widgetrenderingmode.md) — Constants that indicate the rendering mode for a widget.
- [WidgetAccentedRenderingMode](widgetaccentedrenderingmode.md) — Constants that indicate the rendering mode for an `Image` in when displayed in a widget in [accented](widgetrenderingmode/accented.md) mode.
- [AccessoryWidgetBackground](accessorywidgetbackground.md) — An adaptive background view that provides a standard appearance based on the the widget’s environment.
