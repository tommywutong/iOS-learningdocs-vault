---
title: 'localizedString(from:dateStyle:timeStyle:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/dateformatter/localizedstring(from:datestyle:timestyle:)'
source_url: 'https://developer.apple.com/documentation/foundation/dateformatter/localizedstring(from:datestyle:timestyle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateformatter/localizedstring%28from%3Adatestyle%3Atimestyle%3A%29.json'
content_hash: 'sha256:8c1335fd067f836f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateFormatter](../dateformatter.md)

# localizedString(from:dateStyle:timeStyle:)

<sub>Type Method</sub>

Returns a string representation of a specified date, that the system formats for the current locale using the specified date and time styles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func localizedString(from date: Date, dateStyle dstyle: DateFormatter.Style, timeStyle tstyle: DateFormatter.Style) -> String
```

## Parameters

- `date` — A date.

- `dstyle` — A format style for the date. For possible values, see [Style](style.md).

- `tstyle` — A format style for the time. For possible values, see [Style](style.md).

## Return Value

A localized string representation of `date` using the specified date and time styles.

## Discussion

This method uses a date formatter configured with the current default settings. The returned string is the same as if you configured and used a date formatter as shown in the following example:

```objc
NSDateFormatter *formatter = [[NSDateFormatter alloc] init];
formatter.formatterBehavior = NSDateFormatterBehavior10_4;
formatter.dateStyle = dateStyle;
formatter.timeStyle = timeStyle;
NSString *result = [formatter stringForObjectValue:date];
```

## See Also

### Converting Objects

- [- dateFromString:](<date(from_).md>) — Returns a date representation of a specified string that the system interprets using the receiver’s current settings.
- [- stringFromDate:](<string(from_).md>) — Returns a string representation of a specified date that the system formats using the receiver’s current settings.
- [- getObjectValue:forString:range:error:](<getobjectvalue(__for_range_).md>) — Returns by reference a date representation of a specified string and its date range, as well as a Boolean value that indicates whether the system can parse the string.
