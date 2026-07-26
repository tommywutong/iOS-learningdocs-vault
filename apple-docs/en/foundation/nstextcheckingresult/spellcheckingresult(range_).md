---
title: 'spellCheckingResult(range:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nstextcheckingresult/spellcheckingresult(range:)'
source_url: 'https://developer.apple.com/documentation/foundation/nstextcheckingresult/spellcheckingresult(range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstextcheckingresult/spellcheckingresult%28range%3A%29.json'
content_hash: 'sha256:8f789ed4a3d6bdaa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTextCheckingResult](../nstextcheckingresult.md)

# spellCheckingResult(range:)

<sub>Type Method</sub>

Creates and returns a text checking result with the range of a misspelled word.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func spellCheckingResult(range: NSRange) -> NSTextCheckingResult
```

## Parameters

- `range` — The range of the detected result.

## Return Value

Returns an `NSTextCheckingResult` with the specified [range](range.md) and a [resultType](resulttype.md) of [NSTextCheckingTypeSpelling](checkingtype/spelling.md).

## See Also

### Text Checking Results for Spelling

- [+ correctionCheckingResultWithRange:replacementString:](<correctioncheckingresult(range_replacementstring_).md>) — Creates and returns a text checking result after detecting a possible correction.
