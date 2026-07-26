---
title: formatOptions
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/iso8601dateformatter/formatoptions
source_url: 'https://developer.apple.com/documentation/foundation/iso8601dateformatter/formatoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/iso8601dateformatter/formatoptions.json'
content_hash: 'sha256:0096c67fb0b779e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ISO8601DateFormatter](../iso8601dateformatter.md)

# formatOptions

<sub>Instance Property</sub>

Options for generating and parsing ISO 8601 date representations. See [Options](options.md) for possible values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var formatOptions: ISO8601DateFormatter.Options { get set }
```

## Discussion

The ISO 8601 specification allows for dates to be expressed in a variety of ways. You can configure the format used to parse and generate representations by specifying various combinations of format options.

| Format | Example | Options |
|---|---|---|
| Date with dash separators | `2016-06-13` | [NSISO8601DateFormatWithFullDate](options/withfulldate.md), [NSISO8601DateFormatWithDashSeparatorInDate](options/withdashseparatorindate.md) |
| [RFC 3339](https://www.ietf.org/rfc/rfc3339) Date and Time | `2016-06-13T16:00:00+00:00` | [NSISO8601DateFormatWithInternetDateTime](options/withinternetdatetime.md) |
| Date and Time with space separator between date and time | `20160613 160000` | [NSISO8601DateFormatWithFullDate](options/withfulldate.md), [NSISO8601DateFormatWithFullTime](options/withfulltime.md), [NSISO8601DateFormatWithSpaceBetweenDateAndTime](options/withspacebetweendateandtime.md) |
| Week of Year | `2016-W24` | [NSISO8601DateFormatWithYear](options/withyear.md), [NSISO8601DateFormatWithWeekOfYear](options/withweekofyear.md), [NSISO8601DateFormatWithDashSeparatorInDate](options/withdashseparatorindate.md) |
| Week of Year with Ordinal Weekday | `2016-W24-1` | [NSISO8601DateFormatWithYear](options/withyear.md), [NSISO8601DateFormatWithWeekOfYear](options/withweekofyear.md), [NSISO8601DateFormatWithDay](options/withday.md), [NSISO8601DateFormatWithDashSeparatorInDate](options/withdashseparatorindate.md) |
| Ordinal Day of Year | `2016-165` | [NSISO8601DateFormatWithYear](options/withyear.md), [NSISO8601DateFormatWithDay](options/withday.md), [NSISO8601DateFormatWithDashSeparatorInDate](options/withdashseparatorindate.md) |

> [!important] Important
> Resetting this property can incur a significant performance cost, as it may cause internal state to be regenerated.

## See Also

### Configuring the Formatter

- [timeZone](timezone.md) — The time zone used to create and parse date representations. When unspecified, GMT is used.
