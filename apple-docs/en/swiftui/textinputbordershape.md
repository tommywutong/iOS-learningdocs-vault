---
title: TextInputBorderShape
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/textinputbordershape
source_url: 'https://developer.apple.com/documentation/swiftui/textinputbordershape'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textinputbordershape.json'
content_hash: 'sha256:7e7b051d9789499e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TextInputBorderShape

<sub>Structure</sub>

A shape used to draw the border of a text input control.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TextInputBorderShape
```

## Relationships

- **Conforms To**: [Animatable](animatable.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [InsettableShape](insettableshape.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Shape](shape.md), [View](view.md)

## Topics

### Getting border shape options

- [automatic](textinputbordershape/automatic.md) — A shape that defers to the system to determine an appropriate shape for the given context and platform. _(beta)_
- [capsule](textinputbordershape/capsule.md) — A capsule shape. _(beta)_
- [roundedRectangle](textinputbordershape/roundedrectangle.md) — A rounded rectangle shape. _(beta)_

## See Also

### Managing text entry

- [autocorrectionDisabled(_:)](<view/autocorrectiondisabled(__).md>) — Sets whether to disable autocorrection for this view.
- [autocorrectionDisabled](environmentvalues/autocorrectiondisabled.md) — A Boolean value that determines whether the view hierarchy has auto-correction enabled.
- [keyboardType(_:)](<view/keyboardtype(__).md>) — Sets the keyboard type for this view.
- [scrollDismissesKeyboard(_:)](<view/scrolldismisseskeyboard(__).md>) — Configures the behavior in which scrollable content interacts with the software keyboard.
- [textContentType(_:)](<view/textcontenttype(__).md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [textInputAutocapitalization(_:)](<view/textinputautocapitalization(__).md>) — Sets how often the shift key in the keyboard is automatically enabled.
- [TextInputAutocapitalization](textinputautocapitalization.md) — The kind of autocapitalization behavior applied during text input.
- [textInputBorderShape(_:)](<view/textinputbordershape(__).md>) — Sets the border shape for text input controls in the view hierarchy. _(beta)_
- [textInputCompletion(_:)](<view/textinputcompletion(__).md>) — Associates a fully formed string with the value of this view when used as a text input suggestion
- [textInputSuggestions(_:)](<view/textinputsuggestions(__).md>) — Configures the text input suggestions for this view.
- [textInputSuggestions(_:content:)](<view/textinputsuggestions(__content_).md>) — Configures the text input suggestions for this view.
- [textInputSuggestions(_:id:content:)](<view/textinputsuggestions(__id_content_).md>) — Configures the text input suggestions for this view.
- [textContentType(_:)](<view/textcontenttype(__)-4dqqb.md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on a watchOS device.
- [textContentType(_:)](<view/textcontenttype(__)-6fic1.md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [textContentType(_:)](<view/textcontenttype(__)-ufdv.md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on an iOS or tvOS device.
