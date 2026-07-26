---
title: BGTaskScheduler.Error.Code.tooManyPendingTaskRequests
framework: Background Tasks
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgtaskscheduler/error/code/toomanypendingtaskrequests
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/error/code/toomanypendingtaskrequests'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgtaskscheduler/error/code/toomanypendingtaskrequests.json'
content_hash: 'sha256:52b9a401758f75b3'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Background Tasks](../../../../backgroundtasks.md) · [BGTaskScheduler](../../../bgtaskscheduler.md) · [Error](../../error.md) · [Code](../code.md)

# BGTaskScheduler.Error.Code.tooManyPendingTaskRequests

<sub>Case</sub>

A task scheduling error that indicates there are too many pending tasks of the type requested.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case tooManyPendingTaskRequests
```

## Discussion

Try canceling some existing task requests and then resubmit the request that failed.

## See Also

### Identifying an error

- [BGTaskSchedulerErrorCodeNotPermitted](notpermitted.md) — A task scheduling error that indicates the app isn’t permitted to launch the task.
- [BGTaskSchedulerErrorCodeUnavailable](unavailable.md) — A task scheduling error that indicates the app or extension can’t schedule background work.
- [BGTaskSchedulerErrorCodeImmediateRunIneligible](immediaterunineligible.md) — A task scheduling error that indicates a task request didn’t run immediately due to system conditions.
