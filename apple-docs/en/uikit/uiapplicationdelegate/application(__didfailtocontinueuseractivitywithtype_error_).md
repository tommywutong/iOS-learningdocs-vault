---
title: 'application(_:didFailToContinueUserActivityWithType:error:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（26.0 起废弃）, iPadOS 8.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplicationdelegate/application(_:didfailtocontinueuseractivitywithtype:error:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:didfailtocontinueuseractivitywithtype:error:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/application%28_%3Adidfailtocontinueuseractivitywithtype%3Aerror%3A%29.json'
content_hash: 'sha256:1e3dcb741dbfe93f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# application(_:didFailToContinueUserActivityWithType:error:)

<sub>Instance Method</sub>

Tells the delegate that the activity couldn’t be continued.

> [!warning] Deprecated
> Use UIScene lifecycle and scene(_:didFailToContinueUserActivityWithType:error:) from UISceneDelegate instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func application(_ application: UIApplication, didFailToContinueUserActivityWithType userActivityType: String, error: any Error)
```

## Parameters

- `application` — Your shared app object.

- `userActivityType` — The activity type that was attempted.

- `error` — An error object indicating the reason for the failure.

## Discussion

Use this method to let the user know that the specified activity could not be continued. If you do not implement this method, UIKit displays an error to the user with an appropriate message about the reason for the failure.

This method is not called if either [- application:willFinishLaunchingWithOptions:](<application(__willfinishlaunchingwithoptions_).md>) or [- application:didFinishLaunchingWithOptions:](<application(__didfinishlaunchingwithoptions_).md>) returns [false](../../swift/false.md).

## See Also

### Continuing user activity and handling quick actions

- [- application:willContinueUserActivityWithType:](<application(__willcontinueuseractivitywithtype_).md>) — Tells the delegate if your app takes responsibility for notifying users when a continuation activity takes longer than expected. _(deprecated)_
- [- application:continueUserActivity:restorationHandler:](<application(__continue_restorationhandler_).md>) — Tells the delegate that the data for continuing an activity is available. _(deprecated)_
- [- application:didUpdateUserActivity:](<application(__didupdate_).md>) — Tells the delegate that the activity was updated. _(deprecated)_
- [- application:performActionForShortcutItem:completionHandler:](<application(__performactionfor_completionhandler_).md>) — Tells the delegate that the user selected a Home screen quick action for your app, except when you’ve intercepted the interaction in a launch method. _(deprecated)_
