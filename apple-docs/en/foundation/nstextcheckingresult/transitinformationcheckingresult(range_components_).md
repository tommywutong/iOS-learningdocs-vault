---
title: 'transitInformationCheckingResult(range:components:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nstextcheckingresult/transitinformationcheckingresult(range:components:)'
source_url: 'https://developer.apple.com/documentation/foundation/nstextcheckingresult/transitinformationcheckingresult(range:components:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstextcheckingresult/transitinformationcheckingresult%28range%3Acomponents%3A%29.json'
content_hash: 'sha256:7613064c370782a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTextCheckingResult](../nstextcheckingresult.md)

# transitInformationCheckingResult(range:components:)

<sub>Type Method</sub>

Creates and returns a text checking result with the specified transit information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func transitInformationCheckingResult(range: NSRange, components: [NSTextCheckingKey : String]) -> NSTextCheckingResult
```

## Parameters

- `range` — The range of the detected result.

- `components` — A dictionary containing the transit components. The currently supported keys are [NSTextCheckingAirlineKey](../nstextcheckingkey/airline.md) and [NSTextCheckingFlightKey](../nstextcheckingkey/flight.md).

## Return Value

Returns an `NSTextCheckingResult` with the specified [range](range.md) and a [resultType](resulttype.md) of [NSTextCheckingTypeTransitInformation](checkingtype/transitinformation.md).
