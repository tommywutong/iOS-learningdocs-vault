---
title: allowsTightening
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/allowstightening
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/allowstightening'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/allowstightening.json'
content_hash: 'sha256:9e3ec1cc93a86d0f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# allowsTightening

<sub>Instance Property</sub>

A Boolean value that indicates whether inter-character spacing should tighten to fit the text into the available space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allowsTightening: Bool { get set }
```

## Discussion

The default value is `false`.

## See Also

### Managing text layout

- [truncationMode(_:)](<../view/truncationmode(__).md>) — Sets the truncation mode for lines of text that are too long to fit in the available space.
- [truncationMode](truncationmode.md) — A value that indicates how the layout truncates the last line of text to fit into the available space.
- [allowsTightening(_:)](<../view/allowstightening(__).md>) — Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [minimumScaleFactor(_:)](<../view/minimumscalefactor(__).md>) — Sets the minimum amount that text in this view scales down to fit in the available space.
- [minimumScaleFactor](minimumscalefactor.md) — The minimum permissible proportion to shrink the font size to fit the text into the available space.
- [baselineOffset(_:)](<../view/baselineoffset(__).md>) — Sets the vertical offset for the text relative to its baseline in this view.
- [kerning(_:)](<../view/kerning(__).md>) — Sets the spacing, or kerning, between characters for the text in this view.
- [tracking(_:)](<../view/tracking(__).md>) — Sets the tracking for the text in this view.
- [flipsForRightToLeftLayoutDirection(_:)](<../view/flipsforrighttoleftlayoutdirection(__).md>) — Sets whether this view mirrors its contents horizontally when the layout direction is right-to-left.
- [TextAlignment](../textalignment.md) — An alignment position for text along the horizontal axis.
