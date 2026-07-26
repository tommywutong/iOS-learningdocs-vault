---
title: autocorrectionType
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinputtraits/autocorrectiontype
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputtraits/autocorrectiontype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputtraits/autocorrectiontype.json'
content_hash: 'sha256:50c35c650ac1bcbc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputTraits](../uitextinputtraits.md)

# autocorrectionType

<sub>Instance Property</sub>

The autocorrection style for the text object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional var autocorrectionType: UITextAutocorrectionType { get set }
```

## Discussion

This property determines whether autocorrection is enabled or disabled during typing. With autocorrection enabled, the text object tracks unknown words and suggests a more suitable replacement candidate to the user, replacing the typed text automatically unless the user explicitly overrides the action.

The default value for this property is [UITextAutocorrectionTypeDefault](../uitextautocorrectiontype/default.md), which for most input methods results in autocorrection being enabled.

## See Also

### Managing spelling and autocorrection

- [autocapitalizationType](autocapitalizationtype.md) — The autocapitalization style for the text object.
- [UITextAutocapitalizationType](../uitextautocapitalizationtype.md) — The autocapitalization behavior of a text-based view.
- [UITextAutocorrectionType](../uitextautocorrectiontype.md) — The autocorrection behavior of a text-based view.
- [spellCheckingType](spellcheckingtype.md) — The spell-checking style for the text object.
- [UITextSpellCheckingType](../uitextspellcheckingtype.md) — The spell-checking behavior of a text-based view.
- [inlinePredictionType](inlinepredictiontype.md) — The behavior of inline text predictions for a text-entry area.
- [UITextInlinePredictionType](../uitextinlinepredictiontype.md) — Constants that identify the behavior of inline text predictions for a text-entry area.
