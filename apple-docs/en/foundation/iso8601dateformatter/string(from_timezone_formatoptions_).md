---
title: 'string(from:timeZone:formatOptions:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/iso8601dateformatter/string(from:timezone:formatoptions:)'
source_url: 'https://developer.apple.com/documentation/foundation/iso8601dateformatter/string(from:timezone:formatoptions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/iso8601dateformatter/string%28from%3Atimezone%3Aformatoptions%3A%29.json'
content_hash: 'sha256:74d1b5c236f78752'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ISO8601DateFormatter](../iso8601dateformatter.md)

# string(from:timeZone:formatOptions:)

<sub>Type Method</sub>

Creates a representation of the specified date with a given time zone and format options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func string(from date: Date, timeZone: TimeZone, formatOptions: ISO8601DateFormatter.Options = []) -> String
```

## Parameters

- `date` — The date to be represented.

- `timeZone` — The time zone used.

- `formatOptions` — The options used. For possible values, see [Options](options.md).

## Return Value

A user-readable string representing the date.

## Discussion

This method uses a date formatter configured with the specified time zone and format options. The following code examples produce the same string value:

**Swift**

```swift
let date = Date()
var string: String
 
let formatter = ISO8601DateFormatter()
string = formatter.string(from: date)
 
if let GMT = TimeZone(abbreviation: "GMT") {
    let options: ISO8601DateFormatter.Options = [.withInternetDateTime, .withDashSeparatorInDate, .withColonSeparatorInTime, .withTimeZone]
    string = ISO8601DateFormatter.string(from: date, timeZone: GMT, formatOptions: options)
}
```

**Objective-C**

```objc
NSDate *date = [NSDate date];
NSString *string;
 
NSISO8601DateFormatter *formatter = [[NSISO8601DateFormatter alloc] init];
string = [formatter stringFromDate:date];
 
NSTimeZone *GMT = [NSTimeZone timeZoneWithAbbreviation: @"GMT"];
NSISO8601DateFormatOptions options = NSISO8601DateFormatWithInternetDateTime | NSISO8601DateFormatWithDashSeparatorInDate | NSISO8601DateFormatWithColonSeparatorInTime | NSISO8601DateFormatWithTimeZone;
string = [NSISO8601DateFormatter stringFromDate:date timeZone:GMT formatOptions:options];
```

## See Also

### Converting ISO 8601 Dates

- [- stringFromDate:](<string(from_).md>) — Creates and returns an ISO 8601 formatted string representation of the specified date.
- [- dateFromString:](<date(from_).md>) — Creates and returns a date object from the specified ISO 8601 formatted string representation.
