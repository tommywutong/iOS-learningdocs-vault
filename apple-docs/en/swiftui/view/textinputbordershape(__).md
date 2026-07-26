---
title: 'textInputBorderShape(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/view/textinputbordershape(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/textinputbordershape(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/textinputbordershape%28_%3A%29.json'
content_hash: 'sha256:473dce76a1c92238'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# textInputBorderShape(_:)

<sub>Instance Method</sub>

Sets the border shape for text input controls in the view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func textInputBorderShape(_ shape: TextInputBorderShape) -> some View

```

## Parameters

- `shape` — The shape to use for the border of text input controls.

## Discussion

Use this modifier to customize the border shape of [TextField](../textfield.md) and other text input controls. The shape can be applied to individual controls or to a container to affect all text input controls within it.

In this example, a search field and button both use a capsule shape:

```swift
HStack {
    TextField("Search", text: $searchText)
    Button("Go", action: search)
}
.buttonBorderShape(.capsule)
.textInputBorderShape(.capsule)
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
- [TextInputBorderShape](../textinputbordershape.md) — A shape used to draw the border of a text input control. _(beta)_
- [textInputCompletion(_:)](<textinputcompletion(__).md>) — Associates a fully formed string with the value of this view when used as a text input suggestion
- [textInputSuggestions(_:)](<textinputsuggestions(__).md>) — Configures the text input suggestions for this view.
- [textInputSuggestions(_:content:)](<textinputsuggestions(__content_).md>) — Configures the text input suggestions for this view.
- [textInputSuggestions(_:id:content:)](<textinputsuggestions(__id_content_).md>) — Configures the text input suggestions for this view.
- [textContentType(_:)](<textcontenttype(__)-4dqqb.md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on a watchOS device.
- [textContentType(_:)](<textcontenttype(__)-6fic1.md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [textContentType(_:)](<textcontenttype(__)-ufdv.md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on an iOS or tvOS device.
