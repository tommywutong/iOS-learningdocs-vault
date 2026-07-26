---
title: 'underline(_:pattern:color:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/underline(_:pattern:color:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/underline(_:pattern:color:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/underline%28_%3Apattern%3Acolor%3A%29.json'
content_hash: 'sha256:ad42e352c7c08177'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# underline(_:pattern:color:)

<sub>Instance Method</sub>

Applies an underline to the text in this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func underline(_ isActive: Bool = true, pattern: Text.LineStyle.Pattern = .solid, color: Color? = nil) -> some View

```

## Parameters

- `isActive` — A Boolean value that indicates whether underline is added. The default value is `true`.

- `pattern` — The pattern of the line. The default value is `solid`.

- `color` — The color of the underline. If `color` is `nil`, the underline uses the default foreground color.

## Return Value

A view where text has a line running along its baseline.

## See Also

### Controlling text style

- [bold(_:)](<bold(__).md>) — Applies a bold font weight to the text in this view.
- [italic(_:)](<italic(__).md>) — Applies italics to the text in this view.
- [strikethrough(_:pattern:color:)](<strikethrough(__pattern_color_).md>) — Applies a strikethrough to the text in this view.
- [textCase(_:)](<textcase(__).md>) — Sets a transform for the case of the text contained in this view when displayed.
- [textCase](../environmentvalues/textcase.md) — A stylistic override to transform the case of `Text` when displayed, using the environment’s locale.
- [monospaced(_:)](<monospaced(__).md>) — Modifies the fonts of all child views to use the fixed-width variant of the current font, if possible.
- [monospacedDigit()](<monospaceddigit().md>) — Modifies the fonts of all child views to use fixed-width digits, if possible, while leaving other characters proportionally spaced.
- [AttributedTextFormattingDefinition](../attributedtextformattingdefinition.md) — A protocol for defining how text can be styled in a view.
- [AttributedTextValueConstraint](../attributedtextvalueconstraint.md) — A protocol for defining a constraint on the value of a certain attribute.
- [AttributedTextFormatting](../attributedtextformatting.md) — A namespace for types related to attributed text formatting definitions.
