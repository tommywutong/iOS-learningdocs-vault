---
title: 'applicationWillTerminate(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplicationdelegate/applicationwillterminate(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationwillterminate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/applicationwillterminate%28_%3A%29.json'
content_hash: 'sha256:8cc404de31f28b4a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# applicationWillTerminate(_:)

<sub>Instance Method</sub>

Tells the delegate when the app is about to terminate.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func applicationWillTerminate(_ application: UIApplication)
```

## Parameters

- `application` — Your singleton app object.

## Discussion

This method lets your app know that it is about to be terminated and purged from memory entirely. You should use this method to perform any final clean-up tasks for your app, such as freeing shared resources, saving user data, and invalidating timers. Your implementation of this method has approximately five seconds to perform any tasks and return. If the method does not return before time expires, the system may terminate the process altogether.

For apps that do not support background execution or are linked against iOS 3.x or earlier, this method is always called when the user quits the app. For apps that support background execution, this method is generally not called when the user quits the app because the app simply moves to the background in that case. However, this method may be called in situations where the app is running in the background (not suspended) and the system needs to terminate it for some reason.

After calling this method, the app also posts a [UIApplicationWillTerminateNotification](../uiapplication/willterminatenotification.md) notification to give interested objects a chance to respond to the transition.

## See Also

### Related Documentation

- [- application:didFinishLaunchingWithOptions:](<application(__didfinishlaunchingwithoptions_).md>) — Tells the delegate that the launch process is almost done and the app is almost ready to run.

### Responding to app life-cycle events

- [- applicationDidBecomeActive:](<applicationdidbecomeactive(__).md>) — Tells the delegate that the app has become active. _(deprecated)_
- [- applicationWillResignActive:](<applicationwillresignactive(__).md>) — Tells the delegate that the app is about to become inactive. _(deprecated)_
- [- applicationDidEnterBackground:](<applicationdidenterbackground(__).md>) — Tells the delegate that the app is now in the background.
- [- applicationWillEnterForeground:](<applicationwillenterforeground(__).md>) — Tells the delegate that the app is about to enter the foreground. _(deprecated)_
- [UIApplicationDidBecomeActiveNotification](../uiapplication/didbecomeactivenotification.md) — A notification that posts when the app becomes active.
- [UIApplicationDidEnterBackgroundNotification](../uiapplication/didenterbackgroundnotification.md) — A notification that posts when the app enters the background.
- [UIApplicationWillEnterForegroundNotification](../uiapplication/willenterforegroundnotification.md) — A notification that posts shortly before an app leaves the background state on its way to becoming the active app.
- [UIApplicationWillResignActiveNotification](../uiapplication/willresignactivenotification.md) — A notification that posts when the app is no longer active and loses focus.
- [UIApplicationWillTerminateNotification](../uiapplication/willterminatenotification.md) — A notification that posts when the app is about to terminate.
