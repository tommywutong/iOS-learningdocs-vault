---
title: 'applicationWillResignActive(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（26.0 起废弃）, iPadOS 2.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplicationdelegate/applicationwillresignactive(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationwillresignactive(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/applicationwillresignactive%28_%3A%29.json'
content_hash: 'sha256:41f28ff281c4d243'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# applicationWillResignActive(_:)

<sub>Instance Method</sub>

Tells the delegate that the app is about to become inactive.

> [!warning] Deprecated
> Use UIScene lifecycle and sceneWillResignActive(_:) from UISceneDelegate or the UIApplication.willResignActiveNotification instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func applicationWillResignActive(_ application: UIApplication)
```

## Parameters

- `application` — Your singleton app object.

## Discussion

> [!important] Important
> If you’re using scenes (see [Scenes](../scenes.md)), UIKit will not call this method. Use [- sceneWillResignActive:](<../uiscenedelegate/scenewillresignactive(__).md>) instead to pause any activity or save state. UIKit posts a [UIApplicationWillResignActiveNotification](../uiapplication/willresignactivenotification.md) regardless of whether your app uses scenes.

UIKit calls this method to let your app know that it is about to move from the active to inactive state. The app moves to the inactive state because of temporary interruptions like an incoming phone call or SMS message, or when the user quits the app and it begins the transition to the background state. An app in the inactive state continues to run but doesn’t dispatch incoming events to responders.

Use this method to pause ongoing tasks, disable timers, and throttle down OpenGL ES frame rates. Games should use this method to pause the game. An app in the inactive state should do minimal work while it waits to transition to either the active or background state.

If your app has unsaved user data, you can save it to ensure that it isn’t lost. However, it is recommended that you save user data at appropriate points throughout the execution of your app, usually in response to specific actions. For example, save data when the user dismisses a data entry screen. Don’t rely on specific app state transitions to save all of your app’s critical data.

After calling this method, UIKit also posts a [UIApplicationWillResignActiveNotification](../uiapplication/willresignactivenotification.md) to give interested objects a chance to respond to the transition.

## See Also

### Responding to app life-cycle events

- [- applicationDidBecomeActive:](<applicationdidbecomeactive(__).md>) — Tells the delegate that the app has become active. _(deprecated)_
- [- applicationDidEnterBackground:](<applicationdidenterbackground(__).md>) — Tells the delegate that the app is now in the background.
- [- applicationWillEnterForeground:](<applicationwillenterforeground(__).md>) — Tells the delegate that the app is about to enter the foreground. _(deprecated)_
- [- applicationWillTerminate:](<applicationwillterminate(__).md>) — Tells the delegate when the app is about to terminate.
- [UIApplicationDidBecomeActiveNotification](../uiapplication/didbecomeactivenotification.md) — A notification that posts when the app becomes active.
- [UIApplicationDidEnterBackgroundNotification](../uiapplication/didenterbackgroundnotification.md) — A notification that posts when the app enters the background.
- [UIApplicationWillEnterForegroundNotification](../uiapplication/willenterforegroundnotification.md) — A notification that posts shortly before an app leaves the background state on its way to becoming the active app.
- [UIApplicationWillResignActiveNotification](../uiapplication/willresignactivenotification.md) — A notification that posts when the app is no longer active and loses focus.
- [UIApplicationWillTerminateNotification](../uiapplication/willterminatenotification.md) — A notification that posts when the app is about to terminate.
