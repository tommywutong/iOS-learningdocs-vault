---
title: 'applicationSignificantTimeChange(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplicationdelegate/applicationsignificanttimechange(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationsignificanttimechange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/applicationsignificanttimechange%28_%3A%29.json'
content_hash: 'sha256:22da3e8b4b561a57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# applicationSignificantTimeChange(_:)

<sub>Instance Method</sub>

Tells the delegate when there is a significant change in the time.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func applicationSignificantTimeChange(_ application: UIApplication)
```

## Parameters

- `application` — Your singleton app object.

## Discussion

Examples of significant time changes include the arrival of midnight, an update of the time by a carrier, and the change to daylight savings time. The delegate can implement this method to adjust any object of the app that displays time or is sensitive to time changes.

Prior to calling this method, the app also posts a [UIApplicationSignificantTimeChangeNotification](../uiapplication/significanttimechangenotification.md) notification to give interested objects a chance to respond to the change.

If your app is currently suspended, this message is queued until your app returns to the foreground, at which point it is delivered. If multiple time changes occur, only the most recent one is delivered.

## See Also

### Responding to environment changes

- [- applicationProtectedDataDidBecomeAvailable:](<applicationprotecteddatadidbecomeavailable(__).md>) — Tells the delegate that protected files are available now.
- [- applicationProtectedDataWillBecomeUnavailable:](<applicationprotecteddatawillbecomeunavailable(__).md>) — Tells the delegate that the protected files are about to become unavailable.
- [- applicationDidReceiveMemoryWarning:](<applicationdidreceivememorywarning(__).md>) — Tells the delegate when the app receives a memory warning from the system.
- [UIApplicationProtectedDataDidBecomeAvailable](../uiapplication/protecteddatadidbecomeavailablenotification.md) — A notification that posts when the protected files become available for your code to access.
- [UIApplicationProtectedDataWillBecomeUnavailable](../uiapplication/protecteddatawillbecomeunavailablenotification.md) — A notification that posts shortly before protected files are locked down and become inaccessible.
- [UIApplicationDidReceiveMemoryWarningNotification](../uiapplication/didreceivememorywarningnotification.md) — A notification that posts when the app receives a warning from the operating system about low memory availability.
- [UIApplicationSignificantTimeChangeNotification](../uiapplication/significanttimechangenotification.md) — A notification that posts when there’s a significant change in time.
