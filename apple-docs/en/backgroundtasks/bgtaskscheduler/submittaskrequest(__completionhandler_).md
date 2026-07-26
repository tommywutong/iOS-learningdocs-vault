---
title: 'submitTaskRequest(_:completionHandler:)'
framework: Background Tasks
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/backgroundtasks/bgtaskscheduler/submittaskrequest(_:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/submittaskrequest(_:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgtaskscheduler/submittaskrequest%28_%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:652519e30d4ce059'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Background Tasks](../../backgroundtasks.md) · [BGTaskScheduler](../bgtaskscheduler.md)

# submitTaskRequest(_:completionHandler:)

<sub>Instance Method</sub>

Submits a background task request to be scheduled with a completion handler.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func submitTaskRequest(_ taskRequest: BGTaskRequest, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func submitTaskRequest(_ taskRequest: BGTaskRequest) async throws
```

## Parameters

- `taskRequest` — The task request object representing the parameters of the background task to be scheduled.

- `completionHandler` — A block that is called when submission completes. The block receives an optional error parameter: - `nil` if the task was submitted successfully - An `NSError` if submission failed

## Discussion

This method asynchronously submits the task request and invokes the completion handler with any errors that occur during submission.

Submitting a task request for an unexecuted task that’s already in the queue replaces the previous task request.

There can be a total of 1 refresh task and 10 processing tasks scheduled at any time. Trying to schedule more tasks will result in an error with code [BGTaskSchedulerErrorCodeTooManyPendingTaskRequests](error/code/toomanypendingtaskrequests.md).

Common errors include:

- [BGTaskSchedulerErrorCodeNotPermitted](error/code/notpermitted.md): Task identifier not permitted or unsupported resources requested
- [BGTaskSchedulerErrorCodeTooManyPendingTaskRequests](error/code/toomanypendingtaskrequests.md): Too many pending tasks of this type
- [BGTaskSchedulerErrorCodeUnavailable](error/code/unavailable.md): Background refresh disabled or app not permitted
- [BGTaskSchedulerErrorCodeImmediateRunIneligible](error/code/immediaterunineligible.md): Immediate run not eligible due to system conditions

The completion handler is called on an arbitrary queue.

> [!note] Note
> The completion handler may be invoked on a arbitrary queue after an arbitrary amount of delay. Do not call this method from the main thread or performance-critical contexts.

This method replaces the deprecated [- submitTaskRequest:error:](<submit(__).md>) method
