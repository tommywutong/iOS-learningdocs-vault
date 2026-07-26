---
title: 'overlay(_:alignment:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/overlay(_:alignment:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/overlay(_:alignment:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/overlay%28_%3Aalignment%3A%29.json'
content_hash: 'sha256:f4e47dc57470d623'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# overlay(_:alignment:)

<sub>Instance Method</sub>

Layers a secondary view in front of this view.

> [!warning] Deprecated
> Use [overlay(alignment:content:)](<overlay(alignment_content_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func overlay<Overlay>(_ overlay: Overlay, alignment: Alignment = .center) -> some View where Overlay : View

```

## Parameters

- `overlay` — The view to layer in front of this view.

- `alignment` — The alignment for `overlay` in relation to this view.

## Return Value

A view that layers `overlay` in front of the view.

## Discussion

When you apply an overlay to a view, the original view continues to provide the layout characteristics for the resulting view. In the following example, the heart image is shown overlaid in front of, and aligned to the bottom of the folder image.

```swift
Image(systemName: "folder")
    .font(.system(size: 55, weight: .thin))
    .overlay(Text("❤️"), alignment: .bottom)
```

![View showing placement of a heart overlaid onto a folder icon.](../../../../attachments/4f0a125e7d66518fa559f8899e888853/View-overlay-1@2x.png)

## See Also

### Appearance modifiers

- [colorScheme(_:)](<colorscheme(__).md>) — Sets this view’s color scheme. _(deprecated)_
- [listRowPlatterColor(_:)](<listrowplattercolor(__).md>) — Sets the color that the system applies to the row background when this view is placed in a list. _(deprecated)_
- [background(_:alignment:)](<background(__alignment_).md>) — Layers the given view behind this view. _(deprecated)_
- [foregroundColor(_:)](<foregroundcolor(__).md>) — Sets the color of the foreground elements displayed by this view. _(deprecated)_
- [complicationForeground()](<complicationforeground().md>) — Promotes this view to the foreground in a complication. _(deprecated)_
