---
title: 'register(forTaskWithIdentifier:using:launchHandler:)'
framework: Background Tasks
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/backgroundtasks/bgtaskscheduler/register(fortaskwithidentifier:using:launchhandler:)'
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/register(fortaskwithidentifier:using:launchhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgtaskscheduler/register%28fortaskwithidentifier%3Ausing%3Alaunchhandler%3A%29.json'
content_hash: 'sha256:69e41eaf58d1496d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Background Tasks](../../backgroundtasks.md) · [BGTaskScheduler](../bgtaskscheduler.md)

# register(forTaskWithIdentifier:using:launchHandler:)

<sub>Instance Method</sub>

Register a launch handler for the task with the associated identifier that’s executed on the specified queue.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func register(forTaskWithIdentifier identifier: String, using queue: dispatch_queue_t?, launchHandler: @escaping (BGTask) -> Void) -> Bool
```

## Parameters

- `identifier` — A string containing the identifier of the task.

- `queue` — A queue for executing the task. Pass `nil` to use a default background queue.

- `launchHandler` — The system runs the block of code for the launch handler when it launches the app in the background. The block takes a single parameter, a [BGTask](../bgtask.md) object used for assigning an expiration handler and for setting a completion status. The block has no return value.

## Return value

Returns [true](../../swift/true.md) if the launch handler was registered. Returns [false](../../swift/false.md) if the identifier isn’t included in the [BGTaskSchedulerPermittedIdentifiers](../../bundleresources/information-property-list/bgtaskschedulerpermittedidentifiers.md) `Info.plist`.

## Discussion

Every identifier in the [BGTaskSchedulerPermittedIdentifiers](../../bundleresources/information-property-list/bgtaskschedulerpermittedidentifiers.md) requires a handler. Registration of all launch handlers must be complete before the end of [applicationDidFinishLaunching(_:)](<../../uikit/uiapplicationdelegate/applicationdidfinishlaunching(__).md>).

> [!important] Important
> Register each task identifier only once. The system kills the app on the second registration of the same task identifier.

## See Also

### Scheduling a task

- [- submitTaskRequest:error:](<submit(__).md>) — Submit a previously registered background task for execution. _(deprecated)_
