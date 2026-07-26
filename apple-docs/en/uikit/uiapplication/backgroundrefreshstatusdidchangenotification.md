---
title: backgroundRefreshStatusDidChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/backgroundrefreshstatusdidchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/backgroundrefreshstatusdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/backgroundrefreshstatusdidchangenotification.json'
content_hash: 'sha256:802bbc3d5d668bca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# backgroundRefreshStatusDidChangeNotification

<sub>Type Property</sub>

A notification that posts when the app’s status for downloading content in the background changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated class let backgroundRefreshStatusDidChangeNotification: NSNotification.Name
```

## Discussion

The system sends this notification when the [backgroundRefreshStatus](backgroundrefreshstatus.md) property of the app object changes. That property can change in response to the user disabling multitasking support for the app. The `object` of the notification is the `UIApplication` object. There is no `userInfo` dictionary.

## See Also

### Managing background tasks

- [backgroundRefreshStatus](backgroundrefreshstatus.md) — Indicates whether the app can refresh content when running in the background.
- [UIBackgroundRefreshStatus](../uibackgroundrefreshstatus.md) — Constants that indicate whether background execution is enabled for the app.
- [- beginBackgroundTaskWithName:expirationHandler:](<beginbackgroundtask(withname_expirationhandler_).md>) — Marks the start of a task with a custom name that should continue if the app enters the background.
- [- beginBackgroundTaskWithExpirationHandler:](<beginbackgroundtask(expirationhandler_).md>) — Marks the start of a task that should continue if the app enters the background.
- [- endBackgroundTask:](<endbackgroundtask(__).md>) — Marks the end of a specific long-running background task.
- [UIBackgroundTaskIdentifier](../uibackgroundtaskidentifier.md) — A unique token that identifies a request to run in the background.
- [backgroundTimeRemaining](backgroundtimeremaining.md) — The maximum amount of time remaining for the app to run in the background.
