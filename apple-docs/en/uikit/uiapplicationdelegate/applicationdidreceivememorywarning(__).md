---
title: 'applicationDidReceiveMemoryWarning(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplicationdelegate/applicationdidreceivememorywarning(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationdidreceivememorywarning(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/applicationdidreceivememorywarning%28_%3A%29.json'
content_hash: 'sha256:8c4d6ff0198fa124'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# applicationDidReceiveMemoryWarning(_:)

<sub>Instance Method</sub>

Tells the delegate when the app receives a memory warning from the system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func applicationDidReceiveMemoryWarning(_ application: UIApplication)
```

## Parameters

- `application` — Your singleton app object.

## Discussion

Your implementation of this method should free up as much memory as possible by purging cached data objects that can be recreated (or reloaded from disk) later. You use this method in conjunction with the [- didReceiveMemoryWarning](<../uiviewcontroller/didreceivememorywarning().md>) of the [UIViewController](../uiviewcontroller.md) class and the [UIApplicationDidReceiveMemoryWarningNotification](../uiapplication/didreceivememorywarningnotification.md) notification to release memory throughout your app.

It is strongly recommended that you implement this method. If your app does not release enough memory during low-memory conditions, the system may terminate it outright.

## See Also

### Related Documentation

- [- didReceiveMemoryWarning](<../uiviewcontroller/didreceivememorywarning().md>) — Sent to the view controller when the app receives a memory warning.

### Responding to environment changes

- [- applicationProtectedDataDidBecomeAvailable:](<applicationprotecteddatadidbecomeavailable(__).md>) — Tells the delegate that protected files are available now.
- [- applicationProtectedDataWillBecomeUnavailable:](<applicationprotecteddatawillbecomeunavailable(__).md>) — Tells the delegate that the protected files are about to become unavailable.
- [- applicationSignificantTimeChange:](<applicationsignificanttimechange(__).md>) — Tells the delegate when there is a significant change in the time.
- [UIApplicationProtectedDataDidBecomeAvailable](../uiapplication/protecteddatadidbecomeavailablenotification.md) — A notification that posts when the protected files become available for your code to access.
- [UIApplicationProtectedDataWillBecomeUnavailable](../uiapplication/protecteddatawillbecomeunavailablenotification.md) — A notification that posts shortly before protected files are locked down and become inaccessible.
- [UIApplicationDidReceiveMemoryWarningNotification](../uiapplication/didreceivememorywarningnotification.md) — A notification that posts when the app receives a warning from the operating system about low memory availability.
- [UIApplicationSignificantTimeChangeNotification](../uiapplication/significanttimechangenotification.md) — A notification that posts when there’s a significant change in time.
