---
title: showsWidgetLabel
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/showswidgetlabel
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/showswidgetlabel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/showswidgetlabel.json'
content_hash: 'sha256:86797f5f2fdbf50e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# showsWidgetLabel

<sub>Instance Property</sub>

A Boolean value that indicates whether an accessory family widget can display an accessory label.

<sub>iOS, iPadOS, Mac Catalyst, visionOS, watchOS</sub>

```swift
var showsWidgetLabel: Bool { get set }
```

## Discussion

Use this value to determine if you can provide additional content, or possibly move some of the widget’s content out of the main view and into the widget label.

```swift

@Environment(\.widgetFamily) var widgetFamily
@Environment(\.showsWidgetLabel) var showsWidgetLabel

var body: some View {
   switch widgetFamily {
   case .accessoryCircular:
       if showsWidgetLabel {
           Image("cat_full")
               .widgetLabel(label: Text("Cats"))
       }
       else {
           VStack {
               Image("cat_small")
               Text("Cats")
           }
       }
   }
}

```

This environment value is most useful when defining the appearance for the [WidgetFamily.accessoryCircular](../../widgetkit/widgetfamily/accessorycircular.md) widget family, because it’s value can change depending on where the widget appears. For example, if the widget is the top circular complication on the Infograph watch face, the value is `true`. Otherwise it is `false`. The environment variable is always `false` in iOS.

Other families always have the same value, regardless of where the widget appears. For the [WidgetFamily.accessoryCorner](../../widgetkit/widgetfamily/accessorycorner.md) widget family, the value is always `true`. For other families, it is `false`.

## See Also

### Widgets

- [showsWidgetContainerBackground](showswidgetcontainerbackground.md) — An environment variable that indicates whether the background of a widget appears.
- [widgetFamily](widgetfamily.md) — The template of the widget — small, medium, or large.
- [widgetRenderingMode](widgetrenderingmode.md) — The widget’s rendering mode, based on where the system is displaying it.
- [widgetContentMargins](widgetcontentmargins.md) — A property that identifies the content margins of a widget.
