---
title: monospaced()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/font/monospaced()
source_url: 'https://developer.apple.com/documentation/swiftui/font/monospaced()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/font/monospaced%28%29.json'
content_hash: 'sha256:1077534b6c025d43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Font](../font.md)

# monospaced()

<sub>Instance Method</sub>

Returns a fixed-width font from the same family as the base font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func monospaced() -> Font
```

## Return Value

A fixed-width font from the same family as the base font, if one is available, and a default fixed-width font otherwise.

## Discussion

If there’s no suitable font face in the same family, SwiftUI returns a default fixed-width font.

The following example adds the `monospaced()` modifier to the default system font, then applies this font to a [Text](../text.md) view:

```swift
struct ContentView: View {
    let myFont = Font
        .system(size: 24)
        .monospaced()

    var body: some View {
        Text("Hello, world!")
            .font(myFont)
            .padding()
            .navigationTitle("Monospaced")
    }
}
```

![A macOS window showing the text Hello, world in a 24-point](../../../../attachments/fe6495d1d5d860442569b8e417b11198/Environment-Font-monospaced-1@2x.png)

SwiftUI may provide different fixed-width replacements for standard user interface fonts (such as [title](title.md), or a system font created with [system(_:design:)](<system(__design_).md>)) than for those same fonts when created by name with [custom(_:size:)](<custom(__size_).md>).

The [font(_:)](<../view/font(__).md>) modifier applies the font to all text within the view. To mix fixed-width text with other styles in the same `Text` view, use the [init(_:)](<../text/init(__)-1a4oh.md>) initializer to use an appropropriately-styled [AttributedString](../../foundation/attributedstring.md) for the text view’s content. You can use the [init(markdown:options:baseURL:)](<../../foundation/attributedstring/init(markdown_options_baseurl_)-52n3u.md>) initializer to provide a Markdown-formatted string containing the backtick-syntax (`…`) to apply code voice to specific ranges of the attributed string.

## See Also

### Styling a font

- [bold()](<bold().md>) — Adds bold or emphasized styling to the font.
- [italic()](<italic().md>) — Adds italics to the font.
- [monospacedDigit()](<monospaceddigit().md>) — Returns a modified font that uses fixed-width digits, while leaving other characters proportionally spaced.
- [smallCaps()](<smallcaps().md>) — Adjusts the font to enable all small capitals.
- [lowercaseSmallCaps()](<lowercasesmallcaps().md>) — Adjusts the font to enable lowercase small capitals.
- [uppercaseSmallCaps()](<uppercasesmallcaps().md>) — Adjusts the font to enable uppercase small capitals.
- [weight(_:)](<weight(__).md>) — Sets the weight of the font.
- [width(_:)](<width(__).md>) — Sets the width of the font.
- [Width](width.md) — A width to use for fonts that have multiple widths.
- [leading(_:)](<leading(__).md>) — Adjusts the line spacing of a font.
- [Leading](leading.md) — A line spacing adjustment that you can apply to a font.
