---
title: CFGregorianUnits
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+（8.0 起废弃）, iPadOS 2.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.4+（10.10 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corefoundation/cfgregorianunits
source_url: 'https://developer.apple.com/documentation/corefoundation/cfgregorianunits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfgregorianunits.json'
content_hash: 'sha256:fcc0af1b4ec65b1e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFGregorianUnits

<sub>Structure</sub>

Structure used to represent a time interval in Gregorian units.

> [!warning] Deprecated
> Use CFCalendar or NSCalendar API instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFGregorianUnits
```

## Overview

A CFGregorianUnits is used to represent arbitrary time _intervals_ (to represent a point in time using Gregorian units, use a [CFGregorianDate](cfgregoriandate.md)). Each field can take values up to the maximum possible for its data type. Negative values are also valid.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<cfgregorianunits/init().md>) _(deprecated)_
- [init(years:months:days:hours:minutes:seconds:)](<cfgregorianunits/init(years_months_days_hours_minutes_seconds_).md>) _(deprecated)_

### Instance Properties

- [days](cfgregorianunits/days.md) _(deprecated)_
- [hours](cfgregorianunits/hours.md) _(deprecated)_
- [minutes](cfgregorianunits/minutes.md) _(deprecated)_
- [months](cfgregorianunits/months.md) _(deprecated)_
- [seconds](cfgregorianunits/seconds.md) _(deprecated)_
- [years](cfgregorianunits/years.md) _(deprecated)_

## See Also

### Data Types

- [CFAbsoluteTime](cfabsolutetime.md) — Type used to represent a specific point in time relative to the absolute reference date of 1 Jan 2001 00:00:00 GMT.
- [CFGregorianDate](cfgregoriandate.md) — Structure used to represent a point in time using the Gregorian calendar. _(deprecated)_
- [CFTimeInterval](cftimeinterval.md) — Type used to represent elapsed time in seconds.
