---
title: 'tipImageStyle(_:_:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/tipimagestyle(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/tipimagestyle(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/tipimagestyle%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:b6959b429096d5af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# tipImageStyle(_:_:_:)

<sub>Instance Method</sub>

Sets the style for a tip’s image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func tipImageStyle<S1, S2, S3>(_ primary: S1, _ secondary: S2, _ tertiary: S3) -> some View where S1 : ShapeStyle, S2 : ShapeStyle, S3 : ShapeStyle

```

## See Also

### Providing tips

- [popoverTip(_:arrowEdge:action:)](<popovertip(__arrowedge_action_).md>) — Presents a popover tip on the modified view.
- [popoverTip(_:isPresented:attachmentAnchor:arrowEdge:action:)](<popovertip(__ispresented_attachmentanchor_arrowedge_action_).md>) — Presents a popover tip on the modified view.
- [popoverTip(_:isPresented:attachmentAnchor:arrowEdges:action:)](<popovertip(__ispresented_attachmentanchor_arrowedges_action_).md>) — Presents a popover tip on the modified view.
- [tipAnchor(_:)](<tipanchor(__).md>) — Sets a value for the specified tip anchor to be used to anchor a tip view to the `.bounds` of the view.
- [tipBackground(_:)](<tipbackground(__).md>) — Sets the tip’s view background to a style.
- [tipBackgroundInteraction(_:)](<tipbackgroundinteraction(__).md>) — Controls whether people can interact with the view behind a presented tip.
- [tipCornerRadius(_:antialiased:)](<tipcornerradius(__antialiased_).md>) — Sets the corner radius for an inline tip view.
- [tipImageSize(_:)](<tipimagesize(__).md>) — Sets the size for a tip’s image.
- [tipViewStyle(_:)](<tipviewstyle(__).md>) — Sets the given style for TipView within the view hierarchy.
- [tipImageStyle(_:)](<tipimagestyle(__).md>) — Sets the style for a tip’s image.
- [tipImageStyle(_:_:)](<tipimagestyle(____).md>) — Sets the style for a tip’s image.
