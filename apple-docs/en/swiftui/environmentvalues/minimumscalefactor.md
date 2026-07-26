---
title: minimumScaleFactor
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/minimumscalefactor
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/minimumscalefactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/minimumscalefactor.json'
content_hash: 'sha256:eb853b7a5de75c08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# minimumScaleFactor

<sub>Instance Property</sub>

The minimum permissible proportion to shrink the font size to fit the text into the available space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var minimumScaleFactor: CGFloat { get set }
```

## Discussion

In the example below, a label with a `minimumScaleFactor` of `0.5` draws its text in a font size as small as half of the actual font if needed to fit into the space next to the text input field:

```swift
HStack {
    Text("This is a very long label:")
        .lineLimit(1)
        .minimumScaleFactor(0.5)
    TextField("My Long Text Field", text: $myTextField)
        .frame(width: 250, height: 50, alignment: .center)
}
```

![A screenshot showing the effects of setting the minimumScaleFactor on](../../../../attachments/68f36609e7807a7ff513a4c83fa884ef/SwiftUI-View-minimumScaleFactor@2x.png)

You can set the minimum scale factor to any value greater than `0` and less than or equal to `1`. The default value is `1`.

SwiftUI uses this value to shrink text that doesn’t fit in a view when it’s okay to shrink the text. For example, a label with a `minimumScaleFactor` of `0.5` draws its text in a font size as small as half the actual font if needed.

## See Also

### Managing text layout

- [truncationMode(_:)](<../view/truncationmode(__).md>) — Sets the truncation mode for lines of text that are too long to fit in the available space.
- [truncationMode](truncationmode.md) — A value that indicates how the layout truncates the last line of text to fit into the available space.
- [allowsTightening(_:)](<../view/allowstightening(__).md>) — Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [allowsTightening](allowstightening.md) — A Boolean value that indicates whether inter-character spacing should tighten to fit the text into the available space.
- [minimumScaleFactor(_:)](<../view/minimumscalefactor(__).md>) — Sets the minimum amount that text in this view scales down to fit in the available space.
- [baselineOffset(_:)](<../view/baselineoffset(__).md>) — Sets the vertical offset for the text relative to its baseline in this view.
- [kerning(_:)](<../view/kerning(__).md>) — Sets the spacing, or kerning, between characters for the text in this view.
- [tracking(_:)](<../view/tracking(__).md>) — Sets the tracking for the text in this view.
- [flipsForRightToLeftLayoutDirection(_:)](<../view/flipsforrighttoleftlayoutdirection(__).md>) — Sets whether this view mirrors its contents horizontally when the layout direction is right-to-left.
- [TextAlignment](../textalignment.md) — An alignment position for text along the horizontal axis.
