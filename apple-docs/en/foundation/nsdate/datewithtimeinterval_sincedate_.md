---
title: 'dateWithTimeInterval:sinceDate:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdate/datewithtimeinterval:sincedate:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdate/datewithtimeinterval:sincedate:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdate/datewithtimeinterval%3Asincedate%3A.json'
content_hash: 'sha256:e940b2325b4d7d94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDate](../nsdate.md)

# dateWithTimeInterval:sinceDate:

<sub>Type Method</sub>

Creates and returns a date object set to a given number of seconds from the specified date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) dateWithTimeInterval:(NSTimeInterval) secsToBeAdded sinceDate:(NSDate *) date;
```

## Parameters

- `secsToBeAdded` — The number of seconds to add to `date`. Use a negative argument to specify a date and time before `date`.

- `date` — The date.

## Return Value

An `NSDate` object set to `secsToBeAdded` seconds from `date`.
