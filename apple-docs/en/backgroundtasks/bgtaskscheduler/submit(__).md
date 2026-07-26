---
title: 'submit(_:)'
framework: Background Tasks
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/backgroundtasks/bgtaskscheduler/submit(_:)'
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/submit(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgtaskscheduler/submit%28_%3A%29.json'
content_hash: 'sha256:061d93d6d729cdc3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Background Tasks](../../backgroundtasks.md) · [BGTaskScheduler](../bgtaskscheduler.md)

# submit(_:)

<sub>Instance Method</sub>

Submit a previously registered background task for execution.

> [!warning] Deprecated
> Use submitTaskRequest:completionHandler: instead to capture all error conditions

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func submit(_ taskRequest: BGTaskRequest) throws
```

## Parameters

- `taskRequest` — A background task request object specifying the task identifier and optional configuration information.

## Discussion

Submitting a task request for an unexecuted task that’s already in the queue replaces the previous task request.

There can be a total of 1 refresh task and 10 processing tasks scheduled at any time. Trying to schedule more tasks returns [BGTaskSchedulerErrorCodeTooManyPendingTaskRequests](error/code/toomanypendingtaskrequests.md).

## See Also

### Scheduling a task

- [- registerForTaskWithIdentifier:usingQueue:launchHandler:](<register(fortaskwithidentifier_using_launchhandler_).md>) — Register a launch handler for the task with the associated identifier that’s executed on the specified queue.
