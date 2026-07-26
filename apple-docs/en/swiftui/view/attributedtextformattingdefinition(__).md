---
title: 'attributedTextFormattingDefinition(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/attributedtextformattingdefinition(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/attributedtextformattingdefinition(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/attributedtextformattingdefinition%28_%3A%29.json'
content_hash: 'sha256:8dc325d26227f9ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# attributedTextFormattingDefinition(_:)

<sub>Instance Method</sub>

Apply a text formatting definition to nested views.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func attributedTextFormattingDefinition<D>(_ definition: D) -> some View where D : AttributedTextFormattingDefinition

```

## Discussion

Applying a text formatting definition to a [Text](../text.md) or [TextEditor](../texteditor.md) created using the [init(_:)](<../text/init(__)-1a4oh.md>) or [init(text:selection:)](<../texteditor/init(text_selection_).md>) initializer, respectively, makes sure that any content observable to the user adheres to the constraints of the formatting definition.

You can compose your own definition from an attribute scope and a series of [AttributedTextValueConstraint](../attributedtextvalueconstraint.md)s:

```swift
// MyTextFormattingDefinition.swift

struct MyTextFormattingDefinition: AttributedTextFormattingDefinition {
    var body: some AttributedTextFormattingDefinition<
        AttributeScopes.SwiftUIAttributes
    > {
        ValueConstraint(
            for: \.underlineStyle,
            values: [nil, .single],
            default: .single)
        MyAttributedTextValueConstraint()
    }
}

// MyEditorView.swift

TextEditor(text: $text)
    .attributedTextFormattingDefinition(MyTextFormattingDefinition())
```

> [!note] Note
> A [Binding](../binding.md) to the text of a view with an [AttributedTextFormattingDefinition](../attributedtextformattingdefinition.md) may still contain values that do not adhere to text formatting definition. E.g., a [TextEditor](../texteditor.md) may choose to not apply constraints in the text formatting definition to parts of a bound attributed string that are not visible on screen.

To manually enforce constraints, e.g. before serializing text contents, use the [constrain(_:)](<../attributedtextformattingdefinition/constrain(__)-1ur9c.md>) method.

## See Also

### Text style

- [bold(_:)](<bold(__).md>) — Applies a bold font weight to the text in this view.
- [fontDesign(_:)](<fontdesign(__).md>) — Sets the font design of the text in this view.
- [fontWeight(_:)](<fontweight(__).md>) — Sets the font weight of the text in this view.
- [fontWidth(_:)](<fontwidth(__).md>) — Sets the font width of the text in this view.
- [italic(_:)](<italic(__).md>) — Applies italics to the text in this view.
- [monospaced(_:)](<monospaced(__).md>) — Modifies the fonts of all child views to use the fixed-width variant of the current font, if possible.
- [monospacedDigit()](<monospaceddigit().md>) — Modifies the fonts of all child views to use fixed-width digits, if possible, while leaving other characters proportionally spaced.
- [strikethrough(_:pattern:color:)](<strikethrough(__pattern_color_).md>) — Applies a strikethrough to the text in this view.
- [textCase(_:)](<textcase(__).md>) — Sets a transform for the case of the text contained in this view when displayed.
- [textScale(_:isEnabled:)](<textscale(__isenabled_).md>) — Applies a text scale to text in the view.
- [textRenderer(_:)](<textrenderer(__).md>) — Returns a new view such that any text views within it will use `renderer` to draw themselves.
- [underline(_:pattern:color:)](<underline(__pattern_color_).md>) — Applies an underline to the text in this view.
