---
title: backgroundRefreshStatus
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/backgroundrefreshstatus
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/backgroundrefreshstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/backgroundrefreshstatus.json'
content_hash: 'sha256:50cfd4f2a8ac9250'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# backgroundRefreshStatus

<sub>Instance Property</sub>

Indicates whether the app can refresh content when running in the background.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var backgroundRefreshStatus: UIBackgroundRefreshStatus { get }
```

## Discussion

You can use this property to determine whether Background App Refresh—an app’s ability to open in the background to perform refresh tasks—is enabled, and warn the user if it is not. Don’t warn the user if the value of this property is set to [UIBackgroundRefreshStatusRestricted](../uibackgroundrefreshstatus/restricted.md). A restricted user, such as one who is managed under parental controls, can’t enable Background App Refresh.

Background App Refresh is disabled automatically when a device is operating in low-power mode. When this happens, the time available for performing background tasks is reduced to save power.

## See Also

### Managing background tasks

- [UIBackgroundRefreshStatus](../uibackgroundrefreshstatus.md) — Constants that indicate whether background execution is enabled for the app.
- [UIApplicationBackgroundRefreshStatusDidChangeNotification](backgroundrefreshstatusdidchangenotification.md) — A notification that posts when the app’s status for downloading content in the background changes.
- [- beginBackgroundTaskWithName:expirationHandler:](<beginbackgroundtask(withname_expirationhandler_).md>) — Marks the start of a task with a custom name that should continue if the app enters the background.
- [- beginBackgroundTaskWithExpirationHandler:](<beginbackgroundtask(expirationhandler_).md>) — Marks the start of a task that should continue if the app enters the background.
- [- endBackgroundTask:](<endbackgroundtask(__).md>) — Marks the end of a specific long-running background task.
- [UIBackgroundTaskIdentifier](../uibackgroundtaskidentifier.md) — A unique token that identifies a request to run in the background.
- [backgroundTimeRemaining](backgroundtimeremaining.md) — The maximum amount of time remaining for the app to run in the background.
