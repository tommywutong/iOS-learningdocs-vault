---
title: 'grammarCheckingResult(range:details:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nstextcheckingresult/grammarcheckingresult(range:details:)'
source_url: 'https://developer.apple.com/documentation/foundation/nstextcheckingresult/grammarcheckingresult(range:details:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstextcheckingresult/grammarcheckingresult%28range%3Adetails%3A%29.json'
content_hash: 'sha256:d8a424ab20eb7a0b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTextCheckingResult](../nstextcheckingresult.md)

# grammarCheckingResult(range:details:)

<sub>Type Method</sub>

Creates and returns a text checking result with the specified array of grammatical errors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func grammarCheckingResult(range: NSRange, details: [[String : Any]]) -> NSTextCheckingResult
```

## Parameters

- `range` — The range of the detected result.

- `details` — An array of details regarding the grammatical errors. This array of strings is suitable for presenting to the user.

## Return Value

Returns an `NSTextCheckingResult` with the specified [range](range.md) and a [resultType](resulttype.md) of [NSTextCheckingTypeGrammar](checkingtype/grammar.md).

## See Also

### Text Checking Results for Grammar

- [grammarDetails](grammardetails.md) — The details of a located grammatical type checking result.
