---
title: 'application(_:didUpdate:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（26.0 起废弃）, iPadOS 8.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplicationdelegate/application(_:didupdate:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:didupdate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/application%28_%3Adidupdate%3A%29.json'
content_hash: 'sha256:6b8281870a201eef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# application(_:didUpdate:)

<sub>Instance Method</sub>

Tells the delegate that the activity was updated.

> [!warning] Deprecated
> Use UIScene lifecycle and scene(_:didUpdate) from UISceneDelegate instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func application(_ application: UIApplication, didUpdate userActivity: NSUserActivity)
```

## Parameters

- `application` — Your shared app object.

- `userActivity` — The activity object containing the data associated with the task the user was performing.

## Discussion

This method is called on the main thread when a user activity managed by UIKit has been updated. You can implement this method as a final opportunity to add data to the user activity object.

## See Also

### Continuing user activity and handling quick actions

- [- application:willContinueUserActivityWithType:](<application(__willcontinueuseractivitywithtype_).md>) — Tells the delegate if your app takes responsibility for notifying users when a continuation activity takes longer than expected. _(deprecated)_
- [- application:continueUserActivity:restorationHandler:](<application(__continue_restorationhandler_).md>) — Tells the delegate that the data for continuing an activity is available. _(deprecated)_
- [- application:didFailToContinueUserActivityWithType:error:](<application(__didfailtocontinueuseractivitywithtype_error_).md>) — Tells the delegate that the activity couldn’t be continued. _(deprecated)_
- [- application:performActionForShortcutItem:completionHandler:](<application(__performactionfor_completionhandler_).md>) — Tells the delegate that the user selected a Home screen quick action for your app, except when you’ve intercepted the interaction in a launch method. _(deprecated)_
