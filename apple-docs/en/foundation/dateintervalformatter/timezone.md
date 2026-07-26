---
title: timeZone
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/dateintervalformatter/timezone
source_url: 'https://developer.apple.com/documentation/foundation/dateintervalformatter/timezone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateintervalformatter/timezone.json'
content_hash: 'sha256:b4e186c40dbd5908'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateIntervalFormatter](../dateintervalformatter.md)

# timeZone

<sub>Instance Property</sub>

The time zone with which to specify time values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var timeZone: TimeZone! { get set }
```

## Discussion

The default value of this property is the default time zone for the current user, which is accessible from the [defaultTimeZone](../nstimezone/default.md) method of [NSTimeZone](../nstimezone.md). You can change this value to a different time zone to generate strings based on that time zone.

## See Also

### Configuring the Formatter Options

- [dateStyle](datestyle.md) — The style to use when formatting day, month, and year information.
- [timeStyle](timestyle.md) — The style to use when formatting hour, minute, and second information.
- [dateTemplate](datetemplate.md) — The template for formatting one date and time value.
- [calendar](calendar.md) — The calendar to use for date values.
- [locale](locale.md) — The locale to use when formatting date and time values.
