---
title: 'application(_:willContinueUserActivityWithType:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（26.0 起废弃）, iPadOS 8.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplicationdelegate/application(_:willcontinueuseractivitywithtype:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:willcontinueuseractivitywithtype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/application%28_%3Awillcontinueuseractivitywithtype%3A%29.json'
content_hash: 'sha256:292147cae017bb1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# application(_:willContinueUserActivityWithType:)

<sub>Instance Method</sub>

Tells the delegate if your app takes responsibility for notifying users when a continuation activity takes longer than expected.

> [!warning] Deprecated
> Use UIScene lifecycle and scene(_:willContinueUserActivityWithType:) from UISceneDelegate instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func application(_ application: UIApplication, willContinueUserActivityWithType userActivityType: String) -> Bool
```

## Parameters

- `application` — Your shared app object.

- `userActivityType` — The requested activity type.

## Return Value

[true](../../swift/true.md) if you want to notify the user that a continuation is in progress or [false](../../swift/false.md) if you want iOS to notify the user.

## Discussion

Use this method to provide immediate feedback to the user that an activity is about to continue on this device. The app calls this method as soon as the user confirms that an activity should be continued but possibly before the data associated with that activity is available.

Your implementation of this method should prepare to initiate the activity. If you notify the user as part of your preparations, return [true](../../swift/true.md) from this method so that iOS does not also notify the user. If you do not implement this method or your implementation returns [false](../../swift/false.md), iOS notifes the user.

This method is not called if either [- application:willFinishLaunchingWithOptions:](<application(__willfinishlaunchingwithoptions_).md>) or [- application:didFinishLaunchingWithOptions:](<application(__didfinishlaunchingwithoptions_).md>) returns [false](../../swift/false.md).

## See Also

### Continuing user activity and handling quick actions

- [- application:continueUserActivity:restorationHandler:](<application(__continue_restorationhandler_).md>) — Tells the delegate that the data for continuing an activity is available. _(deprecated)_
- [- application:didUpdateUserActivity:](<application(__didupdate_).md>) — Tells the delegate that the activity was updated. _(deprecated)_
- [- application:didFailToContinueUserActivityWithType:error:](<application(__didfailtocontinueuseractivitywithtype_error_).md>) — Tells the delegate that the activity couldn’t be continued. _(deprecated)_
- [- application:performActionForShortcutItem:completionHandler:](<application(__performactionfor_completionhandler_).md>) — Tells the delegate that the user selected a Home screen quick action for your app, except when you’ve intercepted the interaction in a launch method. _(deprecated)_
