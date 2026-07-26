---
title: 'lineHeight(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/lineheight(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/lineheight(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/lineheight%28_%3A%29.json'
content_hash: 'sha256:53d43fd2995cba6b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# lineHeight(_:)

<sub>Instance Method</sub>

A modifier for the default line height in the view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func lineHeight(_ lineHeight: AttributedString.LineHeight?) -> some View

```

## Discussion

The default value is `nil`. In that case, SwiftUI automatically chooses an appropriate line height setting for each context.

> [!info] See Also
> [lineHeight](../environmentvalues/lineheight.md)

## See Also

### Text layout

- [allowsTightening(_:)](<allowstightening(__).md>) — Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [baselineOffset(_:)](<baselineoffset(__).md>) — Sets the vertical offset for the text relative to its baseline in this view.
- [flipsForRightToLeftLayoutDirection(_:)](<flipsforrighttoleftlayoutdirection(__).md>) — Sets whether this view mirrors its contents horizontally when the layout direction is right-to-left.
- [kerning(_:)](<kerning(__).md>) — Sets the spacing, or kerning, between characters for the text in this view.
- [minimumScaleFactor(_:)](<minimumscalefactor(__).md>) — Sets the minimum amount that text in this view scales down to fit in the available space.
- [tracking(_:)](<tracking(__).md>) — Sets the tracking for the text in this view.
- [truncationMode(_:)](<truncationmode(__).md>) — Sets the truncation mode for lines of text that are too long to fit in the available space.
- [typesettingLanguage(_:isEnabled:)](<typesettinglanguage(__isenabled_).md>) — Specifies the language for typesetting.
- [writingDirection(strategy:)](<writingdirection(strategy_).md>) — A modifier for the default text writing direction strategy in the view hierarchy.
