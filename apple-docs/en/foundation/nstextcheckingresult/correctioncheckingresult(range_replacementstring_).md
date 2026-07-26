---
title: 'correctionCheckingResult(range:replacementString:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nstextcheckingresult/correctioncheckingresult(range:replacementstring:)'
source_url: 'https://developer.apple.com/documentation/foundation/nstextcheckingresult/correctioncheckingresult(range:replacementstring:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstextcheckingresult/correctioncheckingresult%28range%3Areplacementstring%3A%29.json'
content_hash: 'sha256:e4b22a8e7fcb6fef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTextCheckingResult](../nstextcheckingresult.md)

# correctionCheckingResult(range:replacementString:)

<sub>Type Method</sub>

Creates and returns a text checking result after detecting a possible correction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func correctionCheckingResult(range: NSRange, replacementString: String) -> NSTextCheckingResult
```

## Parameters

- `range` — The range of the detected result.

- `replacementString` — The suggested replacement string.

## Return Value

Returns an `NSTextCheckingResult` with the specified [range](range.md) and a [resultType](resulttype.md) of [NSTextCheckingTypeSpelling](checkingtype/spelling.md).

## See Also

### Related Documentation

- [replacementString](replacementstring.md) — A replacement string from one of a number of replacement checking results.

### Text Checking Results for Spelling

- [+ spellCheckingResultWithRange:](<spellcheckingresult(range_).md>) — Creates and returns a text checking result with the range of a misspelled word.
