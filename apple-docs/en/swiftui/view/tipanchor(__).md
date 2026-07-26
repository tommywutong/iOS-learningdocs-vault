---
title: 'tipAnchor(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/tipanchor(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/tipanchor(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/tipanchor%28_%3A%29.json'
content_hash: 'sha256:db9a7475b3e1649c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# tipAnchor(_:)

<sub>Instance Method</sub>

Sets a value for the specified tip anchor to be used to anchor a tip view to the `.bounds` of the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func tipAnchor<AnchorID>(_ id: AnchorID) -> some View where AnchorID : Hashable, AnchorID : Sendable

```

## Parameters

- `id` — The anchored view’s identifier.

## Return Value

A new version of the view that writes to the key.

## Discussion

Use this modifier to specify an anchor view for a `TipView`’s arrow to point towards.

```swift
struct TrailRow: View {
    let trail: Trail

    var body: some View {
        HStack {
            Text(trail.name)

            Button(action: trail.favorite) {
                Image(systemName: "star")
            }
            .tipAnchor("FavoriteTrailTipAnchor")
        }

        TipView(FavoriteTrailTip(), anchorID: "FavoriteTrailTipAnchor")
    }
}
```

## See Also

### Providing tips

- [popoverTip(_:arrowEdge:action:)](<popovertip(__arrowedge_action_).md>) — Presents a popover tip on the modified view.
- [popoverTip(_:isPresented:attachmentAnchor:arrowEdge:action:)](<popovertip(__ispresented_attachmentanchor_arrowedge_action_).md>) — Presents a popover tip on the modified view.
- [popoverTip(_:isPresented:attachmentAnchor:arrowEdges:action:)](<popovertip(__ispresented_attachmentanchor_arrowedges_action_).md>) — Presents a popover tip on the modified view.
- [tipBackground(_:)](<tipbackground(__).md>) — Sets the tip’s view background to a style.
- [tipBackgroundInteraction(_:)](<tipbackgroundinteraction(__).md>) — Controls whether people can interact with the view behind a presented tip.
- [tipCornerRadius(_:antialiased:)](<tipcornerradius(__antialiased_).md>) — Sets the corner radius for an inline tip view.
- [tipImageSize(_:)](<tipimagesize(__).md>) — Sets the size for a tip’s image.
- [tipViewStyle(_:)](<tipviewstyle(__).md>) — Sets the given style for TipView within the view hierarchy.
- [tipImageStyle(_:)](<tipimagestyle(__).md>) — Sets the style for a tip’s image.
- [tipImageStyle(_:_:)](<tipimagestyle(____).md>) — Sets the style for a tip’s image.
- [tipImageStyle(_:_:_:)](<tipimagestyle(______).md>) — Sets the style for a tip’s image.
