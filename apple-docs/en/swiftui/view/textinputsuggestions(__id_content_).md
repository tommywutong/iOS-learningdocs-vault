---
title: 'textInputSuggestions(_:id:content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 15.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/textinputsuggestions(_:id:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/textinputsuggestions(_:id:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/textinputsuggestions%28_%3Aid%3Acontent%3A%29.json'
content_hash: 'sha256:f68a448f2c6fd50f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# textInputSuggestions(_:id:content:)

<sub>Instance Method</sub>

Configures the text input suggestions for this view.

<sub>macOS</sub>

```swift
nonisolated func textInputSuggestions<Data, ID, Content>(_ data: Data, id: KeyPath<Data.Element, ID>, @ContentBuilder content: @escaping (Data.Element) -> Content) -> some View where Data : RandomAccessCollection, ID : Hashable, Content : View

```

## Parameters

- `data` — The data that is used to create views dynamically.

- `id` — The key path to the provided data’s identifier.

- `content` — The content builder that creates views dynamically.

## Discussion

You can suggest text completions during a text input operation by providing data to this modifier. The interface presents the suggestion views as a list of choices when someone activates the text editing interface.

Associate a string with each suggestion view by adding the [textInputCompletion(_:)](<textinputcompletion(__).md>) modifier to the view.

Use `Label` to get platform-standard visual representations of suggestion text accompanied with images, and `Section` for labelled sections of results.

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
- [textContentType(_:)](<textcontenttype(__)-4dqqb.md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on a watchOS device.
- [textContentType(_:)](<textcontenttype(__)-6fic1.md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [textContentType(_:)](<textcontenttype(__)-ufdv.md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on an iOS or tvOS device.
