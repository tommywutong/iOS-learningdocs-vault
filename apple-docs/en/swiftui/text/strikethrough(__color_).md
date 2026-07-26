---
title: 'strikethrough(_:color:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/text/strikethrough(_:color:)'
source_url: 'https://developer.apple.com/documentation/swiftui/text/strikethrough(_:color:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/strikethrough%28_%3Acolor%3A%29.json'
content_hash: 'sha256:3494e71118efb9eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Text](../text.md)

# strikethrough(_:color:)

<sub>Instance Method</sub>

Applies a strikethrough to the text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func strikethrough(_ isActive: Bool = true, color: Color? = nil) -> Text
```

## Parameters

- `isActive` — A Boolean value that indicates whether the text has a strikethrough applied.

- `color` — The color of the strikethrough. If `color` is `nil`, the strikethrough uses the default foreground color.

## Return Value

Text with a line through its center.

## See Also

### Styling the view’s text

- [foregroundStyle(_:)](<foregroundstyle(__).md>) — Sets the style of the text displayed by this view.
- [bold()](<bold().md>) — Applies a bold or emphasized treatment to the fonts of the text.
- [bold(_:)](<bold(__).md>) — Applies a bold font weight to the text.
- [italic()](<italic().md>) — Applies italics to the text.
- [italic(_:)](<italic(__).md>) — Applies italics to the text.
- [strikethrough(_:pattern:color:)](<strikethrough(__pattern_color_).md>) — Applies a strikethrough to the text.
- [underline(_:color:)](<underline(__color_).md>) — Applies an underline to the text.
- [underline(_:pattern:color:)](<underline(__pattern_color_).md>) — Applies an underline to the text.
- [monospaced(_:)](<monospaced(__).md>) — Modifies the font of the text to use the fixed-width variant of the current font, if possible.
- [monospacedDigit()](<monospaceddigit().md>) — Modifies the text view’s font to use fixed-width digits, while leaving other characters proportionally spaced.
- [kerning(_:)](<kerning(__).md>) — Sets the spacing, or kerning, between characters.
- [tracking(_:)](<tracking(__).md>) — Sets the tracking for the text.
- [baselineOffset(_:)](<baselineoffset(__).md>) — Sets the vertical offset for the text relative to its baseline.
- [Case](case.md) — A scheme for transforming the capitalization of characters within text.
- [DateStyle](datestyle.md) — A predefined style used to display a `Date`.
