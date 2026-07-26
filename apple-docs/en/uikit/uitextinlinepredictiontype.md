---
title: UITextInlinePredictionType
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinlinepredictiontype
source_url: 'https://developer.apple.com/documentation/uikit/uitextinlinepredictiontype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinlinepredictiontype.json'
content_hash: 'sha256:2b25296750fa0faa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextInlinePredictionType

<sub>Enumeration</sub>

Constants that identify the behavior of inline text predictions for a text-entry area.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UITextInlinePredictionType
```

## Overview

Use these constants with the [inlinePredictionType](uitextinputtraits/inlinepredictiontype.md) property.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UITextInlinePredictionTypeDefault](uitextinlinepredictiontype/default.md) — A constant that determines the behavior of inline text predictions according to the context.
- [UITextInlinePredictionTypeNo](uitextinlinepredictiontype/no.md) — A constant that turns off inline text predictions.
- [UITextInlinePredictionTypeYes](uitextinlinepredictiontype/yes.md) — A constant that turns on inline text predictions.

### Initializers

- [init(rawValue:)](<uitextinlinepredictiontype/init(rawvalue_).md>)

## See Also

### Managing spelling and autocorrection

- [autocapitalizationType](uitextinputtraits/autocapitalizationtype.md) — The autocapitalization style for the text object.
- [UITextAutocapitalizationType](uitextautocapitalizationtype.md) — The autocapitalization behavior of a text-based view.
- [autocorrectionType](uitextinputtraits/autocorrectiontype.md) — The autocorrection style for the text object.
- [UITextAutocorrectionType](uitextautocorrectiontype.md) — The autocorrection behavior of a text-based view.
- [spellCheckingType](uitextinputtraits/spellcheckingtype.md) — The spell-checking style for the text object.
- [UITextSpellCheckingType](uitextspellcheckingtype.md) — The spell-checking behavior of a text-based view.
- [inlinePredictionType](uitextinputtraits/inlinepredictiontype.md) — The behavior of inline text predictions for a text-entry area.
