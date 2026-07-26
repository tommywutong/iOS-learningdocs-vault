---
title: 'leading(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/font/leading(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/font/leading(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/font/leading%28_%3A%29.json'
content_hash: 'sha256:965f88226cb6ecb2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Font](../font.md)

# leading(_:)

<sub>Instance Method</sub>

Adjusts the line spacing of a font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func leading(_ leading: Font.Leading) -> Font
```

## Parameters

- `leading` — The line spacing adjustment to apply.

## Return Value

A modified font that uses the specified line spacing, or the original font if it doesn’t support line spacing adjustments.

## Discussion

You can change a font’s line spacing while maintaining other characteristics of the font by applying this modifier. For example, you can decrease spacing of the [body](body.md) font by applying the [Font.Leading.tight](leading/tight.md) value to it:

```swift
let myFont = Font.body.leading(.tight)
```

The availability of leading adjustments depends on the font. For some fonts, the modifier has no effect and returns the original font.

## See Also

### Styling a font

- [bold()](<bold().md>) — Adds bold or emphasized styling to the font.
- [italic()](<italic().md>) — Adds italics to the font.
- [monospaced()](<monospaced().md>) — Returns a fixed-width font from the same family as the base font.
- [monospacedDigit()](<monospaceddigit().md>) — Returns a modified font that uses fixed-width digits, while leaving other characters proportionally spaced.
- [smallCaps()](<smallcaps().md>) — Adjusts the font to enable all small capitals.
- [lowercaseSmallCaps()](<lowercasesmallcaps().md>) — Adjusts the font to enable lowercase small capitals.
- [uppercaseSmallCaps()](<uppercasesmallcaps().md>) — Adjusts the font to enable uppercase small capitals.
- [weight(_:)](<weight(__).md>) — Sets the weight of the font.
- [width(_:)](<width(__).md>) — Sets the width of the font.
- [Width](width.md) — A width to use for fonts that have multiple widths.
- [Leading](leading.md) — A line spacing adjustment that you can apply to a font.
