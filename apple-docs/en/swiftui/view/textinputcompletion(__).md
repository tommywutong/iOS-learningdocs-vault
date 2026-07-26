---
title: 'textInputCompletion(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 15.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/textinputcompletion(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/textinputcompletion(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/textinputcompletion%28_%3A%29.json'
content_hash: 'sha256:807f4f632b23a332'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# textInputCompletion(_:)

<sub>Instance Method</sub>

Associates a fully formed string with the value of this view when used as a text input suggestion

<sub>macOS</sub>

```swift
nonisolated func textInputCompletion(_ completion: String) -> some View

```

## Parameters

- `completion` — A string to use as the view’s completion.

## Discussion

Use this method to associate a fully formed string with a view that is within a text input suggestion list context. The system uses this value when the view is selected to replace the partial text being currently edited of the associated text field.

```swift
TextField("Location", text: $addressText)
    .textInputSuggestions(isEnabled: true) {
        Text("The Fillmore")
            .textInputCompletion("1805 Geary Blvd, San Francisco")
        Text("The Catalyst")
            .textInputCompletion("1011 Pacific Ave, Santa Cruz")
        Text("Rio Theatre")
            .textInputCompletion("1205 Soquel Ave, Santa Cruz")
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
- [textInputSuggestions(_:)](<textinputsuggestions(__).md>) — Configures the text input suggestions for this view.
- [textInputSuggestions(_:content:)](<textinputsuggestions(__content_).md>) — Configures the text input suggestions for this view.
- [textInputSuggestions(_:id:content:)](<textinputsuggestions(__id_content_).md>) — Configures the text input suggestions for this view.
- [textContentType(_:)](<textcontenttype(__)-4dqqb.md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on a watchOS device.
- [textContentType(_:)](<textcontenttype(__)-6fic1.md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [textContentType(_:)](<textcontenttype(__)-ufdv.md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on an iOS or tvOS device.
