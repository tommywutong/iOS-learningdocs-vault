---
title: isUnspecified
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/morphology/isunspecified
source_url: 'https://developer.apple.com/documentation/foundation/morphology/isunspecified'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/morphology/isunspecified.json'
content_hash: 'sha256:27143bcebf752c68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Morphology](../morphology.md)

# isUnspecified

<sub>Instance Property</sub>

A Boolean value that indicates whether this instance specifies no particular grammar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isUnspecified: Bool { get }
```

## Discussion

This value is equivalent to having set none of the properties in this [Morphology](../morphology.md). This occurs when the user hasn’t specified preferences, or chose not to share them with this app. When the morphology is unspecified, inflecting a string with this morphology does nothing.

## See Also

### Accessing Grammatical Properties

- [grammaticalGender](grammaticalgender-swift.property.md) — The grammatical gender used for inflecting strings with this morphology.
- [GrammaticalGender](grammaticalgender-swift.enum.md) — A representation of grammatical gender, used for inflecting strings.
- [number](number.md) — The grammatical number used for inflecting strings with this morphology.
- [GrammaticalNumber](grammaticalnumber.md) — A representation of grammatical number, used for inflecting strings.
- [partOfSpeech](partofspeech-swift.property.md) — The grammatical part of speech used for inflecting strings with this morphology.
- [PartOfSpeech](partofspeech-swift.enum.md) — A representation of grammatical parts of speech, used for inflecting strings.
