---
title: 'applicationDidEnterBackground(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplicationdelegate/applicationdidenterbackground(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationdidenterbackground(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/applicationdidenterbackground%28_%3A%29.json'
content_hash: 'sha256:dc6b6cb33b897e8a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# applicationDidEnterBackground(_:)

<sub>Instance Method</sub>

Tells the delegate that the app is now in the background.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func applicationDidEnterBackground(_ application: UIApplication)
```

## Parameters

- `application` — Your singleton app object.

## Discussion

> [!important] Important
> If you’re using scenes (see [Scenes](../scenes.md)), UIKit will not call this method. Use [- sceneDidEnterBackground:](<../uiscenedelegate/scenedidenterbackground(__).md>) instead to perform any final tasks. UIKit posts a [UIApplicationDidEnterBackgroundNotification](../uiapplication/didenterbackgroundnotification.md) regardless of whether your app uses scenes.

Use this method to release shared resources, invalidate timers, and store enough app state information to restore your app to its current state in case it’s terminated later. Disable updates to your app’s user interface, and avoid using some types of shared system resources (such as the user’s contacts database). Don’t use OpenGL ES in the background.

Return from [- applicationDidEnterBackground:](<applicationdidenterbackground(__).md>) as quickly as possible. Your implementation of this method has approximately five seconds to perform any tasks and return. If the method doesn’t return before time runs out, your app is terminated and purged from memory.

If you need additional time to perform any final tasks, request additional execution time from the system by calling [- beginBackgroundTaskWithExpirationHandler:](<../uiapplication/beginbackgroundtask(expirationhandler_).md>). Call [- beginBackgroundTaskWithExpirationHandler:](<../uiapplication/beginbackgroundtask(expirationhandler_).md>) as early as possible. Because the system needs time to process your request, there’s a chance that the system might suspend your app before that task assertion is granted. For example, don’t call [- beginBackgroundTaskWithExpirationHandler:](<../uiapplication/beginbackgroundtask(expirationhandler_).md>) at the very end of your [- applicationDidEnterBackground:](<applicationdidenterbackground(__).md>) method and expect your app to continue running.

Perform any tasks related to adjusting your user interface before [- applicationDidEnterBackground:](<applicationdidenterbackground(__).md>) exits. Move other tasks (such as saving state) to a concurrent dispatch queue or secondary thread as needed. Because it’s likely any background tasks you start in [- applicationDidEnterBackground:](<applicationdidenterbackground(__).md>) won’t run until after that method exits, request additional background execution time before starting those tasks. In other words, first call [- beginBackgroundTaskWithExpirationHandler:](<../uiapplication/beginbackgroundtask(expirationhandler_).md>) and _then_ run the task on a dispatch queue or secondary thread.

UIKit also posts a [UIApplicationDidEnterBackgroundNotification](../uiapplication/didenterbackgroundnotification.md) around the same time it calls this method to give interested objects a chance to respond to the transition.

For more information about how to transition gracefully to the background, and for information about how to start background tasks, see [App Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072).

## See Also

### Responding to app life-cycle events

- [- applicationDidBecomeActive:](<applicationdidbecomeactive(__).md>) — Tells the delegate that the app has become active. _(deprecated)_
- [- applicationWillResignActive:](<applicationwillresignactive(__).md>) — Tells the delegate that the app is about to become inactive. _(deprecated)_
- [- applicationWillEnterForeground:](<applicationwillenterforeground(__).md>) — Tells the delegate that the app is about to enter the foreground. _(deprecated)_
- [- applicationWillTerminate:](<applicationwillterminate(__).md>) — Tells the delegate when the app is about to terminate.
- [UIApplicationDidBecomeActiveNotification](../uiapplication/didbecomeactivenotification.md) — A notification that posts when the app becomes active.
- [UIApplicationDidEnterBackgroundNotification](../uiapplication/didenterbackgroundnotification.md) — A notification that posts when the app enters the background.
- [UIApplicationWillEnterForegroundNotification](../uiapplication/willenterforegroundnotification.md) — A notification that posts shortly before an app leaves the background state on its way to becoming the active app.
- [UIApplicationWillResignActiveNotification](../uiapplication/willresignactivenotification.md) — A notification that posts when the app is no longer active and loses focus.
- [UIApplicationWillTerminateNotification](../uiapplication/willterminatenotification.md) — A notification that posts when the app is about to terminate.
