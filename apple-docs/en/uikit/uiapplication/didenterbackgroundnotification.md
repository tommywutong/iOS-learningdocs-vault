---
title: didEnterBackgroundNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/didenterbackgroundnotification
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/didenterbackgroundnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/didenterbackgroundnotification.json'
content_hash: 'sha256:4c005081fe871883'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# didEnterBackgroundNotification

<sub>Type Property</sub>

A notification that posts when the app enters the background.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated class let didEnterBackgroundNotification: NSNotification.Name
```

## Discussion

The `object` of the notification is the [UIApplication](../uiapplication.md) object. There is no `userInfo` dictionary.

## See Also

### Responding to app life-cycle events

- [- applicationDidBecomeActive:](<../uiapplicationdelegate/applicationdidbecomeactive(__).md>) — Tells the delegate that the app has become active. _(deprecated)_
- [- applicationWillResignActive:](<../uiapplicationdelegate/applicationwillresignactive(__).md>) — Tells the delegate that the app is about to become inactive. _(deprecated)_
- [- applicationDidEnterBackground:](<../uiapplicationdelegate/applicationdidenterbackground(__).md>) — Tells the delegate that the app is now in the background.
- [- applicationWillEnterForeground:](<../uiapplicationdelegate/applicationwillenterforeground(__).md>) — Tells the delegate that the app is about to enter the foreground. _(deprecated)_
- [- applicationWillTerminate:](<../uiapplicationdelegate/applicationwillterminate(__).md>) — Tells the delegate when the app is about to terminate.
- [UIApplicationDidBecomeActiveNotification](didbecomeactivenotification.md) — A notification that posts when the app becomes active.
- [UIApplicationWillEnterForegroundNotification](willenterforegroundnotification.md) — A notification that posts shortly before an app leaves the background state on its way to becoming the active app.
- [UIApplicationWillResignActiveNotification](willresignactivenotification.md) — A notification that posts when the app is no longer active and loses focus.
- [UIApplicationWillTerminateNotification](willterminatenotification.md) — A notification that posts when the app is about to terminate.
