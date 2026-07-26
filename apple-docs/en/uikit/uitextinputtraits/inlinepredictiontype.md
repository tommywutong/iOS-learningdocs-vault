---
title: inlinePredictionType
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinputtraits/inlinepredictiontype
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputtraits/inlinepredictiontype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputtraits/inlinepredictiontype.json'
content_hash: 'sha256:aa2f89ba2adb0425'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputTraits](../uitextinputtraits.md)

# inlinePredictionType

<sub>Instance Property</sub>

The behavior of inline text predictions for a text-entry area.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional var inlinePredictionType: UITextInlinePredictionType { get set }
```

## Discussion

This property controls whether system-provided text suggestions appear inline during typing. The default value is [UITextInlinePredictionTypeDefault](../uitextinlinepredictiontype/default.md).

If you use a [UITextView](../uitextview.md) or [UITextField](../uitextfield.md), set this property if you want to change the inline text prediction behavior. For example, you might want to turn off inline text predictions if your app provides its own text suggestions.

The following code turns off inline text predictions in a text view:

```swift
let textView = UITextView(frame: frame)
textView.inlinePredictionType = .no
```

## See Also

### Managing spelling and autocorrection

- [autocapitalizationType](autocapitalizationtype.md) — The autocapitalization style for the text object.
- [UITextAutocapitalizationType](../uitextautocapitalizationtype.md) — The autocapitalization behavior of a text-based view.
- [autocorrectionType](autocorrectiontype.md) — The autocorrection style for the text object.
- [UITextAutocorrectionType](../uitextautocorrectiontype.md) — The autocorrection behavior of a text-based view.
- [spellCheckingType](spellcheckingtype.md) — The spell-checking style for the text object.
- [UITextSpellCheckingType](../uitextspellcheckingtype.md) — The spell-checking behavior of a text-based view.
- [UITextInlinePredictionType](../uitextinlinepredictiontype.md) — Constants that identify the behavior of inline text predictions for a text-entry area.
