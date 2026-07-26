---
title: 'applicationProtectedDataWillBecomeUnavailable(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplicationdelegate/applicationprotecteddatawillbecomeunavailable(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationprotecteddatawillbecomeunavailable(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/applicationprotecteddatawillbecomeunavailable%28_%3A%29.json'
content_hash: 'sha256:7c8219d35567fc60'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# applicationProtectedDataWillBecomeUnavailable(_:)

<sub>Instance Method</sub>

Tells the delegate that the protected files are about to become unavailable.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func applicationProtectedDataWillBecomeUnavailable(_ application: UIApplication)
```

## Parameters

- `application` — Your singleton app object.

## Discussion

On a device that uses content protection, protected files are stored in an encrypted form and made available only at certain times, usually when the device is unlocked. This notification lets your app know that the device is about to be locked and that any protected files it is currently accessing might become unavailable shortly.

If your app is currently accessing a protected file, you can use this method to release any references to that file. Although it is not an error to access the file while the device is locked, any attempts to do so will fail. Therefore, if your app depends on the file, you might want to take steps to avoid using that file while the device is locked.

## See Also

### Responding to environment changes

- [- applicationProtectedDataDidBecomeAvailable:](<applicationprotecteddatadidbecomeavailable(__).md>) — Tells the delegate that protected files are available now.
- [- applicationDidReceiveMemoryWarning:](<applicationdidreceivememorywarning(__).md>) — Tells the delegate when the app receives a memory warning from the system.
- [- applicationSignificantTimeChange:](<applicationsignificanttimechange(__).md>) — Tells the delegate when there is a significant change in the time.
- [UIApplicationProtectedDataDidBecomeAvailable](../uiapplication/protecteddatadidbecomeavailablenotification.md) — A notification that posts when the protected files become available for your code to access.
- [UIApplicationProtectedDataWillBecomeUnavailable](../uiapplication/protecteddatawillbecomeunavailablenotification.md) — A notification that posts shortly before protected files are locked down and become inaccessible.
- [UIApplicationDidReceiveMemoryWarningNotification](../uiapplication/didreceivememorywarningnotification.md) — A notification that posts when the app receives a warning from the operating system about low memory availability.
- [UIApplicationSignificantTimeChangeNotification](../uiapplication/significanttimechangenotification.md) — A notification that posts when there’s a significant change in time.
