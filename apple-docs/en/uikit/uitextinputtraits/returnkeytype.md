---
title: returnKeyType
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinputtraits/returnkeytype
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputtraits/returnkeytype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputtraits/returnkeytype.json'
content_hash: 'sha256:ed1764f35a565cb3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputTraits](../uitextinputtraits.md)

# returnKeyType

<sub>Instance Property</sub>

The visible indication of what the Return key does.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional var returnKeyType: UIReturnKeyType { get set }
```

## Discussion

Setting this property to a different key type changes the visible title of the Return key and typically results in the system dismissing the keyboard when it is pressed. The default value for this property is [UIReturnKeyDefault](../uireturnkeytype/default.md).

## See Also

### Configuring the keyboard appearance

- [keyboardType](keyboardtype.md) — The keyboard type for the text object.
- [UIKeyboardType](../uikeyboardtype.md) — Constants that specify the type of keyboard to display for a text-based view.
- [keyboardAppearance](keyboardappearance.md) — The appearance style of the keyboard for the text object.
- [UIKeyboardAppearance](../uikeyboardappearance.md) — Constants that specify the appearance of the keyboard for a text-based view.
- [UIReturnKeyType](../uireturnkeytype.md) — Constants that specify the type of Return key the keyboard displays.
- [textContentType](textcontenttype.md) — The semantic meaning for a text input area.
- [UITextContentType](../uitextcontenttype.md) — Constants that identify the semantic meaning for a text-entry area.
