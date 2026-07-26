---
title: widgetRenderingMode
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/widgetrenderingmode
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/widgetrenderingmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/widgetrenderingmode.json'
content_hash: 'sha256:54b435e777b74bcd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# widgetRenderingMode

<sub>Instance Property</sub>

The widget’s rendering mode, based on where the system is displaying it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var widgetRenderingMode: WidgetRenderingMode { get set }
```

## Discussion

You can read the rendering mode from the environment values using this key.

```swift
@Environment(\.widgetRenderingMode) var widgetRenderingMode
```

Then modify the widget’s appearance based on the mode.

```swift
var body: some View {
    ZStack {
       switch renderingMode {
        case .fullColor:
           Text("Full color")
        case .accented:
           ZStack {
               Circle(...)
               VStack {
                   Text("Accented")
                       .widgetAccentable()
                   Text("Normal")
               }
           }
        case .vibrant:
           Text("Full color")
        default:
           ...
        }
    }
}
```

## See Also

### Widgets

- [showsWidgetContainerBackground](showswidgetcontainerbackground.md) — An environment variable that indicates whether the background of a widget appears.
- [showsWidgetLabel](showswidgetlabel.md) — A Boolean value that indicates whether an accessory family widget can display an accessory label.
- [widgetFamily](widgetfamily.md) — The template of the widget — small, medium, or large.
- [widgetContentMargins](widgetcontentmargins.md) — A property that identifies the content margins of a widget.
