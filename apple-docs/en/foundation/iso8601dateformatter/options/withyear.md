---
title: withYear
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/iso8601dateformatter/options/withyear
source_url: 'https://developer.apple.com/documentation/foundation/iso8601dateformatter/options/withyear'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/iso8601dateformatter/options/withyear.json'
content_hash: 'sha256:10971b064d1bd2c3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [ISO8601DateFormatter](../../iso8601dateformatter.md) · [Options](../options.md)

# withYear

<sub>Type Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var withYear: ISO8601DateFormatter.Options { get }
```

## Discussion

The date representation includes the year. The format for year is inferred based on the other specified options.

- If [NSISO8601DateFormatWithWeekOfYear](withweekofyear.md) is specified, `YYYY` is used.
- Otherwise, `yyyy` is used.

## See Also

### Constants

- [NSISO8601DateFormatWithMonth](withmonth.md)
- [NSISO8601DateFormatWithWeekOfYear](withweekofyear.md)
- [NSISO8601DateFormatWithDay](withday.md)
- [NSISO8601DateFormatWithTime](withtime.md)
- [NSISO8601DateFormatWithTimeZone](withtimezone.md)
- [NSISO8601DateFormatWithSpaceBetweenDateAndTime](withspacebetweendateandtime.md)
- [NSISO8601DateFormatWithDashSeparatorInDate](withdashseparatorindate.md)
- [NSISO8601DateFormatWithColonSeparatorInTime](withcolonseparatorintime.md)
- [NSISO8601DateFormatWithColonSeparatorInTimeZone](withcolonseparatorintimezone.md)
- [NSISO8601DateFormatWithFullDate](withfulldate.md)
- [NSISO8601DateFormatWithFullTime](withfulltime.md)
- [NSISO8601DateFormatWithInternetDateTime](withinternetdatetime.md)
