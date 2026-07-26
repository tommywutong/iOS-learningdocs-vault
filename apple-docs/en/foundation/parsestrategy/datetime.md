---
title: dateTime
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/parsestrategy/datetime
source_url: 'https://developer.apple.com/documentation/foundation/parsestrategy/datetime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/parsestrategy/datetime.json'
content_hash: 'sha256:6c25d2f8b750cc27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ParseStrategy](../parsestrategy.md)

# dateTime

<sub>Type Property</sub>

A default format style for formatting dates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var dateTime: Date.FormatStyle { get }
```

## Discussion

Use this type property when the call point allows the use of [FormatStyle](../date/formatstyle.md); in other words, when the value type is [Date](../date.md). Typically, you use this with the [formatted(_:)](<../date/formatted(__).md>) method of [Date](../date.md).

Customize the date format style using modifier syntax to apply specific date and time formats. For example:

```swift
let meetingDate = Date()
let localeArray = ["en_US", "sv_SE", "en_GB", "th_TH", "fr_BE"]
for localeID in localeArray {
    print(meetingDate.formatted(.dateTime
                                .day(.twoDigits)
                                .month(.wide)
                                .weekday(.short)
                                .hour(.conversationalTwoDigits(amPM: .wide))
                                .locale(Locale(identifier: localeID))))
}

// Tu, October 27, 5 PM
// ti 27 oktober 17
// Tu 27 October, 17
// อ. 27 ตุลาคม 17
// ma 27 octobre à 17 h
```

The default format styles provided are [numeric](../date/formatstyle/datestyle/numeric.md) date format and [shortened](../date/formatstyle/timestyle/shortened.md) time format. For example:

```swift
let meetingDate = Date()
meetingDate.formatted(.dateTime)) // 10/28/2020, 12:13 AM
```
