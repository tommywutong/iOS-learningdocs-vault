---
title: 'textInputAutocapitalization(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/textinputautocapitalization(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/textinputautocapitalization(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/textinputautocapitalization%28_%3A%29.json'
content_hash: 'sha256:b89c7bdc880de935'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# textInputAutocapitalization(_:)

<sub>Instance Method</sub>

Sets how often the shift key in the keyboard is automatically enabled.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func textInputAutocapitalization(_ autocapitalization: TextInputAutocapitalization?) -> some View

```

## Parameters

- `autocapitalization` — One of the capitalizing behaviors defined in the [TextInputAutocapitalization](../textinputautocapitalization.md) struct or nil.

## Discussion

Use `textInputAutocapitalization(_:)` when you need to automatically capitalize words, sentences, or other text like proper nouns.

In example below, as the user enters text the shift key is automatically enabled before every word:

```swift
TextField("Last, First", text: $fullName)
    .textInputAutocapitalization(.words)
```

The [TextInputAutocapitalization](../textinputautocapitalization.md) struct defines the available autocapitalizing behavior. Providing `nil` to  this view modifier does not change the autocapitalization behavior. The default is `TextInputAutocapitalization.sentences`.

## See Also

### Managing text entry

- [autocorrectionDisabled(_:)](<autocorrectiondisabled(__).md>) — Sets whether to disable autocorrection for this view.
- [autocorrectionDisabled](../environmentvalues/autocorrectiondisabled.md) — A Boolean value that determines whether the view hierarchy has auto-correction enabled.
- [keyboardType(_:)](<keyboardtype(__).md>) — Sets the keyboard type for this view.
- [scrollDismissesKeyboard(_:)](<scrolldismisseskeyboard(__).md>) — Configures the behavior in which scrollable content interacts with the software keyboard.
- [textContentType(_:)](<textcontenttype(__).md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [TextInputAutocapitalization](../textinputautocapitalization.md) — The kind of autocapitalization behavior applied during text input.
- [textInputBorderShape(_:)](<textinputbordershape(__).md>) — Sets the border shape for text input controls in the view hierarchy. _(beta)_
- [TextInputBorderShape](../textinputbordershape.md) — A shape used to draw the border of a text input control. _(beta)_
- [textInputCompletion(_:)](<textinputcompletion(__).md>) — Associates a fully formed string with the value of this view when used as a text input suggestion
- [textInputSuggestions(_:)](<textinputsuggestions(__).md>) — Configures the text input suggestions for this view.
- [textInputSuggestions(_:content:)](<textinputsuggestions(__content_).md>) — Configures the text input suggestions for this view.
- [textInputSuggestions(_:id:content:)](<textinputsuggestions(__id_content_).md>) — Configures the text input suggestions for this view.
- [textContentType(_:)](<textcontenttype(__)-4dqqb.md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on a watchOS device.
- [textContentType(_:)](<textcontenttype(__)-6fic1.md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [textContentType(_:)](<textcontenttype(__)-ufdv.md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on an iOS or tvOS device.
