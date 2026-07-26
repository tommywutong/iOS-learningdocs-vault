---
title: 'writingDirection(strategy:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/writingdirection(strategy:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/writingdirection(strategy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/writingdirection%28strategy%3A%29.json'
content_hash: 'sha256:adbc945e2db20a7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# writingDirection(strategy:)

<sub>Instance Method</sub>

A modifier for the default text writing direction strategy in the view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func writingDirection(strategy: Text.WritingDirectionStrategy) -> some View

```

## Discussion

To control the writing direction explicitly, choose the [layoutBased](../text/writingdirectionstrategy/layoutbased.md) mode and set the [layoutDirection](../environmentvalues/layoutdirection.md) to the appropriate value.

## See Also

### Text layout

- [allowsTightening(_:)](<allowstightening(__).md>) — Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [baselineOffset(_:)](<baselineoffset(__).md>) — Sets the vertical offset for the text relative to its baseline in this view.
- [flipsForRightToLeftLayoutDirection(_:)](<flipsforrighttoleftlayoutdirection(__).md>) — Sets whether this view mirrors its contents horizontally when the layout direction is right-to-left.
- [kerning(_:)](<kerning(__).md>) — Sets the spacing, or kerning, between characters for the text in this view.
- [lineHeight(_:)](<lineheight(__).md>) — A modifier for the default line height in the view hierarchy.
- [minimumScaleFactor(_:)](<minimumscalefactor(__).md>) — Sets the minimum amount that text in this view scales down to fit in the available space.
- [tracking(_:)](<tracking(__).md>) — Sets the tracking for the text in this view.
- [truncationMode(_:)](<truncationmode(__).md>) — Sets the truncation mode for lines of text that are too long to fit in the available space.
- [typesettingLanguage(_:isEnabled:)](<typesettinglanguage(__isenabled_).md>) — Specifies the language for typesetting.
