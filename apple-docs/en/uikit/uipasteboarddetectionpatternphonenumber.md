---
title: UIPasteboardDetectionPatternPhoneNumber
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboarddetectionpatternphonenumber
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboarddetectionpatternphonenumber'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboarddetectionpatternphonenumber.json'
content_hash: 'sha256:2969e47ece60b08c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPasteboardDetectionPatternPhoneNumber

<sub>Global Variable</sub>

A pattern that indicates the pasteboard detects a string that contains a phone number.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern UIPasteboardDetectionPattern const UIPasteboardDetectionPatternPhoneNumber;
```

## Discussion

When you include this pattern in calls to [detectValuesForPatterns:inItemSet:completionHandler:](uipasteboard/detectvaluesforpatterns_initemset_completionhandler_.md) or [detectValuesForPatterns:completionHandler:](uipasteboard/detectvaluesforpatterns_completionhandler_.md) and the pasteboard detects a string that contains a phone number, the system reports the value as an array of [NSString](../foundation/nsstring.md). You can return the detected results in a paste operation with `UIPasteboardDetectionResultPhoneNumber`, which contains a semantic representation of the phone number and label values.

## See Also

### Detecting common patterns

- [UIPasteboardDetectionPatternCalendarEvent](uipasteboarddetectionpatterncalendarevent.md) — A pattern that indicates the pasteboard detects a string that contains a calendar event.
- [UIPasteboardDetectionPatternEmailAddress](uipasteboarddetectionpatternemailaddress.md) — A pattern that indicates the pasteboard detects a string that contains an email address.
- [UIPasteboardDetectionPatternFlightNumber](uipasteboarddetectionpatternflightnumber.md) — A pattern that indicates the pasteboard detects a string that contains a flight number.
- [UIPasteboardDetectionPatternLink](uipasteboarddetectionpatternlink.md) — A pattern that indicates the pasteboard detects of a string that contains a URL.
- [UIPasteboardDetectionPatternMoneyAmount](uipasteboarddetectionpatternmoneyamount.md) — A pattern that indicates the pasteboard detects a string that contains an amount of money.
- [UIPasteboardDetectionPatternNumber](uipasteboard/detectionpattern/number.md) — A pattern that indicates the pasteboard contains a string that consists of a numeric value.
- [UIPasteboardDetectionPatternPostalAddress](uipasteboarddetectionpatternpostaladdress.md) — A pattern that indicates the pasteboard detects a string that contains a postal address.
- [UIPasteboardDetectionPatternProbableWebSearch](uipasteboard/detectionpattern/probablewebsearch.md) — A pattern that indicates the pasteboard contains a string suitable for use as a web search term.
- [UIPasteboardDetectionPatternProbableWebURL](uipasteboard/detectionpattern/probableweburl.md) — A pattern that indicates the pasteboard contains a string that consists of a URL.
- [UIPasteboardDetectionPatternShipmentTrackingNumber](uipasteboarddetectionpatternshipmenttrackingnumber.md) — A pattern that indicates the pasteboard detects a string that contains a parcel tracking number and carrier.
