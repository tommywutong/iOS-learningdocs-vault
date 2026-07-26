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
doc_path: /documentation/swiftui/font/bold()
source_url: 'https://developer.apple.com/documentation/swiftui/font/bold()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/font/bold%28%29.json'
content_hash: 'sha256:0faad1512ee56123'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Font](../font.md)

# bold()

<sub>Instance Method</sub>

Adds bold or emphasized styling to the font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func bold() -> Font
```

## Discussion

For fonts created from text styles, it could mean applying emphasized styling, which does not necessarily mean the bold weight specifically, so this modifier is not to be confused with [weight(_:)](<weight(__).md>).

For example:

```swift
Font.body.bold()
```

will most likely get you the emphasized version of body text style, which is often in [semibold](weight/semibold.md) weight. While

```swift
Font.body.weight(.bold)
```

will specifically get you the body text style font in the [bold](weight/bold.md) weight.

## See Also

### Styling a font

- [italic()](<italic().md>) — Adds italics to the font.
- [monospaced()](<monospaced().md>) — Returns a fixed-width font from the same family as the base font.
- [monospacedDigit()](<monospaceddigit().md>) — Returns a modified font that uses fixed-width digits, while leaving other characters proportionally spaced.
- [smallCaps()](<smallcaps().md>) — Adjusts the font to enable all small capitals.
- [lowercaseSmallCaps()](<lowercasesmallcaps().md>) — Adjusts the font to enable lowercase small capitals.
- [uppercaseSmallCaps()](<uppercasesmallcaps().md>) — Adjusts the font to enable uppercase small capitals.
- [weight(_:)](<weight(__).md>) — Sets the weight of the font.
- [width(_:)](<width(__).md>) — Sets the width of the font.
- [Width](width.md) — A width to use for fonts that have multiple widths.
- [leading(_:)](<leading(__).md>) — Adjusts the line spacing of a font.
- [Leading](leading.md) — A line spacing adjustment that you can apply to a font.
