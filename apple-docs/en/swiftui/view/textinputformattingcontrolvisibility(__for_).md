---
title: 'textInputFormattingControlVisibility(_:for:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/textinputformattingcontrolvisibility(_:for:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/textinputformattingcontrolvisibility(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/textinputformattingcontrolvisibility%28_%3Afor%3A%29.json'
content_hash: 'sha256:def0efdbb0fcc65c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# textInputFormattingControlVisibility(_:for:)

<sub>Instance Method</sub>

Specifies which system text formatting controls are available for people to format text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func textInputFormattingControlVisibility(_ visibility: Visibility, for placement: TextInputFormattingControlPlacement.Set) -> some View

```

## Parameters

- `visibility` — Whether the controls in the given placements may become visible.

- `placement` — The onscreen control to modify.

## Discussion

A [TextEditor](../texteditor.md) with a binding to an `AttributedString` offers built-in controls for formatting text. These controls appear in different placements depending on the platform. By default, `TextEditor` shows them in the context menu and in the keyboard toolbar on iOS. See [Set](../textinputformattingcontrolplacement/set.md) for the available placements.

In this example, the formatting accessory bar is shown in a macOS editor:

```swift
struct StyledTextEditingView: View {
    @State private var text: AttributedString = ""

    var body: some View {
        TextEditor(text: $text)
            .textInputFormattingControlVisibility(.visible, for: .accessoryBar)
    }
}
```

## See Also

### Managing text entry

- [autocorrectionDisabled(_:)](<autocorrectiondisabled(__).md>) — Sets whether to disable autocorrection for this view.
- [autocorrectionDisabled](../environmentvalues/autocorrectiondisabled.md) — A Boolean value that determines whether the view hierarchy has auto-correction enabled.
- [keyboardType(_:)](<keyboardtype(__).md>) — Sets the keyboard type for this view.
- [scrollDismissesKeyboard(_:)](<scrolldismisseskeyboard(__).md>) — Configures the behavior in which scrollable content interacts with the software keyboard.
- [textContentType(_:)](<textcontenttype(__).md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [textInputAutocapitalization(_:)](<textinputautocapitalization(__).md>) — Sets how often the shift key in the keyboard is automatically enabled.
- [TextInputAutocapitalization](../textinputautocapitalization.md) — The kind of autocapitalization behavior applied during text input.
- [textInputBorderShape(_:)](<textinputbordershape(__).md>) — Sets the border shape for text input controls in the view hierarchy. _(beta)_
- [TextInputBorderShape](../textinputbordershape.md) — A shape used to draw the border of a text input control. _(beta)_
- [textInputCompletion(_:)](<textinputcompletion(__).md>) — Associates a fully formed string with the value of this view when used as a text input suggestion
- [textInputSuggestions(_:)](<textinputsuggestions(__).md>) — Configures the text input suggestions for this view.
- [textInputSuggestions(_:content:)](<textinputsuggestions(__content_).md>) — Configures the text input suggestions for this view.
- [textInputSuggestions(_:id:content:)](<textinputsuggestions(__id_content_).md>) — Configures the text input suggestions for this view.
- [textContentType(_:)](<textcontenttype(__)-4dqqb.md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on a watchOS device.
- [textContentType(_:)](<textcontenttype(__)-6fic1.md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
