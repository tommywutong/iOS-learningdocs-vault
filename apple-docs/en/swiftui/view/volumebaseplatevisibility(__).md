---
title: 'volumeBaseplateVisibility(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/volumebaseplatevisibility(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/volumebaseplatevisibility(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/volumebaseplatevisibility%28_%3A%29.json'
content_hash: 'sha256:0e2d23ed450e0964'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# volumeBaseplateVisibility(_:)

<sub>Instance Method</sub>

Sets the visibility of the baseplate of a volume, which appears when a user looks towards the ‘floor’ of a volume and during resize. Both `automatic` and `visible` will show the baseplate. `hidden` will never show it.

<sub>visionOS</sub>

```swift
nonisolated func volumeBaseplateVisibility(_ visibility: Visibility) -> some View

```

## Discussion

The baseplate is a semi-transparent view that appears on the ‘floor’ of a volume.

Usage:

```swift
WindowGroup() {
    Poker()
        .volumeBaseplateVisibility(.visible)
}
.windowStyle(.volumetric)
```

Defaults to `automatic` (visible).

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
- [sliderThumbVisibility(_:)](<sliderthumbvisibility(__).md>) — Sets the thumb visibility for `Slider`s within this view.
- [tableColumnHeaders(_:)](<tablecolumnheaders(__).md>) — Controls the visibility of a `Table`’s column header views.
- [upperLimbVisibility(_:)](<upperlimbvisibility(__).md>) — Sets the preferred visibility of the user’s upper limbs, while an [ImmersiveSpace](../immersivespace.md) scene is presented.
