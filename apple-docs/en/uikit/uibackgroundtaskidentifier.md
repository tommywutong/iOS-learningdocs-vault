---
title: UIBackgroundTaskIdentifier
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibackgroundtaskidentifier
source_url: 'https://developer.apple.com/documentation/uikit/uibackgroundtaskidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibackgroundtaskidentifier.json'
content_hash: 'sha256:b74abe6cae76ca58'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIBackgroundTaskIdentifier

<sub>Structure</sub>

A unique token that identifies a request to run in the background.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct UIBackgroundTaskIdentifier
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Identifier

- [UIBackgroundTaskInvalid](uibackgroundtaskidentifier/invalid.md) — A token that indicates an invalid task request.

### Initializers

- [init(rawValue:)](<uibackgroundtaskidentifier/init(rawvalue_).md>) — Creates a new instance with the specified raw value.

## See Also

### Managing background tasks

- [backgroundRefreshStatus](uiapplication/backgroundrefreshstatus.md) — Indicates whether the app can refresh content when running in the background.
- [UIBackgroundRefreshStatus](uibackgroundrefreshstatus.md) — Constants that indicate whether background execution is enabled for the app.
- [UIApplicationBackgroundRefreshStatusDidChangeNotification](uiapplication/backgroundrefreshstatusdidchangenotification.md) — A notification that posts when the app’s status for downloading content in the background changes.
- [- beginBackgroundTaskWithName:expirationHandler:](<uiapplication/beginbackgroundtask(withname_expirationhandler_).md>) — Marks the start of a task with a custom name that should continue if the app enters the background.
- [- beginBackgroundTaskWithExpirationHandler:](<uiapplication/beginbackgroundtask(expirationhandler_).md>) — Marks the start of a task that should continue if the app enters the background.
- [- endBackgroundTask:](<uiapplication/endbackgroundtask(__).md>) — Marks the end of a specific long-running background task.
- [backgroundTimeRemaining](uiapplication/backgroundtimeremaining.md) — The maximum amount of time remaining for the app to run in the background.
