---
title: widgetContentMargins
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 26.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/widgetcontentmargins
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/widgetcontentmargins'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/widgetcontentmargins.json'
content_hash: 'sha256:33eb716cbadd7ec5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# widgetContentMargins

<sub>Instance Property</sub>

A property that identifies the content margins of a widget.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var widgetContentMargins: EdgeInsets { get }
```

## Return Value

Returns the content margins for the current widget presentation context.

## Discussion

The content margins of a widget depend on the context in which it appears. The system applies default content margins. However, if you disable automatic application of default content margins with [contentMarginsDisabled()](<../widgetconfiguration/contentmarginsdisabled().md>), the system uses the `widgetContentMargins` property in combination with [padding(_:)](<../view/padding(__).md>) to selectively apply default content margins.

## See Also

### Widgets

- [showsWidgetContainerBackground](showswidgetcontainerbackground.md) — An environment variable that indicates whether the background of a widget appears.
- [showsWidgetLabel](showswidgetlabel.md) — A Boolean value that indicates whether an accessory family widget can display an accessory label.
- [widgetFamily](widgetfamily.md) — The template of the widget — small, medium, or large.
- [widgetRenderingMode](widgetrenderingmode.md) — The widget’s rendering mode, based on where the system is displaying it.
