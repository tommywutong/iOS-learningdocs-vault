---
title: truncationMode
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/truncationmode
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/truncationmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/truncationmode.json'
content_hash: 'sha256:1f273e9c0bd1c0d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# truncationMode

<sub>Instance Property</sub>

A value that indicates how the layout truncates the last line of text to fit into the available space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var truncationMode: Text.TruncationMode { get set }
```

## Discussion

The default value is [Text.TruncationMode.tail](../text/truncationmode/tail.md). Some controls, however, might have a different default if appropriate.

## See Also

### Managing text layout

- [truncationMode(_:)](<../view/truncationmode(__).md>) — Sets the truncation mode for lines of text that are too long to fit in the available space.
- [allowsTightening(_:)](<../view/allowstightening(__).md>) — Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [allowsTightening](allowstightening.md) — A Boolean value that indicates whether inter-character spacing should tighten to fit the text into the available space.
- [minimumScaleFactor(_:)](<../view/minimumscalefactor(__).md>) — Sets the minimum amount that text in this view scales down to fit in the available space.
- [minimumScaleFactor](minimumscalefactor.md) — The minimum permissible proportion to shrink the font size to fit the text into the available space.
- [baselineOffset(_:)](<../view/baselineoffset(__).md>) — Sets the vertical offset for the text relative to its baseline in this view.
- [kerning(_:)](<../view/kerning(__).md>) — Sets the spacing, or kerning, between characters for the text in this view.
- [tracking(_:)](<../view/tracking(__).md>) — Sets the tracking for the text in this view.
- [flipsForRightToLeftLayoutDirection(_:)](<../view/flipsforrighttoleftlayoutdirection(__).md>) — Sets whether this view mirrors its contents horizontally when the layout direction is right-to-left.
- [TextAlignment](../textalignment.md) — An alignment position for text along the horizontal axis.
