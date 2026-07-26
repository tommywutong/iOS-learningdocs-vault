---
title: Task Management
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/task-management
source_url: 'https://developer.apple.com/documentation/foundation/task-management'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/task-management.json'
content_hash: 'sha256:4b386fa5c95cb9cd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# Task Management

<sub>API Collection</sub>

Manage your app’s work and how it interacts with system services like Handoff and Shortcuts.

## Topics

### Undo

- [UndoManager](undomanager.md) — A general-purpose recorder of operations that enables undo and redo.

### Progress

- [ProgressReporting](progressreporting.md) — An interface for objects that report progress using a single progress instance.
- [Progress](progress.md) — An object that conveys ongoing progress to the user for a specified task.

### Operations

- [Operation](operation.md) — An abstract class that represents the code and data associated with a single task.
- [OperationQueue](operationqueue.md) — A queue that regulates the execution of operations.
- [BlockOperation](blockoperation.md) — An operation that manages the concurrent execution of one or more blocks.

### Scheduling

- [Timer](timer.md) — A timer that fires after a certain time interval has elapsed, sending a specified message to a target object.

### Activity Sharing

- [Creating a user activity object](creating-a-user-activity-object.md) — Identify key user interactions and include the information to restore them later.
- [Implementing Handoff in Your App](implementing-handoff-in-your-app.md) — Create, send, and receive user activities directly.
- [Continuing User Activities with Handoff](continuing-user-activities-with-handoff.md) — Define and manage which of your app’s activities can be continued between devices.
- [Increasing App Usage with Suggestions Based on User Activities](increasing-app-usage-with-suggestions-based-on-user-activities.md) — Provide a continuous user experience by capturing information from your app and displaying this information as proactive suggestions across the system.
- [Supporting the creation of Quick Notes](supporting-the-creation-of-quick-notes.md) — Support the creation of notes that include your app’s content.
- [NSUserActivity](nsuseractivity.md) — A representation of the state of your app at a moment in time.
- [NSUserActivityDelegate](nsuseractivitydelegate.md) — The interface through which a user activity instance notifies its delegate of updates.

### System Interaction

- [ProcessInfo](processinfo.md) — A collection of information about the current process.
- [NSBackgroundActivityScheduler](nsbackgroundactivityscheduler.md) — A task scheduler suitable for low priority operations that can run in the background.

### User Notifications

- [NSUserNotification](nsusernotification.md) — A notification that can be scheduled for display in the notification center. _(deprecated)_
- [NSUserNotificationAction](nsusernotificationaction.md) — An action that the user can take in response to receiving a notification. _(deprecated)_
- [NSUserNotificationCenter](nsusernotificationcenter.md) — An object that delivers notifications from apps to the user. _(deprecated)_
- [NSUserNotificationCenterDelegate](nsusernotificationcenterdelegate.md) — An interface that enables customizing the behavior of the default notification center.

### Combine Integration

- [Published](published.md) — A type alias for the Combine framework’s type that publishes a property marked with an attribute.
- [ObservableObject](observableobject.md) — A type alias for the Combine framework’s type for an object with a publisher that emits before the object has changed.

## See Also

### App Support

- [Resources](resources.md) — Access assets and other data bundled with your app.
- [Notifications](notifications.md) — Design patterns for broadcasting information and for subscribing to broadcasts.
- [App Extension Support](app-extension-support.md) — Manage the interaction between an app extension and its hosting app.
- [Errors and Exceptions](errors-and-exceptions.md) — Respond to problem situations in your interactions with APIs, and fine-tune your app for better debugging.
- [Scripting Support](scripting-support.md) — Allow users to control your app with AppleScript and other automation technologies, or run scripts from within your app.
