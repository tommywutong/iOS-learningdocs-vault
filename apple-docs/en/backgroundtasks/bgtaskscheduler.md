---
title: BGTaskScheduler
framework: Background Tasks
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgtaskscheduler
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgtaskscheduler.json'
content_hash: 'sha256:cdc8bb778a2f1759'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Background Tasks](../backgroundtasks.md)

# BGTaskScheduler

<sub>Class</sub>

A class for scheduling tasks that add background support to your app’s most critical work.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class BGTaskScheduler
```

## Overview

Background tasks give your app a way to run code even when the app is suspended:

- To register, schedule, and run tasks in the background, see [Using background tasks to update your app](../uikit/using-background-tasks-to-update-your-app.md).
- To submit work in the foreground that can finish even if the app moves to the background, see [Performing long-running tasks on iOS and iPadOS](performing-long-running-tasks-on-ios-and-ipados.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting the shared task scheduler

- [sharedScheduler](bgtaskscheduler/shared.md) — The shared background task scheduler instance.

### Checking task requirements

- [supportedResources](bgtaskscheduler/supportedresources.md) — Additional system resources that a continuous background task can request.

### Scheduling a task

- [- registerForTaskWithIdentifier:usingQueue:launchHandler:](<bgtaskscheduler/register(fortaskwithidentifier_using_launchhandler_).md>) — Register a launch handler for the task with the associated identifier that’s executed on the specified queue.
- [- submitTaskRequest:error:](<bgtaskscheduler/submit(__).md>) — Submit a previously registered background task for execution. _(deprecated)_

### Canceling a task

- [- cancelTaskRequestWithIdentifier:](<bgtaskscheduler/cancel(taskrequestwithidentifier_).md>) — Cancel a previously scheduled task request.
- [- cancelAllTaskRequests](<bgtaskscheduler/cancelalltaskrequests().md>) — Cancel all scheduled task requests.

### Getting all scheduled tasks

- [- getPendingTaskRequestsWithCompletionHandler:](<bgtaskscheduler/getpendingtaskrequests(completionhandler_).md>) — Request a list of unexecuted scheduled task requests.

### Handling errors

- [Error](bgtaskscheduler/error.md) — The Errors for the `BGTaskSchedulerError` domain.
- [Code](bgtaskscheduler/error/code.md) — An enumeration of the task scheduling errors.
- [BGTaskSchedulerErrorDomain](bgtaskscheduler/errordomain.md) — The background tasks error domain as a string.

### Instance Methods

- [- submitTaskRequest:completionHandler:](<bgtaskscheduler/submittaskrequest(__completionhandler_).md>) — Submits a background task request to be scheduled with a completion handler. _(beta)_

## See Also

### Essentials

- [Background Tasks updates](../updates/backgroundtasks.md) — Learn about important changes in Background Tasks.
- [BGTask](bgtask.md) — An abstract class for the framework’s tasks.
