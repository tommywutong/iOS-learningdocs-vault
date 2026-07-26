---
title: 'possibleTags(at:scheme:tokenRange:sentenceRange:scores:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nslinguistictagger/possibletags(at:scheme:tokenrange:sentencerange:scores:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslinguistictagger/possibletags(at:scheme:tokenrange:sentencerange:scores:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslinguistictagger/possibletags%28at%3Ascheme%3Atokenrange%3Asentencerange%3Ascores%3A%29.json'
content_hash: 'sha256:2aaa938de9a1b6fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLinguisticTagger](../nslinguistictagger.md)

# possibleTags(at:scheme:tokenRange:sentenceRange:scores:)

<sub>Instance Method</sub>

Returns an array of possible tags for the given scheme at the specified range, supplying matching scores.

> [!warning] Deprecated
> All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func possibleTags(at charIndex: Int, scheme tagScheme: String, tokenRange: NSRangePointer?, sentenceRange: NSRangePointer?, scores: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [String]?
```

## Parameters

- `charIndex` — The position of the initial character.

- `tagScheme` — The tag scheme. See [NSLinguisticTagScheme](../nslinguistictagscheme.md) for possible values.

- `tokenRange` — The token range.

- `sentenceRange` — The range of the sentence.

- `scores` — Returns by reference an array of numeric scores indicating the likelihood that the range matches the tag scheme.

## Return Value

Returns an array of possible tags for the tag scheme at the specified location, starting with the most likely tag scheme.  For some tag schemes only a single tag will be returned, but for others a list of possibilities will be provided.

## Discussion

Calling this method is not recommended; for most use cases, this information is not as useful as what is provided by the methods described in Enumerating Linguistic Tags and Getting Linguistic Tags.
