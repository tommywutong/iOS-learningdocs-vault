---
title: referenceDate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/datecomponentsformatter/referencedate
source_url: 'https://developer.apple.com/documentation/foundation/datecomponentsformatter/referencedate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponentsformatter/referencedate.json'
content_hash: 'sha256:e0ce01e3a879ce51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponentsFormatter](../datecomponentsformatter.md)

# referenceDate

<sub>Instance Property</sub>

Where units have variable length (number of days in a month, number of hours in a day, etc.), `NSDateComponentsFormatter` will calculate as though counting from the date specified by the `referenceDate` in the appropriate calendar. Defaults to `[NSDate dateWithTimeIntervalSinceReferenceDate:0]` at the time of the `-stringForObjectValue:` call if not set. Set to `nil` to get the default behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var referenceDate: Date? { get set }
```
