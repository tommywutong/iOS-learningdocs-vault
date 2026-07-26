---
title: 'phoneNumberCheckingResult(range:phoneNumber:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nstextcheckingresult/phonenumbercheckingresult(range:phonenumber:)'
source_url: 'https://developer.apple.com/documentation/foundation/nstextcheckingresult/phonenumbercheckingresult(range:phonenumber:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstextcheckingresult/phonenumbercheckingresult%28range%3Aphonenumber%3A%29.json'
content_hash: 'sha256:981dcf0b922e96d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTextCheckingResult](../nstextcheckingresult.md)

# phoneNumberCheckingResult(range:phoneNumber:)

<sub>Type Method</sub>

Creates and returns a text checking result with the specified phone number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func phoneNumberCheckingResult(range: NSRange, phoneNumber: String) -> NSTextCheckingResult
```

## Parameters

- `range` — The range of the detected result.

- `phoneNumber` — The phone number.

## Return Value

Returns an `NSTextCheckingResult` with the specified [range](range.md) and a [resultType](resulttype.md) of [NSTextCheckingTypePhoneNumber](checkingtype/phonenumber.md).

## See Also

### Text Checking Results for Phone Numbers

- [phoneNumber](phonenumber.md) — The phone number of a type checking result.
