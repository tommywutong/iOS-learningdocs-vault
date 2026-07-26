---
title: willResignActiveNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/willresignactivenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/willresignactivenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/willresignactivenotification.json'
content_hash: 'sha256:aada4c364008365d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# willResignActiveNotification

<sub>Type Property</sub>

A notification that posts when the app is no longer active and loses focus.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated class let willResignActiveNotification: NSNotification.Name
```

## Discussion

An app is active when it is receiving events. An active app can be said to have focus. It gains focus after being launched, loses focus when an overlay window pops up or when the device is locked, and gains focus when the device is unlocked.

## See Also

### Responding to app life-cycle events

- [- applicationDidBecomeActive:](<../uiapplicationdelegate/applicationdidbecomeactive(__).md>) — Tells the delegate that the app has become active. _(deprecated)_
- [- applicationWillResignActive:](<../uiapplicationdelegate/applicationwillresignactive(__).md>) — Tells the delegate that the app is about to become inactive. _(deprecated)_
- [- applicationDidEnterBackground:](<../uiapplicationdelegate/applicationdidenterbackground(__).md>) — Tells the delegate that the app is now in the background.
- [- applicationWillEnterForeground:](<../uiapplicationdelegate/applicationwillenterforeground(__).md>) — Tells the delegate that the app is about to enter the foreground. _(deprecated)_
- [- applicationWillTerminate:](<../uiapplicationdelegate/applicationwillterminate(__).md>) — Tells the delegate when the app is about to terminate.
- [UIApplicationDidBecomeActiveNotification](didbecomeactivenotification.md) — A notification that posts when the app becomes active.
- [UIApplicationDidEnterBackgroundNotification](didenterbackgroundnotification.md) — A notification that posts when the app enters the background.
- [UIApplicationWillEnterForegroundNotification](willenterforegroundnotification.md) — A notification that posts shortly before an app leaves the background state on its way to becoming the active app.
- [UIApplicationWillTerminateNotification](willterminatenotification.md) — A notification that posts when the app is about to terminate.
