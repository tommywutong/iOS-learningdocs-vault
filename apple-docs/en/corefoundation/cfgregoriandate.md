---
title: CFGregorianDate
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+（8.0 起废弃）, iPadOS 2.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.4+（10.10 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corefoundation/cfgregoriandate
source_url: 'https://developer.apple.com/documentation/corefoundation/cfgregoriandate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfgregoriandate.json'
content_hash: 'sha256:e61f7477a8844f8d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFGregorianDate

<sub>Structure</sub>

Structure used to represent a point in time using the Gregorian calendar.

> [!warning] Deprecated
> Use CFCalendar or NSCalendar API instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFGregorianDate
```

## Overview

[CFGregorianDate](cfgregoriandate.md) is implemented using the smallest data type appropriate for the range of possible values. For example, there are only 12 months in the Gregorian year, so there is no need to use an integer type larger than 8 bits. To represent a time interval in Gregorian units, use a [CFGregorianUnits](cfgregorianunits.md).

The month and day units are 1-based: the index for January is 1, and the index for the first day of the month is 1.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<cfgregoriandate/init().md>) _(deprecated)_
- [init(year:month:day:hour:minute:second:)](<cfgregoriandate/init(year_month_day_hour_minute_second_).md>) _(deprecated)_

### Instance Properties

- [day](cfgregoriandate/day.md) _(deprecated)_
- [hour](cfgregoriandate/hour.md) _(deprecated)_
- [minute](cfgregoriandate/minute.md) _(deprecated)_
- [month](cfgregoriandate/month.md) _(deprecated)_
- [second](cfgregoriandate/second.md) _(deprecated)_
- [year](cfgregoriandate/year.md) _(deprecated)_

## See Also

### Data Types

- [CFAbsoluteTime](cfabsolutetime.md) — Type used to represent a specific point in time relative to the absolute reference date of 1 Jan 2001 00:00:00 GMT.
- [CFGregorianUnits](cfgregorianunits.md) — Structure used to represent a time interval in Gregorian units. _(deprecated)_
- [CFTimeInterval](cftimeinterval.md) — Type used to represent elapsed time in seconds.
