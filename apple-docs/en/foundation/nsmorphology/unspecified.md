---
title: unspecified
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmorphology/unspecified
source_url: 'https://developer.apple.com/documentation/foundation/nsmorphology/unspecified'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmorphology/unspecified.json'
content_hash: 'sha256:4081bb589d18b542'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMorphology](../nsmorphology.md)

# unspecified

<sub>Instance Property</sub>

A Boolean value that indicates whether this instance specifies no particular grammar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (readonly, getter=isUnspecified) BOOL unspecified;
```

## Discussion

This value is equivalent to having set none of the properties in this [NSMorphology](../nsmorphology.md). This occurs when the user hasn’t specified preferences, or chose not to share them with this app. When the morphology is unspecified, inflecting a string with this morphology does nothing.

## See Also

### Accessing Grammatical Properties

- [grammaticalGender](grammaticalgender.md) — The grammatical gender used for inflecting strings with this morphology.
- [NSGrammaticalGender](../nsgrammaticalgender.md) — A representation of grammatical gender, used for inflecting strings.
- [number](number.md) — The grammatical number used for inflecting strings with this morphology.
- [NSGrammaticalNumber](../nsgrammaticalnumber.md) — A representation of grammatical number, used for inflecting strings.
- [partOfSpeech](partofspeech.md) — The grammatical part of speech used for inflecting strings with this morphology.
- [NSGrammaticalPartOfSpeech](../nsgrammaticalpartofspeech.md) — A representation of grammatical parts of speech, used for inflecting strings.
