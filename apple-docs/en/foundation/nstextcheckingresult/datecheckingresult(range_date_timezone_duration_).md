---
title: 'dateCheckingResult(range:date:timeZone:duration:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nstextcheckingresult/datecheckingresult(range:date:timezone:duration:)'
source_url: 'https://developer.apple.com/documentation/foundation/nstextcheckingresult/datecheckingresult(range:date:timezone:duration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstextcheckingresult/datecheckingresult%28range%3Adate%3Atimezone%3Aduration%3A%29.json'
content_hash: 'sha256:aa7bf8beb19d0549'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTextCheckingResult](../nstextcheckingresult.md)

# dateCheckingResult(range:date:timeZone:duration:)

<sub>Type Method</sub>

Creates and returns a text checking result with the specified date, time zone, and duration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func dateCheckingResult(range: NSRange, date: Date, timeZone: TimeZone, duration: TimeInterval) -> NSTextCheckingResult
```

## Parameters

- `range` — The range of the detected result.

- `date` — The detected date.

- `timeZone` — The detected time zone.

- `duration` — The detected duration.

## Return Value

Returns an `NSTextCheckingResult` with the specified [range](range.md) and a [resultType](resulttype.md) of [NSTextCheckingTypeDate](checkingtype/date.md).

## See Also

### Text Checking Results for Dates and Times

- [+ dateCheckingResultWithRange:date:](<datecheckingresult(range_date_).md>) — Creates and returns a text checking result with the specified date.
- [date](date.md) — The date component of a type checking result.
- [duration](duration.md) — The duration component of a type checking result.
- [timeZone](timezone.md) — The time zone component of a type checking result.
