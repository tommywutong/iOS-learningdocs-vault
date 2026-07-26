---
title: 'secondsFromGMT(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nstimezone/secondsfromgmt(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/nstimezone/secondsfromgmt(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstimezone/secondsfromgmt%28for%3A%29.json'
content_hash: 'sha256:a1affa8e49d63c87'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTimeZone](../nstimezone.md)

# secondsFromGMT(for:)

<sub>Instance Method</sub>

Returns the difference in seconds between the receiver and Greenwich Mean Time at a given date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func secondsFromGMT(for aDate: Date) -> Int
```

## Parameters

- `aDate` — The date against which to test the receiver.

## Return Value

The difference in seconds between the receiver and Greenwich Mean Time at `aDate`.

## Discussion

The difference may be different from the current difference if the time zone changes its offset from GMT at different points in the year—for example, the U.S. time zones change with daylight saving time.

## See Also

### Getting Time Zone Information

- [name](name.md) — The geopolitical region ID that identifies the receiver.
- [abbreviation](abbreviation.md) — The abbreviation for the receiver, such as “EDT” (Eastern Daylight Time).
- [- abbreviationForDate:](<abbreviation(for_).md>) — Returns the abbreviation for the receiver at a given date.
- [secondsFromGMT](secondsfromgmt.md) — The current difference in seconds between the receiver and Greenwich Mean Time.
- [data](data.md) — The data that stores the information used by the receiver.
- [timeZoneDataVersion](timezonedataversion.md) — Returns the time zone data version.
- [NameStyle](namestyle.md) — Constants you use to specify a style when presenting time zone names.
