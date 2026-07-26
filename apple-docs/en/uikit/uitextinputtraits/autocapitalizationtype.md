---
title: autocapitalizationType
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinputtraits/autocapitalizationtype
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputtraits/autocapitalizationtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputtraits/autocapitalizationtype.json'
content_hash: 'sha256:3c6728f97e72567d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputTraits](../uitextinputtraits.md)

# autocapitalizationType

<sub>Instance Property</sub>

The autocapitalization style for the text object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional var autocapitalizationType: UITextAutocapitalizationType { get set }
```

## Discussion

This property determines at what times the Shift key is automatically pressed, thereby making the typed character a capital letter. The default value for this property is [UITextAutocapitalizationTypeSentences](../uitextautocapitalizationtype/sentences.md).

Some keyboard types do not support autocapitalization. Specifically, this option is ignored if the value in the [keyboardType](keyboardtype.md) property is set to [UIKeyboardTypeNumberPad](../uikeyboardtype/numberpad.md), [UIKeyboardTypePhonePad](../uikeyboardtype/phonepad.md), or [UIKeyboardTypeNamePhonePad](../uikeyboardtype/namephonepad.md).

## See Also

### Managing spelling and autocorrection

- [UITextAutocapitalizationType](../uitextautocapitalizationtype.md) — The autocapitalization behavior of a text-based view.
- [autocorrectionType](autocorrectiontype.md) — The autocorrection style for the text object.
- [UITextAutocorrectionType](../uitextautocorrectiontype.md) — The autocorrection behavior of a text-based view.
- [spellCheckingType](spellcheckingtype.md) — The spell-checking style for the text object.
- [UITextSpellCheckingType](../uitextspellcheckingtype.md) — The spell-checking behavior of a text-based view.
- [inlinePredictionType](inlinepredictiontype.md) — The behavior of inline text predictions for a text-entry area.
- [UITextInlinePredictionType](../uitextinlinepredictiontype.md) — Constants that identify the behavior of inline text predictions for a text-entry area.
