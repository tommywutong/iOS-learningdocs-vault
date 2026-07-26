---
title: 'applicationDidBecomeActive(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（26.0 起废弃）, iPadOS 2.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplicationdelegate/applicationdidbecomeactive(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationdidbecomeactive(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/applicationdidbecomeactive%28_%3A%29.json'
content_hash: 'sha256:d82d489fe13c5ad0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# applicationDidBecomeActive(_:)

<sub>Instance Method</sub>

Tells the delegate that the app has become active.

> [!warning] Deprecated
> Use UIScene lifecycle and sceneDidBecomeActive(_:) from UISceneDelegate or the UIApplication.didBecomeActiveNotification instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func applicationDidBecomeActive(_ application: UIApplication)
```

## Parameters

- `application` — Your singleton app object.

## Discussion

> [!important] Important
> If you’re using scenes (see [Scenes](../scenes.md)), UIKit will not call this method. Use [- sceneDidBecomeActive:](<../uiscenedelegate/scenedidbecomeactive(__).md>) instead to restart any tasks or refresh your app’s user interface. UIKit posts a [UIApplicationDidBecomeActiveNotification](../uiapplication/didbecomeactivenotification.md) regardless of whether your app uses scenes.

UIKit calls this method to let your app know that it moved from the inactive to active state. The app moves to the active state because it was launched by the user or the system, or because the user ignores an interruption (like an incoming phone call or SMS message) that sent the app temporarily to the inactive state.

Use this method to restart any tasks that were paused (or not yet started) while the app was inactive. For example, use it to restart timers or throttle up OpenGL ES frame rates. If your app was previously in the background, you can also use it to refresh your app’s user interface.

After calling this method, UIKit posts a [UIApplicationDidBecomeActiveNotification](../uiapplication/didbecomeactivenotification.md) to give interested objects a chance to respond to the transition.

## See Also

### Responding to app life-cycle events

- [- applicationWillResignActive:](<applicationwillresignactive(__).md>) — Tells the delegate that the app is about to become inactive. _(deprecated)_
- [- applicationDidEnterBackground:](<applicationdidenterbackground(__).md>) — Tells the delegate that the app is now in the background.
- [- applicationWillEnterForeground:](<applicationwillenterforeground(__).md>) — Tells the delegate that the app is about to enter the foreground. _(deprecated)_
- [- applicationWillTerminate:](<applicationwillterminate(__).md>) — Tells the delegate when the app is about to terminate.
- [UIApplicationDidBecomeActiveNotification](../uiapplication/didbecomeactivenotification.md) — A notification that posts when the app becomes active.
- [UIApplicationDidEnterBackgroundNotification](../uiapplication/didenterbackgroundnotification.md) — A notification that posts when the app enters the background.
- [UIApplicationWillEnterForegroundNotification](../uiapplication/willenterforegroundnotification.md) — A notification that posts shortly before an app leaves the background state on its way to becoming the active app.
- [UIApplicationWillResignActiveNotification](../uiapplication/willresignactivenotification.md) — A notification that posts when the app is no longer active and loses focus.
- [UIApplicationWillTerminateNotification](../uiapplication/willterminatenotification.md) — A notification that posts when the app is about to terminate.
