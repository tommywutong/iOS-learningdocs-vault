---
title: showsWidgetContainerBackground
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 26.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/showswidgetcontainerbackground
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/showswidgetcontainerbackground'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/showswidgetcontainerbackground.json'
content_hash: 'sha256:75940601edb72942'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# showsWidgetContainerBackground

<sub>Instance Property</sub>

An environment variable that indicates whether the background of a widget appears.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var showsWidgetContainerBackground: Bool { get }
```

## Return Value

`true` if, by default, the background appears in this context; `false` otherwise.

## Discussion

In iOS 16 and earlier, this environment variable is always `true` for system widgets and `false` for accessory widgets. In macOS 13 and earlier, and in watchOS 9 and earlier, it always evaluates to `true`.

If you pass `false` to [containerBackgroundRemovable(_:)](<../widgetconfiguration/containerbackgroundremovable(__).md>) to always show the widget background, the system shows the widget background even if `showsWidgetContainerBackground` evaluates to `true`.

## See Also

### Widgets

- [showsWidgetLabel](showswidgetlabel.md) — A Boolean value that indicates whether an accessory family widget can display an accessory label.
- [widgetFamily](widgetfamily.md) — The template of the widget — small, medium, or large.
- [widgetRenderingMode](widgetrenderingmode.md) — The widget’s rendering mode, based on where the system is displaying it.
- [widgetContentMargins](widgetcontentmargins.md) — A property that identifies the content margins of a widget.
