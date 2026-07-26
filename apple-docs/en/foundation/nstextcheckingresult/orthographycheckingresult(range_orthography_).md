---
title: 'orthographyCheckingResult(range:orthography:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nstextcheckingresult/orthographycheckingresult(range:orthography:)'
source_url: 'https://developer.apple.com/documentation/foundation/nstextcheckingresult/orthographycheckingresult(range:orthography:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstextcheckingresult/orthographycheckingresult%28range%3Aorthography%3A%29.json'
content_hash: 'sha256:194f8148938b9152'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTextCheckingResult](../nstextcheckingresult.md)

# orthographyCheckingResult(range:orthography:)

<sub>Type Method</sub>

Creates and returns a text checking result with the specified orthography.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func orthographyCheckingResult(range: NSRange, orthography: NSOrthography) -> NSTextCheckingResult
```

## Parameters

- `range` — The range of the detected result.

- `orthography` — An orthography object that describes the script.

## Return Value

Returns an `NSTextCheckingResult` with the specified [range](range.md) and a [resultType](resulttype.md) of [NSTextCheckingTypeOrthography](checkingtype/orthography.md).

## See Also

### Text Checking Results for Orthography

- [orthography](orthography.md) — The detected orthography of a type checking result.
