---
title: 'addressCheckingResult(range:components:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nstextcheckingresult/addresscheckingresult(range:components:)'
source_url: 'https://developer.apple.com/documentation/foundation/nstextcheckingresult/addresscheckingresult(range:components:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstextcheckingresult/addresscheckingresult%28range%3Acomponents%3A%29.json'
content_hash: 'sha256:4e11e5aa6cbfe574'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTextCheckingResult](../nstextcheckingresult.md)

# addressCheckingResult(range:components:)

<sub>Type Method</sub>

Creates and returns a text checking result with the specified address components.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func addressCheckingResult(range: NSRange, components: [NSTextCheckingKey : String]) -> NSTextCheckingResult
```

## Parameters

- `range` — The range of the detected result.

- `components` — A dictionary containing the address components. The dictionary keys are described in [Keys for Address Components](../keys-for-address-components.md).

## Return Value

Returns an `NSTextCheckingResult` with the specified [range](range.md) and a [resultType](resulttype.md) of [NSTextCheckingTypeAddress](checkingtype/address.md).

## See Also

### Text Checking Results for Addresses

- [addressComponents](addresscomponents.md) — The address dictionary of a type checking result.
