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
doc_path: /documentation/foundation/parseableformatstyle/datetime
source_url: 'https://developer.apple.com/documentation/foundation/parseableformatstyle/datetime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/parseableformatstyle/datetime.json'
content_hash: 'sha256:4ac42a0d72919196'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ParseableFormatStyle](../parseableformatstyle.md)

# dateTime

<sub>Type Property</sub>

A style for formatting a date and time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var dateTime: Date.FormatStyle { get }
```

## Discussion

Use this type property when the call point allows the use of [FormatStyle](../date/formatstyle.md). You typically do this when calling the [formatted(_:)](<../date/formatted(__).md>) method of [Date](../date.md).

Customize the date format style using modifier syntax to apply specific date and time formats. For example:

```swift
let meetingDate = Date()
let localeArray = ["en_US", "sv_SE", "en_GB", "th_TH", "fr_BE"]
let formattedDates = localeArray.map { localeID in
    meetingDate.formatted(.dateTime
                          .day(.twoDigits)
                          .month(.wide)
                          .weekday(.short)
                          .hour(.conversationalTwoDigits(amPM: .wide))
                          .locale(Locale(identifier: localeID)))
        } // ["Mo, July 31 at 05 PM", "må 31 juli 17", "Mo, 31 July at 17", "จ. 31 กรกฎาคม เวลา 17", "lu 31 juillet à 17 h"]
```

The default format styles provided are [numeric](../date/formatstyle/datestyle/numeric.md) date format and [shortened](../date/formatstyle/timestyle/shortened.md) time format. For example:

```swift
let meetingDate = Date()
let formatted = meetingDate.formatted(.dateTime) // "7/31/2023, 5:15 PM"
```
