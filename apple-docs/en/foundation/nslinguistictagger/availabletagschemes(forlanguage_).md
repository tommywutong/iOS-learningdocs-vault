---
title: 'availableTagSchemes(forLanguage:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nslinguistictagger/availabletagschemes(forlanguage:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslinguistictagger/availabletagschemes(forlanguage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslinguistictagger/availabletagschemes%28forlanguage%3A%29.json'
content_hash: 'sha256:d7d43bfbb4f6124b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLinguisticTagger](../nslinguistictagger.md)

# availableTagSchemes(forLanguage:)

<sub>Type Method</sub>

Returns the tag schemes available for a particular language on the current device.

> [!warning] Deprecated
> All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func availableTagSchemes(forLanguage language: String) -> [NSLinguisticTagScheme]
```

## Parameters

- `language` — A BCP-47 tag identifying the language. For example, “en” for English or  “zh-Hans” for Chinese written using the Simplified Chinese script.

## Return Value

The available tag schemes. For possible values, see [NSLinguisticTagScheme](../nslinguistictagscheme.md).

## Discussion

This is a convenience method for calling the [+ availableTagSchemesForUnit:language:](<availabletagschemes(for_language_).md>), passing [NSLinguisticTaggerUnitWord](../nslinguistictaggerunit/word.md) as the linguistic unit.

## See Also

### Getting the Tag Schemes

- [+ availableTagSchemesForUnit:language:](<availabletagschemes(for_language_).md>) — Returns the tag schemes available for a particular unit and language on the current device. _(deprecated)_
- [tagSchemes](tagschemes.md) — Returns the tag schemes configured for this linguistic tagger. For possible values, see [NSLinguisticTagScheme](../nslinguistictagscheme.md). _(deprecated)_
