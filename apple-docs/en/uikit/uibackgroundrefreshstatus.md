---
title: UIBackgroundRefreshStatus
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibackgroundrefreshstatus
source_url: 'https://developer.apple.com/documentation/uikit/uibackgroundrefreshstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibackgroundrefreshstatus.json'
content_hash: 'sha256:906a7f03dfa8ef37'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIBackgroundRefreshStatus

<sub>Enumeration</sub>

Constants that indicate whether background execution is enabled for the app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UIBackgroundRefreshStatus
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UIBackgroundRefreshStatusRestricted](uibackgroundrefreshstatus/restricted.md) — Background updates are unavailable and the user cannot enable them again.
- [UIBackgroundRefreshStatusDenied](uibackgroundrefreshstatus/denied.md) — The user explicitly disabled background behavior for this app or for the whole system.
- [UIBackgroundRefreshStatusAvailable](uibackgroundrefreshstatus/available.md) — Background updates are available for the app.

### Initializers

- [init(rawValue:)](<uibackgroundrefreshstatus/init(rawvalue_).md>)

## See Also

### Managing background tasks

- [backgroundRefreshStatus](uiapplication/backgroundrefreshstatus.md) — Indicates whether the app can refresh content when running in the background.
- [UIApplicationBackgroundRefreshStatusDidChangeNotification](uiapplication/backgroundrefreshstatusdidchangenotification.md) — A notification that posts when the app’s status for downloading content in the background changes.
- [- beginBackgroundTaskWithName:expirationHandler:](<uiapplication/beginbackgroundtask(withname_expirationhandler_).md>) — Marks the start of a task with a custom name that should continue if the app enters the background.
- [- beginBackgroundTaskWithExpirationHandler:](<uiapplication/beginbackgroundtask(expirationhandler_).md>) — Marks the start of a task that should continue if the app enters the background.
- [- endBackgroundTask:](<uiapplication/endbackgroundtask(__).md>) — Marks the end of a specific long-running background task.
- [UIBackgroundTaskIdentifier](uibackgroundtaskidentifier.md) — A unique token that identifies a request to run in the background.
- [backgroundTimeRemaining](uiapplication/backgroundtimeremaining.md) — The maximum amount of time remaining for the app to run in the background.
