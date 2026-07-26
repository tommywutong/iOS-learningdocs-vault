---
title: 'abbreviation(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nstimezone/abbreviation(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/nstimezone/abbreviation(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstimezone/abbreviation%28for%3A%29.json'
content_hash: 'sha256:18a0f28b0264101a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTimeZone](../nstimezone.md)

# abbreviation(for:)

<sub>Instance Method</sub>

Returns the abbreviation for the receiver at a given date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func abbreviation(for aDate: Date) -> String?
```

## Parameters

- `aDate` — The date for which to get the abbreviation for the receiver.

## Return Value

The abbreviation for the receiver at `aDate`.

## Discussion

Note that the abbreviation may be different at different dates. For example, during daylight saving time the US/Eastern time zone has an abbreviation of “EDT.” At other times, its abbreviation is “EST.”

## See Also

### Getting Time Zone Information

- [name](name.md) — The geopolitical region ID that identifies the receiver.
- [abbreviation](abbreviation.md) — The abbreviation for the receiver, such as “EDT” (Eastern Daylight Time).
- [secondsFromGMT](secondsfromgmt.md) — The current difference in seconds between the receiver and Greenwich Mean Time.
- [- secondsFromGMTForDate:](<secondsfromgmt(for_).md>) — Returns the difference in seconds between the receiver and Greenwich Mean Time at a given date.
- [data](data.md) — The data that stores the information used by the receiver.
- [timeZoneDataVersion](timezonedataversion.md) — Returns the time zone data version.
- [NameStyle](namestyle.md) — Constants you use to specify a style when presenting time zone names.
