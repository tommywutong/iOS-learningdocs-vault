---
title: 'linkCheckingResult(range:url:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nstextcheckingresult/linkcheckingresult(range:url:)'
source_url: 'https://developer.apple.com/documentation/foundation/nstextcheckingresult/linkcheckingresult(range:url:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstextcheckingresult/linkcheckingresult%28range%3Aurl%3A%29.json'
content_hash: 'sha256:7ed3ff93044d2245'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTextCheckingResult](../nstextcheckingresult.md)

# linkCheckingResult(range:url:)

<sub>Type Method</sub>

Creates and returns a text checking result with the specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func linkCheckingResult(range: NSRange, url: URL) -> NSTextCheckingResult
```

## Parameters

- `range` — The range of the detected result.

- `url` — The URL.

## Return Value

Returns an `NSTextCheckingResult` with the specified [range](range.md) and a [resultType](resulttype.md) of [NSTextCheckingTypeLink](checkingtype/link.md).

## See Also

### Text Checking Results for URLs

- [URL](url.md) — The URL of a type checking result.
