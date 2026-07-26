---
title: 'flipsForRightToLeftLayoutDirection(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/flipsforrighttoleftlayoutdirection(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/flipsforrighttoleftlayoutdirection(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/flipsforrighttoleftlayoutdirection%28_%3A%29.json'
content_hash: 'sha256:7edcac33cfdc34cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# flipsForRightToLeftLayoutDirection(_:)

<sub>Instance Method</sub>

Sets whether this view mirrors its contents horizontally when the layout direction is right-to-left.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func flipsForRightToLeftLayoutDirection(_ enabled: Bool) -> some View

```

## Parameters

- `enabled` — A Boolean value that indicates whether this view should have its content flipped horizontally when the layout direction is right-to-left. By default, views will adjust their layouts automatically in a right-to-left context and do not need to be mirrored.

## Return Value

A view that conditionally mirrors its contents horizontally when the layout direction is right-to-left.

## Discussion

Use `flipsForRightToLeftLayoutDirection(_:)` when you need the system to horizontally mirror the contents of the view when presented in a right-to-left layout.

To override the layout direction for a specific view, use the [environment(_:_:)](<environment(____).md>) view modifier to explicitly override the [layoutDirection](../environmentvalues/layoutdirection.md) environment value for the view.

## See Also

### Managing text layout

- [truncationMode(_:)](<truncationmode(__).md>) — Sets the truncation mode for lines of text that are too long to fit in the available space.
- [truncationMode](../environmentvalues/truncationmode.md) — A value that indicates how the layout truncates the last line of text to fit into the available space.
- [allowsTightening(_:)](<allowstightening(__).md>) — Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [allowsTightening](../environmentvalues/allowstightening.md) — A Boolean value that indicates whether inter-character spacing should tighten to fit the text into the available space.
- [minimumScaleFactor(_:)](<minimumscalefactor(__).md>) — Sets the minimum amount that text in this view scales down to fit in the available space.
- [minimumScaleFactor](../environmentvalues/minimumscalefactor.md) — The minimum permissible proportion to shrink the font size to fit the text into the available space.
- [baselineOffset(_:)](<baselineoffset(__).md>) — Sets the vertical offset for the text relative to its baseline in this view.
- [kerning(_:)](<kerning(__).md>) — Sets the spacing, or kerning, between characters for the text in this view.
- [tracking(_:)](<tracking(__).md>) — Sets the tracking for the text in this view.
- [TextAlignment](../textalignment.md) — An alignment position for text along the horizontal axis.
