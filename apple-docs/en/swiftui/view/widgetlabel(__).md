---
title: 'widgetLabel(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/widgetlabel(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/widgetlabel(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/widgetlabel%28_%3A%29.json'
content_hash: 'sha256:9b86743ce7fde811'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# widgetLabel(_:)

<sub>Instance Method</sub>

Returns a localized text label that displays additional content outside the accessory family widget’s main SwiftUI view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func widgetLabel(_ label: LocalizedStringResource) -> some View

```

## Parameters

- `label` — A label generated from a localized string.

## Discussion

To add a text label to an accessory family widget, call this method on the widget’s main SwiftUI view, and pass in a supported `LocalizedStringResource`. The system determines whether it can use the text label. If it can’t, it ignores the label. The system also sets the label’s size, placement, and style based on the clock face. For example, setting the font and rendering the text along a curve.

The following widget families support text accessory labels:

- The [WidgetFamily.accessoryCorner](../../widgetkit/widgetfamily/accessorycorner.md) widget-based complication can display a curved text label on the inside edge of the corner. Adding a label to an accessory corner complication causes the main SwiftUI view to shrink to make space for the label.
- The [WidgetFamily.accessoryCircular](../../widgetkit/widgetfamily/accessorycircular.md) widget can display a text label in watchOS; however, WidgetKit only renders the label along the bezel on the Infograph watch face (the top circular complication).

## See Also

### Labeling a widget

- [widgetLabel(label:)](<widgetlabel(label_).md>) — Creates a label for displaying additional content outside an accessory family widget’s main SwiftUI view.
