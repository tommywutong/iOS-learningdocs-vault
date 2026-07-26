---
title: 'applicationProtectedDataDidBecomeAvailable(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplicationdelegate/applicationprotecteddatadidbecomeavailable(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationprotecteddatadidbecomeavailable(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/applicationprotecteddatadidbecomeavailable%28_%3A%29.json'
content_hash: 'sha256:5e8973af99625ae7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# applicationProtectedDataDidBecomeAvailable(_:)

<sub>Instance Method</sub>

Tells the delegate that protected files are available now.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func applicationProtectedDataDidBecomeAvailable(_ application: UIApplication)
```

## Parameters

- `application` — Your singleton app object.

## Discussion

On a device that uses content protection, protected files are stored in an encrypted form and made available only at certain times, usually when the device is unlocked. This notification lets your app know that the device is now unlocked and that you may access certain types of protected files again.

## See Also

### Responding to environment changes

- [- applicationProtectedDataWillBecomeUnavailable:](<applicationprotecteddatawillbecomeunavailable(__).md>) — Tells the delegate that the protected files are about to become unavailable.
- [- applicationDidReceiveMemoryWarning:](<applicationdidreceivememorywarning(__).md>) — Tells the delegate when the app receives a memory warning from the system.
- [- applicationSignificantTimeChange:](<applicationsignificanttimechange(__).md>) — Tells the delegate when there is a significant change in the time.
- [UIApplicationProtectedDataDidBecomeAvailable](../uiapplication/protecteddatadidbecomeavailablenotification.md) — A notification that posts when the protected files become available for your code to access.
- [UIApplicationProtectedDataWillBecomeUnavailable](../uiapplication/protecteddatawillbecomeunavailablenotification.md) — A notification that posts shortly before protected files are locked down and become inaccessible.
- [UIApplicationDidReceiveMemoryWarningNotification](../uiapplication/didreceivememorywarningnotification.md) — A notification that posts when the app receives a warning from the operating system about low memory availability.
- [UIApplicationSignificantTimeChangeNotification](../uiapplication/significanttimechangenotification.md) — A notification that posts when there’s a significant change in time.
