---
title: UIKeyboardType
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uikeyboardtype
source_url: 'https://developer.apple.com/documentation/uikit/uikeyboardtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikeyboardtype.json'
content_hash: 'sha256:59cb81b7e1781d17'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIKeyboardType

<sub>Enumeration</sub>

Constants that specify the type of keyboard to display for a text-based view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UIKeyboardType
```

## Overview

Use these constants with the [keyboardType](uitextinputtraits/keyboardtype.md) property.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UIKeyboardTypeDefault](uikeyboardtype/default.md) — Specifies the default keyboard for the current input method.
- [UIKeyboardTypeASCIICapable](uikeyboardtype/asciicapable.md) — Specifies a keyboard that displays standard ASCII characters.
- [UIKeyboardTypeNumbersAndPunctuation](uikeyboardtype/numbersandpunctuation.md) — Specifies the numbers and punctuation keyboard.
- [UIKeyboardTypeURL](uikeyboardtype/url.md) — Specifies a keyboard for URL entry.
- [UIKeyboardTypeNumberPad](uikeyboardtype/numberpad.md) — Specifies a numeric keypad for PIN entry.
- [UIKeyboardTypePhonePad](uikeyboardtype/phonepad.md) — Specifies a keypad for entering telephone numbers.
- [UIKeyboardTypeNamePhonePad](uikeyboardtype/namephonepad.md) — Specifies a keypad for entering a person’s name or phone number.
- [UIKeyboardTypeEmailAddress](uikeyboardtype/emailaddress.md) — Specifies a keyboard for entering email addresses.
- [UIKeyboardTypeDecimalPad](uikeyboardtype/decimalpad.md) — Specifies a keyboard with numbers and a decimal point.
- [UIKeyboardTypeTwitter](uikeyboardtype/twitter.md) — Specifies a keyboard for Twitter text entry, with easy access to the at (”`@`”) and hash (”`#`”) characters.
- [UIKeyboardTypeWebSearch](uikeyboardtype/websearch.md) — Specifies a keyboard for web search terms and URL entry.
- [UIKeyboardTypeASCIICapableNumberPad](uikeyboardtype/asciicapablenumberpad.md) — Specifies a number pad that outputs only ASCII digits.
- [UIKeyboardTypeAlphabet](uikeyboardtype/alphabet.md) — Specifies a keyboard for alphabetic entry. _(deprecated)_

### Initializers

- [init(rawValue:)](<uikeyboardtype/init(rawvalue_).md>)

## See Also

### Configuring the keyboard appearance

- [keyboardType](uitextinputtraits/keyboardtype.md) — The keyboard type for the text object.
- [keyboardAppearance](uitextinputtraits/keyboardappearance.md) — The appearance style of the keyboard for the text object.
- [UIKeyboardAppearance](uikeyboardappearance.md) — Constants that specify the appearance of the keyboard for a text-based view.
- [returnKeyType](uitextinputtraits/returnkeytype.md) — The visible indication of what the Return key does.
- [UIReturnKeyType](uireturnkeytype.md) — Constants that specify the type of Return key the keyboard displays.
- [textContentType](uitextinputtraits/textcontenttype.md) — The semantic meaning for a text input area.
- [UITextContentType](uitextcontenttype.md) — Constants that identify the semantic meaning for a text-entry area.
