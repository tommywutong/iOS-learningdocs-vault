---
title: keyboardType
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinputtraits/keyboardtype
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputtraits/keyboardtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputtraits/keyboardtype.json'
content_hash: 'sha256:3c0864633270b89a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputTraits](../uitextinputtraits.md)

# keyboardType

<sub>Instance Property</sub>

The keyboard type for the text object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional var keyboardType: UIKeyboardType { get set }
```

## Discussion

Text objects can be targeted for specific types of input, such as plain text, email, numeric entry, and so on. The keyboard style identifies what keys are available on the keyboard and which ones appear by default. The default value for this property is [UIKeyboardTypeDefault](../uikeyboardtype/default.md).

## See Also

### Configuring the keyboard appearance

- [UIKeyboardType](../uikeyboardtype.md) — Constants that specify the type of keyboard to display for a text-based view.
- [keyboardAppearance](keyboardappearance.md) — The appearance style of the keyboard for the text object.
- [UIKeyboardAppearance](../uikeyboardappearance.md) — Constants that specify the appearance of the keyboard for a text-based view.
- [returnKeyType](returnkeytype.md) — The visible indication of what the Return key does.
- [UIReturnKeyType](../uireturnkeytype.md) — Constants that specify the type of Return key the keyboard displays.
- [textContentType](textcontenttype.md) — The semantic meaning for a text input area.
- [UITextContentType](../uitextcontenttype.md) — Constants that identify the semantic meaning for a text-entry area.
