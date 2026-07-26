---
title: UIPasteboard.DetectedValues
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboard/detectedvalues
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/detectedvalues'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/detectedvalues.json'
content_hash: 'sha256:70c0ce3422417068'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# UIPasteboard.DetectedValues

<sub>Structure</sub>

An object that contains common types of data that the data detection system matches for a pasteboard.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct DetectedValues
```

## Topics

### Detected patterns

- [patterns](detectedvalues/patterns.md) — A set of key paths that represent patterns that the data detection system identifies.
- [probableWebSearch](detectedvalues/probablewebsearch.md) — A string that the data detection system identifies as a probable web search item.
- [probableWebURL](detectedvalues/probableweburl.md) — A string that the data detection system identifies as a probable web URL.

### Detected values

- [calendarEvents](detectedvalues/calendarevents.md) — An array of calendar events that the data detection system identifies.
- [emailAddresses](detectedvalues/emailaddresses.md) — An array of email addresses that the data detection system identifies.
- [flightNumbers](detectedvalues/flightnumbers.md) — An array of flight numbers that the system data detection system identifies.
- [links](detectedvalues/links.md) — An array of web links that the data detection system identifies.
- [moneyAmounts](detectedvalues/moneyamounts.md) — An array of money amounts and currencies that the data detection system identifies.
- [number](detectedvalues/number.md) — A number that the data detection system identifies.
- [phoneNumbers](detectedvalues/phonenumbers.md) — An array of phone numbers that the data detection system identifies.
- [postalAddresses](detectedvalues/postaladdresses.md) — An array of postal addresses that the data detection system identifies.
- [shipmentTrackingNumbers](detectedvalues/shipmenttrackingnumbers.md) — An array of parcel tracking numbers that the data detection system identifies.

## See Also

### Detecting patterns of content in pasteboard items

- [detectPatterns(for:completionHandler:)](<detectpatterns(for_completionhandler_)-23vwn.md>) — Requests that the data detection system identify the patterns that you specify for the pasteboard, and provide the patterns that it matches to your closure.
- [detectedPatterns(for:)](<detectedpatterns(for_).md>) — Requests that the data detection system asynchronously identify the patterns that you specify for the pasteboard, and return the patterns that it matches.
- [detectPatterns(for:inItemSet:completionHandler:)](<detectpatterns(for_initemset_completionhandler_)-7ubl1.md>) — Requests that the data detection system identify the patterns that you specify for the pasteboard items, and provide the patterns that it matches to your closure.
- [detectedPatterns(for:inItemSet:)](<detectedpatterns(for_initemset_).md>) — Requests that the data detection system asynchronously identify the patterns that you specify for the pasteboard items, and return the patterns that it matches.
- [detectValues(for:completionHandler:)](<detectvalues(for_completionhandler_)-6adre.md>) — Requests that the data detection system identify the types of data that you specify for the pasteboard, and provide the values that it matches to your closure.
- [detectedValues(for:)](<detectedvalues(for_).md>) — Requests that the data detection system asynchronously identify the types of values that you specify for the pasteboard, and return the values that it matches.
- [detectValues(for:inItemSet:completionHandler:)](<detectvalues(for_initemset_completionhandler_)-pm9l.md>) — Requests that the data detection system identify the types of data that you specify for the pasteboard items, and provide the values that it matches to your closure.
- [detectedValues(for:inItemSet:)](<detectedvalues(for_initemset_).md>) — Requests that the data detection system asynchronously identify the types of values that you specify for the pasteboard item, and return the values that it matches for each pasteboard.
- [DetectionPattern](detectionpattern.md) — An object that represents a pattern to detect for the pasteboard, such as a URL, text, or a number.
