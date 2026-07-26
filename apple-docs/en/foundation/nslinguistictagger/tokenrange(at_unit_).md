---
title: 'tokenRange(at:unit:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 4.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nslinguistictagger/tokenrange(at:unit:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslinguistictagger/tokenrange(at:unit:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslinguistictagger/tokenrange%28at%3Aunit%3A%29.json'
content_hash: 'sha256:791b4b21085c6aff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLinguisticTagger](../nslinguistictagger.md)

# tokenRange(at:unit:)

<sub>Instance Method</sub>

Returns the range of the linguistic unit containing the specified character index.

> [!warning] Deprecated
> All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tokenRange(at charIndex: Int, unit: NSLinguisticTaggerUnit) -> NSRange
```

## Parameters

- `charIndex` — The character index to begin examination.

- `unit` — The linguistic unit. For possible values, see [NSLinguisticTaggerUnit](../nslinguistictaggerunit.md).

## Return Value

The range of the substring for the linguistic unit.

## See Also

### Determining the Range of a Unit Token

- [- sentenceRangeForRange:](<sentencerange(for_).md>) — Returns the range of a sentence containing the specified range. _(deprecated)_
