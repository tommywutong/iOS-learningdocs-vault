---
title: 'beginBackgroundTask(withName:expirationHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplication/beginbackgroundtask(withname:expirationhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/beginbackgroundtask(withname:expirationhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/beginbackgroundtask%28withname%3Aexpirationhandler%3A%29.json'
content_hash: 'sha256:c3b58ac5ff9652c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# beginBackgroundTask(withName:expirationHandler:)

<sub>Instance Method</sub>

Marks the start of a task with a custom name that should continue if the app enters the background.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated func beginBackgroundTask(withName taskName: String?, expirationHandler handler: (@MainActor @Sendable () -> Void)? = nil) -> UIBackgroundTaskIdentifier
```

## Parameters

- `taskName` — The name to display in the debugger when viewing the background task. If you specify `nil` for this parameter, the method generates a name based on the name of the calling function or method.

- `handler` — A handler to be called shortly before the app’s remaining background time reaches 0. Use this handler to clean up and mark the end of the background task. Failure to end the task explicitly will result in the termination of the app. The system calls the handler synchronously on the main thread, blocking the app’s suspension momentarily.

## Return Value

A unique identifier for the new background task. You must pass this value to the [- endBackgroundTask:](<endbackgroundtask(__).md>) method to mark the end of this task. This method returns [UIBackgroundTaskInvalid](../uibackgroundtaskidentifier/invalid.md) if running in the background isn’t possible.

## Discussion

This method requests additional background execution time for your app. Call this method when leaving a task unfinished might be detrimental to your app’s user experience. For example, call this method before writing data to a file to prevent the system from suspending your app while the operation is in progress. For background tasks requiring more time, use [Background Tasks](../../backgroundtasks.md).

Call this method as early as possible before starting your task, preferably before your app actually enters the background. The method requests the task assertion for your app asynchronously. If you call this method shortly before your app is due to be suspended, there’s a chance that the system might suspend your app before that task assertion is granted. For example, don’t call this method at the very end of your [- applicationDidEnterBackground:](<../uiapplicationdelegate/applicationdidenterbackground(__).md>) method and expect your app to continue running. If the system is unable to grant the task assertion, it calls your expiration handler.

Each call to this method must be balanced by a matching call to the [- endBackgroundTask:](<endbackgroundtask(__).md>) method. Apps running background tasks have a finite amount of time in which to run them. (You can find out the maximum background time available using the [backgroundTimeRemaining](backgroundtimeremaining.md) property.) If you don’t call [- endBackgroundTask:](<endbackgroundtask(__).md>) for each task before time expires, the system kills the app. If you provide a block object in the handler parameter, the system calls your handler before time expires to give you a chance to end the task.

You can call this method at any point in your app’s execution. You may also call this method multiple times to mark the beginning of several background tasks that run in parallel. However, each task must be ended separately. You identify a given task using the value returned by this method.

This method can be safely called on a non-main thread. To extend the execution time of an app extension, use the [performExpiringActivity(withReason:using:)](<../../foundation/processinfo/performexpiringactivity(withreason_using_).md>) method of [ProcessInfo](../../foundation/processinfo.md) instead.

## See Also

### Related Documentation

- [Background Tasks](../../backgroundtasks.md) — Support background processing in your app by wrapping your app’s most critical work in framework-provided tasks.

### Managing background tasks

- [backgroundRefreshStatus](backgroundrefreshstatus.md) — Indicates whether the app can refresh content when running in the background.
- [UIBackgroundRefreshStatus](../uibackgroundrefreshstatus.md) — Constants that indicate whether background execution is enabled for the app.
- [UIApplicationBackgroundRefreshStatusDidChangeNotification](backgroundrefreshstatusdidchangenotification.md) — A notification that posts when the app’s status for downloading content in the background changes.
- [- beginBackgroundTaskWithExpirationHandler:](<beginbackgroundtask(expirationhandler_).md>) — Marks the start of a task that should continue if the app enters the background.
- [- endBackgroundTask:](<endbackgroundtask(__).md>) — Marks the end of a specific long-running background task.
- [UIBackgroundTaskIdentifier](../uibackgroundtaskidentifier.md) — A unique token that identifies a request to run in the background.
- [backgroundTimeRemaining](backgroundtimeremaining.md) — The maximum amount of time remaining for the app to run in the background.
