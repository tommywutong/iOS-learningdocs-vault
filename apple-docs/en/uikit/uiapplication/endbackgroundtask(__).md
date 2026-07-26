---
title: 'endBackgroundTask(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplication/endbackgroundtask(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/endbackgroundtask(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/endbackgroundtask%28_%3A%29.json'
content_hash: 'sha256:52abf92ccf2baa85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# endBackgroundTask(_:)

<sub>Instance Method</sub>

Marks the end of a specific long-running background task.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated func endBackgroundTask(_ identifier: UIBackgroundTaskIdentifier)
```

## Parameters

- `identifier` — An identifier returned by the [- beginBackgroundTaskWithExpirationHandler:](<beginbackgroundtask(expirationhandler_).md>) method.

## Discussion

You must call this method to end a task that was started using the [- beginBackgroundTaskWithExpirationHandler:](<beginbackgroundtask(expirationhandler_).md>) method. If you do not, the system may terminate your app.

This method can be safely called on a non-main thread.

## See Also

### Managing background tasks

- [backgroundRefreshStatus](backgroundrefreshstatus.md) — Indicates whether the app can refresh content when running in the background.
- [UIBackgroundRefreshStatus](../uibackgroundrefreshstatus.md) — Constants that indicate whether background execution is enabled for the app.
- [UIApplicationBackgroundRefreshStatusDidChangeNotification](backgroundrefreshstatusdidchangenotification.md) — A notification that posts when the app’s status for downloading content in the background changes.
- [- beginBackgroundTaskWithName:expirationHandler:](<beginbackgroundtask(withname_expirationhandler_).md>) — Marks the start of a task with a custom name that should continue if the app enters the background.
- [- beginBackgroundTaskWithExpirationHandler:](<beginbackgroundtask(expirationhandler_).md>) — Marks the start of a task that should continue if the app enters the background.
- [UIBackgroundTaskIdentifier](../uibackgroundtaskidentifier.md) — A unique token that identifies a request to run in the background.
- [backgroundTimeRemaining](backgroundtimeremaining.md) — The maximum amount of time remaining for the app to run in the background.
