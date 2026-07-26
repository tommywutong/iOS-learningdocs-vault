---
title: keyboardAppearance
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinputtraits/keyboardappearance
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputtraits/keyboardappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputtraits/keyboardappearance.json'
content_hash: 'sha256:bb3946f800ac45fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputTraits](../uitextinputtraits.md)

# keyboardAppearance

<sub>Instance Property</sub>

The appearance style of the keyboard for the text object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional var keyboardAppearance: UIKeyboardAppearance { get set }
```

## Discussion

This property lets you distinguish between the default text entry inside your application and text entry inside an alert panel. The default value for this property is [UIKeyboardAppearanceDefault](../uikeyboardappearance/default.md).

## See Also

### Configuring the keyboard appearance

- [keyboardType](keyboardtype.md) — The keyboard type for the text object.
- [UIKeyboardType](../uikeyboardtype.md) — Constants that specify the type of keyboard to display for a text-based view.
- [UIKeyboardAppearance](../uikeyboardappearance.md) — Constants that specify the appearance of the keyboard for a text-based view.
- [returnKeyType](returnkeytype.md) — The visible indication of what the Return key does.
- [UIReturnKeyType](../uireturnkeytype.md) — Constants that specify the type of Return key the keyboard displays.
- [textContentType](textcontenttype.md) — The semantic meaning for a text input area.
- [UITextContentType](../uitextcontenttype.md) — Constants that identify the semantic meaning for a text-entry area.
