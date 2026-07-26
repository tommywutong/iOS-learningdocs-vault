---
title: labelsVisibility
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/labelsvisibility
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/labelsvisibility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/labelsvisibility.json'
content_hash: 'sha256:7906820e743bc3da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# labelsVisibility

<sub>Instance Property</sub>

The labels visibility set by [labelsVisibility(_:)](<../view/labelsvisibility(__).md>).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var labelsVisibility: Visibility { get set }
```

## Discussion

Read this environment value from within a view to obtain the preferred visibility for labels within the hierarchy. If you would like to dynamically hide the label of your custom view, make sure to include an accessibility label via the [accessibilityLabel(content:)](<../view/accessibilitylabel(content_).md>) modifier as illustrated below:

```swift
@Environment(\.labelsVisibility)
private var labelsVisibility

var body: some View {
    VStack {
        QuizCardView()
        if labelsVisibility != .hidden {
            label
        }
    }
    .accessibilityLabel {
        label
    }
}

private var label: some View {
    Text("Quiz Card")
}
```

## See Also

### Hiding system elements

- [labelsHidden()](<../view/labelshidden().md>) — Hides the labels of any controls contained within this view.
- [labelsVisibility(_:)](<../view/labelsvisibility(__).md>) — Controls the visibility of labels of any controls contained within this view.
- [menuIndicator(_:)](<../view/menuindicator(__).md>) — Sets the menu indicator visibility for controls within this view.
- [statusBarHidden(_:)](<../view/statusbarhidden(__).md>) — Sets the visibility of the status bar. _(deprecated)_
- [persistentSystemOverlays(_:)](<../view/persistentsystemoverlays(__).md>) — Sets the preferred visibility of the non-transient system views overlaying the app.
- [Visibility](../visibility.md) — The visibility of a UI element, chosen automatically based on the platform, current context, and other factors.
