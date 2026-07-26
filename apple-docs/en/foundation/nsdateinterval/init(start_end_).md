---
title: 'init(start:end:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdateinterval/init(start:end:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdateinterval/init(start:end:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdateinterval/init%28start%3Aend%3A%29.json'
content_hash: 'sha256:0cbb67d1f7a5ffae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDateInterval](../nsdateinterval.md)

# init(start:end:)

<sub>Initializer</sub>

Initializes a date interval from a given start date and end date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(start startDate: Date, end endDate: Date)
```

## Parameters

- `startDate` — The start date of the date interval.

- `endDate` — The end date of the date interval. > [!important] Important > This method raises an `NSArgumentException` if [endDate](enddate.md) occurs earlier than [startDate](startdate.md).

## See Also

### Creating Date Intervals

- [- init](<init().md>) — Initializes a date interval by setting the start and end date to the current date.
- [- initWithStartDate:duration:](<init(start_duration_).md>) — Initializes a date interval with a given start date and duration.
- [- initWithCoder:](<init(coder_).md>) — Returns a date interval initialized from data in the given unarchiver.
