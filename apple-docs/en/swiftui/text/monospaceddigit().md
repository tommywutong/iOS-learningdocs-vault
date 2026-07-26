---
title: monospacedDigit()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/text/monospaceddigit()
source_url: 'https://developer.apple.com/documentation/swiftui/text/monospaceddigit()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/monospaceddigit%28%29.json'
content_hash: 'sha256:f71c9360f973274b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Text](../text.md)

# monospacedDigit()

<sub>Instance Method</sub>

Modifies the text view’s font to use fixed-width digits, while leaving other characters proportionally spaced.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func monospacedDigit() -> Text
```

## Return Value

A text view with a modified font that uses fixed-width numeric characters, while leaving other characters proportionally spaced.

## Discussion

This modifier only affects numeric characters, and leaves all other characters unchanged.

The following example shows the effect of `monospacedDigit()` on a text view. It arranges two text views in a [VStack](../vstack.md), each displaying a formatted date that contains many instances of the character 1. The second text view uses the `monospacedDigit()`. Because 1 is usually a narrow character in proportional fonts, applying the modifier widens all of the 1s, and the text view as a whole. The non-digit characters in the text view remain unaffected.

```swift
let myDate = DateComponents(
    calendar: Calendar(identifier: .gregorian),
    timeZone: TimeZone(identifier: "EST"),
    year: 2011,
    month: 1,
    day: 11,
    hour: 11,
    minute: 11
).date!

var body: some View {
    VStack(alignment: .leading) {
        Text(myDate.formatted(date: .long, time: .complete))
            .font(.system(size: 20))
        Text(myDate.formatted(date: .long, time: .complete))
            .font(.system(size: 20))
            .monospacedDigit()
    }
    .padding()
    .navigationTitle("monospacedDigit() Modifier")
}
```

![Two vertically stacked text views, displaying the date January 11,](../../../../attachments/b7e28c98f5e43223b077b81b7fab9dd6/Text-monospacedDigit-1@2x.png)

If the base font of the text view doesn’t support fixed-width digits, the font remains unchanged.

## See Also

### Styling the view’s text

- [foregroundStyle(_:)](<foregroundstyle(__).md>) — Sets the style of the text displayed by this view.
- [bold()](<bold().md>) — Applies a bold or emphasized treatment to the fonts of the text.
- [bold(_:)](<bold(__).md>) — Applies a bold font weight to the text.
- [italic()](<italic().md>) — Applies italics to the text.
- [italic(_:)](<italic(__).md>) — Applies italics to the text.
- [strikethrough(_:color:)](<strikethrough(__color_).md>) — Applies a strikethrough to the text.
- [strikethrough(_:pattern:color:)](<strikethrough(__pattern_color_).md>) — Applies a strikethrough to the text.
- [underline(_:color:)](<underline(__color_).md>) — Applies an underline to the text.
- [underline(_:pattern:color:)](<underline(__pattern_color_).md>) — Applies an underline to the text.
- [monospaced(_:)](<monospaced(__).md>) — Modifies the font of the text to use the fixed-width variant of the current font, if possible.
- [kerning(_:)](<kerning(__).md>) — Sets the spacing, or kerning, between characters.
- [tracking(_:)](<tracking(__).md>) — Sets the tracking for the text.
- [baselineOffset(_:)](<baselineoffset(__).md>) — Sets the vertical offset for the text relative to its baseline.
- [Case](case.md) — A scheme for transforming the capitalization of characters within text.
- [DateStyle](datestyle.md) — A predefined style used to display a `Date`.
