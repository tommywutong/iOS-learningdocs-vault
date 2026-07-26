---
title: textInputContextIdentifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiresponder/textinputcontextidentifier
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/textinputcontextidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/textinputcontextidentifier.json'
content_hash: 'sha256:1d6c01a642a0ef07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# textInputContextIdentifier

<sub>Instance Property</sub>

An identifier signifying that the responder should preserve its text input mode information.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var textInputContextIdentifier: String? { get }
```

## Discussion

If you redefine this property and return a string value, UIKit tracks the current text input mode for the responder. While in tracking mode, any programmatic changes you make to the text input mode are remembered and restored whenever the responder becomes active.

## See Also

### Managing the text input mode

- [textInputMode](textinputmode.md) — The text input mode for this responder object.
- [+ clearTextInputContextIdentifier:](<cleartextinputcontextidentifier(__).md>) — Clears text input mode information from the app’s user defaults.
- [inputAssistantItem](inputassistantitem.md) — The input assistant to use when configuring the keyboard’s shortcuts bar.
