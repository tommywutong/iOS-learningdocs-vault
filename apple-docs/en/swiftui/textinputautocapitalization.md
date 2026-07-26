---
title: TextInputAutocapitalization
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/textinputautocapitalization
source_url: 'https://developer.apple.com/documentation/swiftui/textinputautocapitalization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textinputautocapitalization.json'
content_hash: 'sha256:7025765c2abcc366'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TextInputAutocapitalization

<sub>Structure</sub>

The kind of autocapitalization behavior applied during text input.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct TextInputAutocapitalization
```

## Overview

Pass an instance of `TextInputAutocapitalization` to the [textInputAutocapitalization(_:)](<view/textinputautocapitalization(__).md>) view modifier.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting autocapitalization options

- [characters](textinputautocapitalization/characters.md) — Defines an autocapitalizing behavior that will capitalize every letter.
- [sentences](textinputautocapitalization/sentences.md) — Defines an autocapitalizing behavior that will capitalize the first letter in every sentence.
- [words](textinputautocapitalization/words.md) — Defines an autocapitalizing behavior that will capitalize the first letter of every word.
- [never](textinputautocapitalization/never.md) — Defines an autocapitalizing behavior that will not capitalize anything.

### Creating an autocapitalization type

- [init(_:)](<textinputautocapitalization/init(__).md>) — Creates a new [TextInputAutocapitalization](textinputautocapitalization.md) struct from a `UITextAutocapitalizationType` enum.

## See Also

### Managing text entry

- [autocorrectionDisabled(_:)](<view/autocorrectiondisabled(__).md>) — Sets whether to disable autocorrection for this view.
- [autocorrectionDisabled](environmentvalues/autocorrectiondisabled.md) — A Boolean value that determines whether the view hierarchy has auto-correction enabled.
- [keyboardType(_:)](<view/keyboardtype(__).md>) — Sets the keyboard type for this view.
- [scrollDismissesKeyboard(_:)](<view/scrolldismisseskeyboard(__).md>) — Configures the behavior in which scrollable content interacts with the software keyboard.
- [textContentType(_:)](<view/textcontenttype(__).md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [textInputAutocapitalization(_:)](<view/textinputautocapitalization(__).md>) — Sets how often the shift key in the keyboard is automatically enabled.
- [textInputBorderShape(_:)](<view/textinputbordershape(__).md>) — Sets the border shape for text input controls in the view hierarchy. _(beta)_
- [TextInputBorderShape](textinputbordershape.md) — A shape used to draw the border of a text input control. _(beta)_
- [textInputCompletion(_:)](<view/textinputcompletion(__).md>) — Associates a fully formed string with the value of this view when used as a text input suggestion
- [textInputSuggestions(_:)](<view/textinputsuggestions(__).md>) — Configures the text input suggestions for this view.
- [textInputSuggestions(_:content:)](<view/textinputsuggestions(__content_).md>) — Configures the text input suggestions for this view.
- [textInputSuggestions(_:id:content:)](<view/textinputsuggestions(__id_content_).md>) — Configures the text input suggestions for this view.
- [textContentType(_:)](<view/textcontenttype(__)-4dqqb.md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on a watchOS device.
- [textContentType(_:)](<view/textcontenttype(__)-6fic1.md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [textContentType(_:)](<view/textcontenttype(__)-ufdv.md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on an iOS or tvOS device.
