---
title: 'kerning(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/kerning(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/kerning(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/kerning%28_%3A%29.json'
content_hash: 'sha256:fa5eae38ed7dd945'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# kerning(_:)

<sub>Instance Method</sub>

Sets the spacing, or kerning, between characters for the text in this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func kerning(_ kerning: CGFloat) -> some View

```

## Parameters

- `kerning` — The spacing to use between individual characters in text. Value of `0` sets the kerning to the system default value.

## Return Value

A view where text has the specified amount of kerning.

## See Also

### Managing text layout

- [truncationMode(_:)](<truncationmode(__).md>) — Sets the truncation mode for lines of text that are too long to fit in the available space.
- [truncationMode](../environmentvalues/truncationmode.md) — A value that indicates how the layout truncates the last line of text to fit into the available space.
- [allowsTightening(_:)](<allowstightening(__).md>) — Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [allowsTightening](../environmentvalues/allowstightening.md) — A Boolean value that indicates whether inter-character spacing should tighten to fit the text into the available space.
- [minimumScaleFactor(_:)](<minimumscalefactor(__).md>) — Sets the minimum amount that text in this view scales down to fit in the available space.
- [minimumScaleFactor](../environmentvalues/minimumscalefactor.md) — The minimum permissible proportion to shrink the font size to fit the text into the available space.
- [baselineOffset(_:)](<baselineoffset(__).md>) — Sets the vertical offset for the text relative to its baseline in this view.
- [tracking(_:)](<tracking(__).md>) — Sets the tracking for the text in this view.
- [flipsForRightToLeftLayoutDirection(_:)](<flipsforrighttoleftlayoutdirection(__).md>) — Sets whether this view mirrors its contents horizontally when the layout direction is right-to-left.
- [TextAlignment](../textalignment.md) — An alignment position for text along the horizontal axis.
