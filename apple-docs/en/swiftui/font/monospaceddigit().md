---
title: monospacedDigit()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/font/monospaceddigit()
source_url: 'https://developer.apple.com/documentation/swiftui/font/monospaceddigit()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/font/monospaceddigit%28%29.json'
content_hash: 'sha256:be503be1c5c59f33'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Font](../font.md)

# monospacedDigit()

<sub>Instance Method</sub>

Returns a modified font that uses fixed-width digits, while leaving other characters proportionally spaced.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func monospacedDigit() -> Font
```

## Return Value

A font that uses fixed-width numeric characters.

## Discussion

This modifier only affects numeric characters, and leaves all other characters unchanged. If the base font doesn’t support fixed-width, or _monospace_ digits, the font remains unchanged.

The following example shows two text fields arranged in a [VStack](../vstack.md). Both text fields specify the 12-point system font, with the second adding the `monospacedDigit()` modifier to the font. Because the text includes the digit 1, normally a narrow character in proportional fonts, the second text field becomes wider than the first.

```swift
@State private var userText = "Effect of monospacing digits: 111,111."

var body: some View {
    VStack {
        TextField("Proportional", text: $userText)
            .font(.system(size: 12))
        TextField("Monospaced", text: $userText)
            .font(.system(size: 12).monospacedDigit())
    }
    .padding()
    .navigationTitle(Text("Font + monospacedDigit()"))
}
```

![A macOS window showing two text fields arranged vertically. Each](../../../../attachments/43f6da3f34065ab05d51b981cd5e9240/Environment-Font-monospacedDigit-1@2x.png)

## See Also

### Styling a font

- [bold()](<bold().md>) — Adds bold or emphasized styling to the font.
- [italic()](<italic().md>) — Adds italics to the font.
- [monospaced()](<monospaced().md>) — Returns a fixed-width font from the same family as the base font.
- [smallCaps()](<smallcaps().md>) — Adjusts the font to enable all small capitals.
- [lowercaseSmallCaps()](<lowercasesmallcaps().md>) — Adjusts the font to enable lowercase small capitals.
- [uppercaseSmallCaps()](<uppercasesmallcaps().md>) — Adjusts the font to enable uppercase small capitals.
- [weight(_:)](<weight(__).md>) — Sets the weight of the font.
- [width(_:)](<width(__).md>) — Sets the width of the font.
- [Width](width.md) — A width to use for fonts that have multiple widths.
- [leading(_:)](<leading(__).md>) — Adjusts the line spacing of a font.
- [Leading](leading.md) — A line spacing adjustment that you can apply to a font.
