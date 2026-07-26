---
title: 'init(start:duration:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdateinterval/init(start:duration:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdateinterval/init(start:duration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdateinterval/init%28start%3Aduration%3A%29.json'
content_hash: 'sha256:c7ab0694e27c8101'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDateInterval](../nsdateinterval.md)

# init(start:duration:)

<sub>Initializer</sub>

Initializes a date interval with a given start date and duration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(start startDate: Date, duration: TimeInterval)
```

## Parameters

- `startDate` — The start date of the date interval.

- `duration` — The duration from the start date for the date interval. > [!important] Important > This method raises an `NSArgumentException` if [duration](duration.md) is less than `0`.

## Discussion

This is the designated initializer.

## See Also

### Creating Date Intervals

- [- init](<init().md>) — Initializes a date interval by setting the start and end date to the current date.
- [- initWithStartDate:endDate:](<init(start_end_).md>) — Initializes a date interval from a given start date and end date.
- [- initWithCoder:](<init(coder_).md>) — Returns a date interval initialized from data in the given unarchiver.
