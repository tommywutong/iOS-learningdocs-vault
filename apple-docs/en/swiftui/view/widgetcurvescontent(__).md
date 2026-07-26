---
title: 'widgetCurvesContent(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 26.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/widgetcurvescontent(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/widgetcurvescontent(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/widgetcurvescontent%28_%3A%29.json'
content_hash: 'sha256:d4e79ec58c1ba4ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# widgetCurvesContent(_:)

<sub>Instance Method</sub>

Displays the widget’s content along a curve if the context allows it.

<sub>iOS, iPadOS, Mac Catalyst, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func widgetCurvesContent(_ curvesContent: Bool = true) -> some View

```

## Parameters

- `curvesContent` — A Boolean value that indicates whether the system curves the widget label’s content, if the context allows.

## Discussion

The system positions the widget’s content along a curve that follows the corner of the watch face when displaying a [WidgetFamily.accessoryCorner](../../widgetkit/widgetfamily/accessorycorner.md) complication. The widget must use  a  [widgetLabel(_:)](<widgetlabel(__)-7wguh.md>) modifier, and the curving effect modifies only text, SF Symbols, and images.

When displaying an `.accessoryCorner` complication, the system places the widget label on the inside of the curve, and the widget’s content on the outside, as shown below.

```swift
var body: some View {
    Text("Hi")
        .widgetCurvesContent()
        .widgetLabel("World!")
}
```

The system can also curve text, SF symbols, and image content from a [ViewThatFits](../viewthatfits.md) view.

```swift
var body: some View {
    ViewThatFits {
        Text("Hello")
        Text("Hi")
    }
    .widgetCurvesContent()
    .widgetLabel("World!")
}
```

## See Also

### Widget configuration

- [widgetAccentable(_:)](<widgetaccentable(__).md>) — Adds the view and all of its subviews to the accented group.
- [widgetLabel(_:)](<widgetlabel(__).md>) — Returns a localized text label that displays additional content outside the accessory family widget’s main SwiftUI view.
- [widgetLabel(label:)](<widgetlabel(label_).md>) — Creates a label for displaying additional content outside an accessory family widget’s main SwiftUI view.
- [dynamicIsland(verticalPlacement:)](<dynamicisland(verticalplacement_).md>) — Specifies the vertical placement for a view of an expanded Live Activity that appears in the Dynamic Island.
- [accessoryWidgetGroupStyle(_:)](<accessorywidgetgroupstyle(__).md>) — The view modifier that can be applied to `AccessoryWidgetGroup` to specify the shape the three content views will be masked with. The value of `style` is set to `.automatic`, which is `.circular` by default.
- [controlWidgetActionHint(_:)](<controlwidgetactionhint(__).md>) — The action hint of the control described by the modified label.
- [controlWidgetStatus(_:)](<controlwidgetstatus(__).md>) — The status of the control described by the modified label.
