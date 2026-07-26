---
title: 'tipBackgroundInteraction(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/tipbackgroundinteraction(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/tipbackgroundinteraction(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/tipbackgroundinteraction%28_%3A%29.json'
content_hash: 'sha256:9a10a6ff6ae0df65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# tipBackgroundInteraction(_:)

<sub>Instance Method</sub>

Controls whether people can interact with the view behind a presented tip.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated func tipBackgroundInteraction(_ interaction: PresentationBackgroundInteraction) -> some View

```

## Parameters

- `interaction` — A specification of how people can interact with the view behind a presented tip.

### Discussion

On many platforms, SwiftUI automatically disables the view behind a popover tip that you present, so that people can’t interact with the backing view until they dismiss the tip. Use this modifier if you want to enable interaction.

The following example enables people to interact with the view behind a `popoverTip`.

```swift
struct LandmarkDetail: View {
    let landmark: Landmark

    var body: some View {
        ScrollView {
            MapView(coordinate: landmark.locationCoordinate)
                .popoverTip(CampsiteTip())
                .tipBackgroundInteraction(.enabled)

            HStack {
                Text(landmark.name)
                Text(landmark.park)
            }
        }
    }
}
```

## See Also

### Providing tips

- [popoverTip(_:arrowEdge:action:)](<popovertip(__arrowedge_action_).md>) — Presents a popover tip on the modified view.
- [popoverTip(_:isPresented:attachmentAnchor:arrowEdge:action:)](<popovertip(__ispresented_attachmentanchor_arrowedge_action_).md>) — Presents a popover tip on the modified view.
- [popoverTip(_:isPresented:attachmentAnchor:arrowEdges:action:)](<popovertip(__ispresented_attachmentanchor_arrowedges_action_).md>) — Presents a popover tip on the modified view.
- [tipAnchor(_:)](<tipanchor(__).md>) — Sets a value for the specified tip anchor to be used to anchor a tip view to the `.bounds` of the view.
- [tipBackground(_:)](<tipbackground(__).md>) — Sets the tip’s view background to a style.
- [tipCornerRadius(_:antialiased:)](<tipcornerradius(__antialiased_).md>) — Sets the corner radius for an inline tip view.
- [tipImageSize(_:)](<tipimagesize(__).md>) — Sets the size for a tip’s image.
- [tipViewStyle(_:)](<tipviewstyle(__).md>) — Sets the given style for TipView within the view hierarchy.
- [tipImageStyle(_:)](<tipimagestyle(__).md>) — Sets the style for a tip’s image.
- [tipImageStyle(_:_:)](<tipimagestyle(____).md>) — Sets the style for a tip’s image.
- [tipImageStyle(_:_:_:)](<tipimagestyle(______).md>) — Sets the style for a tip’s image.
