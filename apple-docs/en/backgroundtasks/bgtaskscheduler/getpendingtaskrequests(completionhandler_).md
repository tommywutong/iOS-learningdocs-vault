---
title: 'getPendingTaskRequests(completionHandler:)'
framework: Background Tasks
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/backgroundtasks/bgtaskscheduler/getpendingtaskrequests(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/getpendingtaskrequests(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgtaskscheduler/getpendingtaskrequests%28completionhandler%3A%29.json'
content_hash: 'sha256:233485942fbe8cf8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Background Tasks](../../backgroundtasks.md) · [BGTaskScheduler](../bgtaskscheduler.md)

# getPendingTaskRequests(completionHandler:)

<sub>Instance Method</sub>

Request a list of unexecuted scheduled task requests.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func getPendingTaskRequests(completionHandler: @escaping @Sendable ([BGTaskRequest]) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func pendingTaskRequests() async -> [BGTaskRequest]
```

## Parameters

- `completionHandler` — The completion handler called with the pending tasks. The handler may execute on a background thread. The handler takes a single parameter `tasksRequests`, an array of `BGTaskRequest` objects. The array is empty if there are no scheduled tasks. The objects passed in the array are copies of the existing requests. Changing the attributes of a request has no effect. To change the attributes submit a new task request using [- submitTaskRequest:error:](<submit(__).md>).

## Discussion

> [!note] Concurrency note
> You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func pendingTaskRequests() async -> [BGTaskRequest]
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../swift/calling-objective-c-apis-asynchronously.md).
