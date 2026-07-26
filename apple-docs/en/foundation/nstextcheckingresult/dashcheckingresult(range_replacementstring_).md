---
title: 'dashCheckingResult(range:replacementString:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nstextcheckingresult/dashcheckingresult(range:replacementstring:)'
source_url: 'https://developer.apple.com/documentation/foundation/nstextcheckingresult/dashcheckingresult(range:replacementstring:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstextcheckingresult/dashcheckingresult%28range%3Areplacementstring%3A%29.json'
content_hash: 'sha256:2f91f3a5c1b428a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTextCheckingResult](../nstextcheckingresult.md)

# dashCheckingResult(range:replacementString:)

<sub>Type Method</sub>

Creates and returns a text checking result with the specified dash corrected replacement string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func dashCheckingResult(range: NSRange, replacementString: String) -> NSTextCheckingResult
```

## Parameters

- `range` — The range of the detected result.

- `replacementString` — The replacement string.

## Return Value

Returns an `NSTextCheckingResult` with the specified [range](range.md) and a [resultType](resulttype.md) of [NSTextCheckingTypeDash](checkingtype/dash.md).

## See Also

### Text Checking Results for Typography

- [+ quoteCheckingResultWithRange:replacementString:](<quotecheckingresult(range_replacementstring_).md>) — Creates and returns a text checking result with the specified quote-balanced replacement string.
