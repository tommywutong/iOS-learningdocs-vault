---
title: 'sentenceRange(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nslinguistictagger/sentencerange(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslinguistictagger/sentencerange(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslinguistictagger/sentencerange%28for%3A%29.json'
content_hash: 'sha256:98012871a46c8586'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLinguisticTagger](../nslinguistictagger.md)

# sentenceRange(for:)

<sub>Instance Method</sub>

Returns the range of a sentence containing the specified range.

> [!warning] Deprecated
> All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sentenceRange(for range: NSRange) -> NSRange
```

## Parameters

- `range` — The character range.

## Return Value

Returns the range of the sentence.

## Discussion

This is a convenience method for calling [- tokenRangeAtIndex:unit:](<tokenrange(at_unit_).md>), passing the [NSLinguisticTaggerUnitSentence](../nslinguistictaggerunit/sentence.md) unit and the first position of the provided range.

## See Also

### Determining the Range of a Unit Token

- [- tokenRangeAtIndex:unit:](<tokenrange(at_unit_).md>) — Returns the range of the linguistic unit containing the specified character index. _(deprecated)_
