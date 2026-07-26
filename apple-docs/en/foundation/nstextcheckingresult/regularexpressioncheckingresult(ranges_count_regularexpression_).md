---
title: 'regularExpressionCheckingResult(ranges:count:regularExpression:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nstextcheckingresult/regularexpressioncheckingresult(ranges:count:regularexpression:)'
source_url: 'https://developer.apple.com/documentation/foundation/nstextcheckingresult/regularexpressioncheckingresult(ranges:count:regularexpression:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstextcheckingresult/regularexpressioncheckingresult%28ranges%3Acount%3Aregularexpression%3A%29.json'
content_hash: 'sha256:9854959590855d90'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTextCheckingResult](../nstextcheckingresult.md)

# regularExpressionCheckingResult(ranges:count:regularExpression:)

<sub>Type Method</sub>

Creates and returns a type checking result with the specified regular expression data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func regularExpressionCheckingResult(ranges: NSRangePointer, count: Int, regularExpression: NSRegularExpression) -> NSTextCheckingResult
```

## Parameters

- `ranges` — A C array of ranges, which must have at least one element, and the first element represents the overall range.

- `count` — The number of items in the `ranges` array.

- `regularExpression` — The regular expression.

## Return Value

Returns an `NSTextCheckingResult` with the specified [range](range.md) and a [resultType](resulttype.md) of [NSTextCheckingTypeRegularExpression](checkingtype/regularexpression.md).

## See Also

### Text Checking Results for Regular Expressions

- [regularExpression](regularexpression.md) — The regular expression of a type checking result.
