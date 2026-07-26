---
title: 'availableTagSchemes(for:language:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 4.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nslinguistictagger/availabletagschemes(for:language:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslinguistictagger/availabletagschemes(for:language:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslinguistictagger/availabletagschemes%28for%3Alanguage%3A%29.json'
content_hash: 'sha256:ad03fa361515dff9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLinguisticTagger](../nslinguistictagger.md)

# availableTagSchemes(for:language:)

<sub>Type Method</sub>

Returns the tag schemes available for a particular unit and language on the current device.

> [!warning] Deprecated
> All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func availableTagSchemes(for unit: NSLinguisticTaggerUnit, language: String) -> [NSLinguisticTagScheme]
```

## Parameters

- `unit` — The linguistic unit. For possible values, see [NSLinguisticTaggerUnit](../nslinguistictaggerunit.md).

- `language` — A BCP-47 tag identifying the language. For example, “en” for English or  “zh-Hans” for Chinese written using the Simplified Chinese script.

## Return Value

The supported tag schemes. For possible values, see [NSLinguisticTagScheme](../nslinguistictagscheme.md).

## See Also

### Getting the Tag Schemes

- [+ availableTagSchemesForLanguage:](<availabletagschemes(forlanguage_).md>) — Returns the tag schemes available for a particular language on the current device. _(deprecated)_
- [tagSchemes](tagschemes.md) — Returns the tag schemes configured for this linguistic tagger. For possible values, see [NSLinguisticTagScheme](../nslinguistictagscheme.md). _(deprecated)_
