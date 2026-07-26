---
title: bold()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/text/bold()
source_url: 'https://developer.apple.com/documentation/swiftui/text/bold()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/bold%28%29.json'
content_hash: 'sha256:9ded9ba5a6b2d799'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Text](../text.md)

# bold()

<sub>Instance Method</sub>

Applies a bold or emphasized treatment to the fonts of the text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func bold() -> Text
```

## Return Value

Bold or emphasized text.

## Discussion

For fonts created from text styles, it could mean applying emphasized styling, which does not necessarily mean the bold weight specifically, so this modifier is not to be confused with [fontWeight(_:)](<fontweight(__).md>).

For example:

```swift
Text("hello").font(.body).bold()
```

will most likely get you the emphasized version of body text style, which is often in [semibold](../font/weight/semibold.md) weight. While

```swift
Text("hello").font(.body).fontWeight(.bold)
```

will specifically get you the body text style font in the [bold](../font/weight/bold.md) weight.

## See Also

### Styling the view’s text

- [foregroundStyle(_:)](<foregroundstyle(__).md>) — Sets the style of the text displayed by this view.
- [bold(_:)](<bold(__).md>) — Applies a bold font weight to the text.
- [italic()](<italic().md>) — Applies italics to the text.
- [italic(_:)](<italic(__).md>) — Applies italics to the text.
- [strikethrough(_:color:)](<strikethrough(__color_).md>) — Applies a strikethrough to the text.
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
