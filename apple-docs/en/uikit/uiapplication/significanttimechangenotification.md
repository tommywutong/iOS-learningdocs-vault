---
title: significantTimeChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/significanttimechangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/significanttimechangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/significanttimechangenotification.json'
content_hash: 'sha256:756e17a5a7ee50b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# significantTimeChangeNotification

<sub>Type Property</sub>

A notification that posts when there’s a significant change in time.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated class let significantTimeChangeNotification: NSNotification.Name
```

## Discussion

The system posts this notification when, for example, there’s a change to a new day (midnight), a carrier time update, or a change to, or from, daylight savings time. The notification doesn’t contain a user info dictionary.

## See Also

### Responding to environment changes

- [- applicationProtectedDataDidBecomeAvailable:](<../uiapplicationdelegate/applicationprotecteddatadidbecomeavailable(__).md>) — Tells the delegate that protected files are available now.
- [- applicationProtectedDataWillBecomeUnavailable:](<../uiapplicationdelegate/applicationprotecteddatawillbecomeunavailable(__).md>) — Tells the delegate that the protected files are about to become unavailable.
- [- applicationDidReceiveMemoryWarning:](<../uiapplicationdelegate/applicationdidreceivememorywarning(__).md>) — Tells the delegate when the app receives a memory warning from the system.
- [- applicationSignificantTimeChange:](<../uiapplicationdelegate/applicationsignificanttimechange(__).md>) — Tells the delegate when there is a significant change in the time.
- [UIApplicationProtectedDataDidBecomeAvailable](protecteddatadidbecomeavailablenotification.md) — A notification that posts when the protected files become available for your code to access.
- [UIApplicationProtectedDataWillBecomeUnavailable](protecteddatawillbecomeunavailablenotification.md) — A notification that posts shortly before protected files are locked down and become inaccessible.
- [UIApplicationDidReceiveMemoryWarningNotification](didreceivememorywarningnotification.md) — A notification that posts when the app receives a warning from the operating system about low memory availability.
