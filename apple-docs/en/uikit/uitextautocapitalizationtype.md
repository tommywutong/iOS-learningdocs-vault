---
title: UITextAutocapitalizationType
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextautocapitalizationtype
source_url: 'https://developer.apple.com/documentation/uikit/uitextautocapitalizationtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextautocapitalizationtype.json'
content_hash: 'sha256:a97f4fff0713e21e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextAutocapitalizationType

<sub>Enumeration</sub>

The autocapitalization behavior of a text-based view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UITextAutocapitalizationType
```

## Overview

Use these constants with the [autocapitalizationType](uitextinputtraits/autocapitalizationtype.md) property. If the script system doesn’t support capitalization, the keyboard input method ignores these constants.

Some keyboard types don’t support autocapitalization. Specifically, if the [keyboardType](uitextinputtraits/keyboardtype.md) property is set to [UIKeyboardTypeNumberPad](uikeyboardtype/numberpad.md), [UIKeyboardTypePhonePad](uikeyboardtype/phonepad.md), or [UIKeyboardTypeNamePhonePad](uikeyboardtype/namephonepad.md), the system ignores these constants.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UITextAutocapitalizationTypeNone](uitextautocapitalizationtype/none.md) — Specifies that there is no automatic text capitalization.
- [UITextAutocapitalizationTypeWords](uitextautocapitalizationtype/words.md) — Specifies automatic capitalization of the first letter of each word.
- [UITextAutocapitalizationTypeSentences](uitextautocapitalizationtype/sentences.md) — Specifies automatic capitalization of the first letter of each sentence.
- [UITextAutocapitalizationTypeAllCharacters](uitextautocapitalizationtype/allcharacters.md) — Specifies automatic capitalization of all characters, such as for entry of two-character state abbreviations for the United States.

### Initializers

- [init(rawValue:)](<uitextautocapitalizationtype/init(rawvalue_).md>)

## See Also

### Managing spelling and autocorrection

- [autocapitalizationType](uitextinputtraits/autocapitalizationtype.md) — The autocapitalization style for the text object.
- [autocorrectionType](uitextinputtraits/autocorrectiontype.md) — The autocorrection style for the text object.
- [UITextAutocorrectionType](uitextautocorrectiontype.md) — The autocorrection behavior of a text-based view.
- [spellCheckingType](uitextinputtraits/spellcheckingtype.md) — The spell-checking style for the text object.
- [UITextSpellCheckingType](uitextspellcheckingtype.md) — The spell-checking behavior of a text-based view.
- [inlinePredictionType](uitextinputtraits/inlinepredictiontype.md) — The behavior of inline text predictions for a text-entry area.
- [UITextInlinePredictionType](uitextinlinepredictiontype.md) — Constants that identify the behavior of inline text predictions for a text-entry area.
