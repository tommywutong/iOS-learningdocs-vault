---
title: 'sliderThumbVisibility(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/sliderthumbvisibility(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/sliderthumbvisibility(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/sliderthumbvisibility%28_%3A%29.json'
content_hash: 'sha256:d8630d5c88c0643f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# sliderThumbVisibility(_:)

<sub>Instance Method</sub>

Sets the thumb visibility for `Slider`s within this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated func sliderThumbVisibility(_ visibility: Visibility) -> some View

```

## Parameters

- `visibility` — The slider thumb visibility to apply.

## Discussion

Use this modifier to override the default slider thumb visibility. For example, the code below creates a `Slider` without an indicator:

```swift
@State private var speed = 50.0
@State private var isEditing = false

var body: some View {
    VStack {
        Slider(
            value: $speed,
            in: 0...100,
            onEditingChanged: { editing in
                isEditing = editing
            }
        )
        .sliderThumbVisibility(.hidden)

        Text("\(speed)")
            .foregroundColor(isEditing ? .red : .blue)
    }
}
```

Note: On watchOS, the slider thumb is always visible.

## See Also

### Visibility

- [hidden()](<hidden().md>) — Hides this view unconditionally.
- [labelsHidden()](<labelshidden().md>) — Hides the labels of any controls contained within this view.
- [labelsVisibility(_:)](<labelsvisibility(__).md>) — Controls the visibility of labels of any controls contained within this view.
- [menuIndicator(_:)](<menuindicator(__).md>) — Sets the menu indicator visibility for controls within this view.
- [listRowSeparator(_:edges:)](<listrowseparator(__edges_).md>) — Sets the display mode for the separator associated with this specific row.
- [listSectionSeparator(_:edges:)](<listsectionseparator(__edges_).md>) — Sets whether to hide the separator associated with a list section.
- [listSectionIndexVisibility(_:)](<listsectionindexvisibility(__).md>) — Changes the visibility of the list section index.
- [persistentSystemOverlays(_:)](<persistentsystemoverlays(__).md>) — Sets the preferred visibility of the non-transient system views overlaying the app.
- [scrollIndicators(_:axes:)](<scrollindicators(__axes_).md>) — Sets the visibility of scroll indicators within this view.
- [scrollClipDisabled(_:)](<scrollclipdisabled(__).md>) — Sets whether a scroll view clips its content to its bounds.
- [tableColumnHeaders(_:)](<tablecolumnheaders(__).md>) — Controls the visibility of a `Table`’s column header views.
- [upperLimbVisibility(_:)](<upperlimbvisibility(__).md>) — Sets the preferred visibility of the user’s upper limbs, while an [ImmersiveSpace](../immersivespace.md) scene is presented.
- [volumeBaseplateVisibility(_:)](<volumebaseplatevisibility(__).md>) — Sets the visibility of the baseplate of a volume, which appears when a user looks towards the ‘floor’ of a volume and during resize. Both `automatic` and `visible` will show the baseplate. `hidden` will never show it.
