---
title: textInputMode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiresponder/textinputmode
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/textinputmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/textinputmode.json'
content_hash: 'sha256:76b5a28538f76a2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# textInputMode

<sub>Instance Property</sub>

The text input mode for this responder object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var textInputMode: UITextInputMode? { get }
```

## Discussion

The text input mode identifies the language and keyboard displayed when this responder is active.

For responders, the system normally displays a keyboard that’s based on the user’s language preferences. You can redefine this property and use it to return a different text input mode in cases where you want a responder to use a specific keyboard. The user can still change the keyboard while the responder is active, but switching away to another responder and then back restores the keyboard you specified.

## See Also

### Managing the text input mode

- [textInputContextIdentifier](textinputcontextidentifier.md) — An identifier signifying that the responder should preserve its text input mode information.
- [+ clearTextInputContextIdentifier:](<cleartextinputcontextidentifier(__).md>) — Clears text input mode information from the app’s user defaults.
- [inputAssistantItem](inputassistantitem.md) — The input assistant to use when configuring the keyboard’s shortcuts bar.
