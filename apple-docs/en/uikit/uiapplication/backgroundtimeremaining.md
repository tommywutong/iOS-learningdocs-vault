---
title: backgroundTimeRemaining
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/backgroundtimeremaining
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/backgroundtimeremaining'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/backgroundtimeremaining.json'
content_hash: 'sha256:4ecbb2fe72824068'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# backgroundTimeRemaining

<sub>Instance Property</sub>

The maximum amount of time remaining for the app to run in the background.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated var backgroundTimeRemaining: TimeInterval { get }
```

## Discussion

The value is valid only after the app enters the background and has started at least one task using [- beginBackgroundTaskWithExpirationHandler:](<beginbackgroundtask(expirationhandler_).md>) in the foreground.

System conditions may end background execution earlier, either by calling the expiration handler, or by terminating the app.

This method can be safely called on a non-main thread.

## See Also

### Managing background tasks

- [backgroundRefreshStatus](backgroundrefreshstatus.md) — Indicates whether the app can refresh content when running in the background.
- [UIBackgroundRefreshStatus](../uibackgroundrefreshstatus.md) — Constants that indicate whether background execution is enabled for the app.
- [UIApplicationBackgroundRefreshStatusDidChangeNotification](backgroundrefreshstatusdidchangenotification.md) — A notification that posts when the app’s status for downloading content in the background changes.
- [- beginBackgroundTaskWithName:expirationHandler:](<beginbackgroundtask(withname_expirationhandler_).md>) — Marks the start of a task with a custom name that should continue if the app enters the background.
- [- beginBackgroundTaskWithExpirationHandler:](<beginbackgroundtask(expirationhandler_).md>) — Marks the start of a task that should continue if the app enters the background.
- [- endBackgroundTask:](<endbackgroundtask(__).md>) — Marks the end of a specific long-running background task.
- [UIBackgroundTaskIdentifier](../uibackgroundtaskidentifier.md) — A unique token that identifies a request to run in the background.
