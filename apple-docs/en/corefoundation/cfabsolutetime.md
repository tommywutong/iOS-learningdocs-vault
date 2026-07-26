---
title: CFAbsoluteTime
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfabsolutetime
source_url: 'https://developer.apple.com/documentation/corefoundation/cfabsolutetime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfabsolutetime.json'
content_hash: 'sha256:2ed151f296051523'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAbsoluteTime

<sub>Type Alias</sub>

Type used to represent a specific point in time relative to the absolute reference date of 1 Jan 2001 00:00:00 GMT.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFAbsoluteTime = CFTimeInterval
```

## Discussion

Absolute time is measured by the number of seconds between the reference date and the specified date. Negative values indicate dates/times before the reference date. Positive values indicate dates/times after the reference date.

## See Also

### Data Types

- [CFGregorianDate](cfgregoriandate.md) — Structure used to represent a point in time using the Gregorian calendar. _(deprecated)_
- [CFGregorianUnits](cfgregorianunits.md) — Structure used to represent a time interval in Gregorian units. _(deprecated)_
- [CFTimeInterval](cftimeinterval.md) — Type used to represent elapsed time in seconds.
