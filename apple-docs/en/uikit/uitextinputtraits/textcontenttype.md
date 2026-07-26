---
title: textContentType
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinputtraits/textcontenttype
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputtraits/textcontenttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputtraits/textcontenttype.json'
content_hash: 'sha256:2758b0ee8a1f2705'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputTraits](../uitextinputtraits.md)

# textContentType

<sub>Instance Property</sub>

The semantic meaning for a text input area.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional var textContentType: UITextContentType! { get set }
```

## Discussion

Use this property to give the keyboard and the system information about the expected semantic meaning for the content that users enter. For example, you might specify [UITextContentTypeEmailAddress](../uitextcontenttype/emailaddress.md) for a text field that users fill in to receive an email confirmation. When you provide this information about the content you expect users to enter in a text input area, the system can in some cases automatically select an appropriate keyboard and improve keyboard corrections and proactive integration with other text input opportunities.

Because the expected semantic meaning for each text input area should be identified as specifically as possible, you can’t combine multiple values for one [textContentType](textcontenttype.md) property. For possible values you can use, see [UITextContentType](../uitextcontenttype.md); by default, the value of this property is `nil`.

## See Also

### Configuring the keyboard appearance

- [keyboardType](keyboardtype.md) — The keyboard type for the text object.
- [UIKeyboardType](../uikeyboardtype.md) — Constants that specify the type of keyboard to display for a text-based view.
- [keyboardAppearance](keyboardappearance.md) — The appearance style of the keyboard for the text object.
- [UIKeyboardAppearance](../uikeyboardappearance.md) — Constants that specify the appearance of the keyboard for a text-based view.
- [returnKeyType](returnkeytype.md) — The visible indication of what the Return key does.
- [UIReturnKeyType](../uireturnkeytype.md) — Constants that specify the type of Return key the keyboard displays.
- [UITextContentType](../uitextcontenttype.md) — Constants that identify the semantic meaning for a text-entry area.
