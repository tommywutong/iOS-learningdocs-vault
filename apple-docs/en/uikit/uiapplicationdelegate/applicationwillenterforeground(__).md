---
title: 'applicationWillEnterForeground(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（26.0 起废弃）, iPadOS 4.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplicationdelegate/applicationwillenterforeground(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationwillenterforeground(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/applicationwillenterforeground%28_%3A%29.json'
content_hash: 'sha256:21478cd5ba2feb44'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# applicationWillEnterForeground(_:)

<sub>Instance Method</sub>

Tells the delegate that the app is about to enter the foreground.

> [!warning] Deprecated
> Use UIScene lifecycle and sceneWillEnterForeground(_:) from UISceneDelegate or the UIApplication.willEnterForegroundNotification instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func applicationWillEnterForeground(_ application: UIApplication)
```

## Parameters

- `application` — Your singleton app object.

## Discussion

> [!important] Important
> If you’re using scenes (see [Scenes](../scenes.md)), UIKit will not call this method. Use [- sceneWillEnterForeground:](<../uiscenedelegate/scenewillenterforeground(__).md>) instead to prepare your app to enter the foreground. UIKit posts a [UIApplicationWillEnterForegroundNotification](../uiapplication/willenterforegroundnotification.md) regardless of whether your app uses [Scenes](../scenes.md).

In iOS 4.0 and later, UIKit calls this method as part of the transition from the background to the active state. You can use this method to undo many of the changes you made to your app upon entering the background. The call to this method is invariably followed by a call to the [- applicationDidBecomeActive:](<applicationdidbecomeactive(__).md>) method, which then moves the app from the inactive to the active state.

UIKit also posts a [UIApplicationWillEnterForegroundNotification](../uiapplication/willenterforegroundnotification.md) shortly before calling this method to give interested objects a chance to respond to the transition.

## See Also

### Responding to app life-cycle events

- [- applicationDidBecomeActive:](<applicationdidbecomeactive(__).md>) — Tells the delegate that the app has become active. _(deprecated)_
- [- applicationWillResignActive:](<applicationwillresignactive(__).md>) — Tells the delegate that the app is about to become inactive. _(deprecated)_
- [- applicationDidEnterBackground:](<applicationdidenterbackground(__).md>) — Tells the delegate that the app is now in the background.
- [- applicationWillTerminate:](<applicationwillterminate(__).md>) — Tells the delegate when the app is about to terminate.
- [UIApplicationDidBecomeActiveNotification](../uiapplication/didbecomeactivenotification.md) — A notification that posts when the app becomes active.
- [UIApplicationDidEnterBackgroundNotification](../uiapplication/didenterbackgroundnotification.md) — A notification that posts when the app enters the background.
- [UIApplicationWillEnterForegroundNotification](../uiapplication/willenterforegroundnotification.md) — A notification that posts shortly before an app leaves the background state on its way to becoming the active app.
- [UIApplicationWillResignActiveNotification](../uiapplication/willresignactivenotification.md) — A notification that posts when the app is no longer active and loses focus.
- [UIApplicationWillTerminateNotification](../uiapplication/willterminatenotification.md) — A notification that posts when the app is about to terminate.
