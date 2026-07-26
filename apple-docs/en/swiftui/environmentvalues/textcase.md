---
title: textCase
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/textcase
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/textcase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/textcase.json'
content_hash: 'sha256:af682db1e3b94bf9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# textCase

<sub>Instance Property</sub>

A stylistic override to transform the case of `Text` when displayed, using the environment’s locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var textCase: Text.Case? { get set }
```

## Discussion

The default value is `nil`, displaying the `Text` without any case changes.

## See Also

### Controlling text style

- [bold(_:)](<../view/bold(__).md>) — Applies a bold font weight to the text in this view.
- [italic(_:)](<../view/italic(__).md>) — Applies italics to the text in this view.
- [underline(_:pattern:color:)](<../view/underline(__pattern_color_).md>) — Applies an underline to the text in this view.
- [strikethrough(_:pattern:color:)](<../view/strikethrough(__pattern_color_).md>) — Applies a strikethrough to the text in this view.
- [textCase(_:)](<../view/textcase(__).md>) — Sets a transform for the case of the text contained in this view when displayed.
- [monospaced(_:)](<../view/monospaced(__).md>) — Modifies the fonts of all child views to use the fixed-width variant of the current font, if possible.
- [monospacedDigit()](<../view/monospaceddigit().md>) — Modifies the fonts of all child views to use fixed-width digits, if possible, while leaving other characters proportionally spaced.
- [AttributedTextFormattingDefinition](../attributedtextformattingdefinition.md) — A protocol for defining how text can be styled in a view.
- [AttributedTextValueConstraint](../attributedtextvalueconstraint.md) — A protocol for defining a constraint on the value of a certain attribute.
- [AttributedTextFormatting](../attributedtextformatting.md) — A namespace for types related to attributed text formatting definitions.
