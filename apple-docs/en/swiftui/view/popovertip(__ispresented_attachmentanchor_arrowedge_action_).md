---
title: 'popoverTip(_:isPresented:attachmentAnchor:arrowEdge:action:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/popovertip(_:ispresented:attachmentanchor:arrowedge:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/popovertip(_:ispresented:attachmentanchor:arrowedge:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/popovertip%28_%3Aispresented%3Aattachmentanchor%3Aarrowedge%3Aaction%3A%29.json'
content_hash: 'sha256:4d28412b561e4c62'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# popoverTip(_:isPresented:attachmentAnchor:arrowEdge:action:)

<sub>Instance Method</sub>

Presents a popover tip on the modified view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@preconcurrency nonisolated func popoverTip(_ tip: (any Tip)?, isPresented: Binding<Bool>? = nil, attachmentAnchor: PopoverAttachmentAnchor = .rect(.bounds), arrowEdge: Edge? = nil, action: @escaping @MainActor @Sendable (Tips.Action) -> Void = { _ in }) -> some View

```

## Parameters

- `tip` — The tip to display.

- `isPresented` — A binding that will automatically update to true when a tip is displayed. This value can be changed to temporarily hide or show a currently displayable tip. If this value is `nil`, the popover will automatically be dismissed based on the tip’s status and display rules.

- `attachmentAnchor` — The positioning anchor that defines the attachment point of the popover. The default is bounds.

- `arrowEdge` — The edge of the attachmentAnchor that defines the location of the popover’s arrow. By default, the system will choose the best orientation of the popover’s arrow.

- `action` — The closure to perform when the user triggers a tip’s action.

### Discussion

Use this modifier to present a tip as a popover on an existing view when the tip becomes eligible for display.

```swift
struct TrailRow: View {
    let trail: Trail

    var body: some View {
        VStack {
            HStack {
                Text(trail.name)

                Button(action: trail.favorite) {
                    Image(systemName: "star")
                }
            }
        }
        .popoverTip(FavoriteTrailTip(), attachmentAnchor: .point(.center), arrowEdge: .top)
    }
}
```

## See Also

### Providing tips

- [popoverTip(_:arrowEdge:action:)](<popovertip(__arrowedge_action_).md>) — Presents a popover tip on the modified view.
- [popoverTip(_:isPresented:attachmentAnchor:arrowEdges:action:)](<popovertip(__ispresented_attachmentanchor_arrowedges_action_).md>) — Presents a popover tip on the modified view.
- [tipAnchor(_:)](<tipanchor(__).md>) — Sets a value for the specified tip anchor to be used to anchor a tip view to the `.bounds` of the view.
- [tipBackground(_:)](<tipbackground(__).md>) — Sets the tip’s view background to a style.
- [tipBackgroundInteraction(_:)](<tipbackgroundinteraction(__).md>) — Controls whether people can interact with the view behind a presented tip.
- [tipCornerRadius(_:antialiased:)](<tipcornerradius(__antialiased_).md>) — Sets the corner radius for an inline tip view.
- [tipImageSize(_:)](<tipimagesize(__).md>) — Sets the size for a tip’s image.
- [tipViewStyle(_:)](<tipviewstyle(__).md>) — Sets the given style for TipView within the view hierarchy.
- [tipImageStyle(_:)](<tipimagestyle(__).md>) — Sets the style for a tip’s image.
- [tipImageStyle(_:_:)](<tipimagestyle(____).md>) — Sets the style for a tip’s image.
- [tipImageStyle(_:_:_:)](<tipimagestyle(______).md>) — Sets the style for a tip’s image.
