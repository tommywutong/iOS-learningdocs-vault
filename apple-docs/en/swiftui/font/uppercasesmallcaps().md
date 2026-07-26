---
title: uppercaseSmallCaps()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/font/uppercasesmallcaps()
source_url: 'https://developer.apple.com/documentation/swiftui/font/uppercasesmallcaps()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/font/uppercasesmallcaps%28%29.json'
content_hash: 'sha256:487240d89e6a2771'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Font](../font.md)

# uppercaseSmallCaps()

<sub>Instance Method</sub>

Adjusts the font to enable uppercase small capitals.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func uppercaseSmallCaps() -> Font
```

## Discussion

This feature turns capital characters into small capitals. It is generally used for words which would otherwise be set in all caps, such as acronyms, but which are desired in small-cap form to avoid disrupting the flow of text.

## See Also

### Styling a font

- [bold()](<bold().md>) — Adds bold or emphasized styling to the font.
- [italic()](<italic().md>) — Adds italics to the font.
- [monospaced()](<monospaced().md>) — Returns a fixed-width font from the same family as the base font.
- [monospacedDigit()](<monospaceddigit().md>) — Returns a modified font that uses fixed-width digits, while leaving other characters proportionally spaced.
- [smallCaps()](<smallcaps().md>) — Adjusts the font to enable all small capitals.
- [lowercaseSmallCaps()](<lowercasesmallcaps().md>) — Adjusts the font to enable lowercase small capitals.
- [weight(_:)](<weight(__).md>) — Sets the weight of the font.
- [width(_:)](<width(__).md>) — Sets the width of the font.
- [Width](width.md) — A width to use for fonts that have multiple widths.
- [leading(_:)](<leading(__).md>) — Adjusts the line spacing of a font.
- [Leading](leading.md) — A line spacing adjustment that you can apply to a font.
