---
title: UIPasteboardDetectionPatternFlightNumber
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboarddetectionpatternflightnumber
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboarddetectionpatternflightnumber'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboarddetectionpatternflightnumber.json'
content_hash: 'sha256:65ec4b3c354f010f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPasteboardDetectionPatternFlightNumber

<sub>Global Variable</sub>

A pattern that indicates the pasteboard detects a string that contains a flight number.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern UIPasteboardDetectionPattern const UIPasteboardDetectionPatternFlightNumber;
```

## Discussion

When you include this pattern in calls to [detectValuesForPatterns:inItemSet:completionHandler:](uipasteboard/detectvaluesforpatterns_initemset_completionhandler_.md) or [detectValuesForPatterns:completionHandler:](uipasteboard/detectvaluesforpatterns_completionhandler_.md) and the pasteboard detects a string that contains a flight number, the system reports the value as an array of [NSString](../foundation/nsstring.md). You can return the detected results in a paste operation with `UIPasteboardDetectionResultFlightNumber`, which contains a semantic representation of the flight number and airline carrier values.

## See Also

### Detecting common patterns

- [UIPasteboardDetectionPatternCalendarEvent](uipasteboarddetectionpatterncalendarevent.md) — A pattern that indicates the pasteboard detects a string that contains a calendar event.
- [UIPasteboardDetectionPatternEmailAddress](uipasteboarddetectionpatternemailaddress.md) — A pattern that indicates the pasteboard detects a string that contains an email address.
- [UIPasteboardDetectionPatternLink](uipasteboarddetectionpatternlink.md) — A pattern that indicates the pasteboard detects of a string that contains a URL.
- [UIPasteboardDetectionPatternMoneyAmount](uipasteboarddetectionpatternmoneyamount.md) — A pattern that indicates the pasteboard detects a string that contains an amount of money.
- [UIPasteboardDetectionPatternNumber](uipasteboard/detectionpattern/number.md) — A pattern that indicates the pasteboard contains a string that consists of a numeric value.
- [UIPasteboardDetectionPatternPhoneNumber](uipasteboarddetectionpatternphonenumber.md) — A pattern that indicates the pasteboard detects a string that contains a phone number.
- [UIPasteboardDetectionPatternPostalAddress](uipasteboarddetectionpatternpostaladdress.md) — A pattern that indicates the pasteboard detects a string that contains a postal address.
- [UIPasteboardDetectionPatternProbableWebSearch](uipasteboard/detectionpattern/probablewebsearch.md) — A pattern that indicates the pasteboard contains a string suitable for use as a web search term.
- [UIPasteboardDetectionPatternProbableWebURL](uipasteboard/detectionpattern/probableweburl.md) — A pattern that indicates the pasteboard contains a string that consists of a URL.
- [UIPasteboardDetectionPatternShipmentTrackingNumber](uipasteboarddetectionpatternshipmenttrackingnumber.md) — A pattern that indicates the pasteboard detects a string that contains a parcel tracking number and carrier.
