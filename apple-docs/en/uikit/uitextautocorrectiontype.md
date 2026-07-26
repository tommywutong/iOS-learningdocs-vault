---
title: UITextAutocorrectionType
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextautocorrectiontype
source_url: 'https://developer.apple.com/documentation/uikit/uitextautocorrectiontype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextautocorrectiontype.json'
content_hash: 'sha256:c45211aad75c3ff9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextAutocorrectionType

<sub>Enumeration</sub>

The autocorrection behavior of a text-based view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UITextAutocorrectionType
```

## Overview

Use these constants with the [autocorrectionType](uitextinputtraits/autocorrectiontype.md) property. If the script system doesn’t support inline autocorrection, the keyboard input method ignores these constants.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UITextAutocorrectionTypeDefault](uitextautocorrectiontype/default.md) — Specifies an appropriate autocorrection behavior for the current script system.
- [UITextAutocorrectionTypeNo](uitextautocorrectiontype/no.md) — Disables autocorrection behavior.
- [UITextAutocorrectionTypeYes](uitextautocorrectiontype/yes.md) — Enables autocorrection behavior.

### Initializers

- [init(rawValue:)](<uitextautocorrectiontype/init(rawvalue_).md>)

## See Also

### Managing spelling and autocorrection

- [autocapitalizationType](uitextinputtraits/autocapitalizationtype.md) — The autocapitalization style for the text object.
- [UITextAutocapitalizationType](uitextautocapitalizationtype.md) — The autocapitalization behavior of a text-based view.
- [autocorrectionType](uitextinputtraits/autocorrectiontype.md) — The autocorrection style for the text object.
- [spellCheckingType](uitextinputtraits/spellcheckingtype.md) — The spell-checking style for the text object.
- [UITextSpellCheckingType](uitextspellcheckingtype.md) — The spell-checking behavior of a text-based view.
- [inlinePredictionType](uitextinputtraits/inlinepredictiontype.md) — The behavior of inline text predictions for a text-entry area.
- [UITextInlinePredictionType](uitextinlinepredictiontype.md) — Constants that identify the behavior of inline text predictions for a text-entry area.
