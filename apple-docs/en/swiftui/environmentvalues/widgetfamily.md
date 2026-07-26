---
title: widgetFamily
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/widgetfamily
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/widgetfamily'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/widgetfamily.json'
content_hash: 'sha256:69513443cb888a1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# widgetFamily

<sub>Instance Property</sub>

The template of the widget — small, medium, or large.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var widgetFamily: WidgetFamily { get }
```

## Discussion

Use this value to retrieve the widget size that the user chose for a widget.

## See Also

### Widgets

- [showsWidgetContainerBackground](showswidgetcontainerbackground.md) — An environment variable that indicates whether the background of a widget appears.
- [showsWidgetLabel](showswidgetlabel.md) — A Boolean value that indicates whether an accessory family widget can display an accessory label.
- [widgetRenderingMode](widgetrenderingmode.md) — The widget’s rendering mode, based on where the system is displaying it.
- [widgetContentMargins](widgetcontentmargins.md) — A property that identifies the content margins of a widget.
