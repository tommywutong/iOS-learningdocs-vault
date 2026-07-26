---
title: BGTaskScheduler.Error.Code.immediateRunIneligible
framework: Background Tasks
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgtaskscheduler/error/code/immediaterunineligible
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/error/code/immediaterunineligible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgtaskscheduler/error/code/immediaterunineligible.json'
content_hash: 'sha256:afcf50f38065a8cb'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Background Tasks](../../../../backgroundtasks.md) · [BGTaskScheduler](../../../bgtaskscheduler.md) · [Error](../../error.md) · [Code](../code.md)

# BGTaskScheduler.Error.Code.immediateRunIneligible

<sub>Case</sub>

A task scheduling error that indicates a task request didn’t run immediately due to system conditions.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case immediateRunIneligible
```

## Discussion

The framework throws this error when a [BGContinuedProcessingTaskRequest](../../../bgcontinuedprocessingtaskrequest.md) that your app submits with [strategy](../../../bgcontinuedprocessingtaskrequest/strategy.md) set to  [BGContinuedProcessingTaskRequestSubmissionStrategyFail](../../../bgcontinuedprocessingtaskrequest/submissionstrategy/fail.md) isn’t able to begin right away due to runtime conditions.

If the task that fails submission is of high importance and your app has other tasks submitted, you can try canceling the other task requests and resubmit the failed request.

## See Also

### Identifying an error

- [BGTaskSchedulerErrorCodeNotPermitted](notpermitted.md) — A task scheduling error that indicates the app isn’t permitted to launch the task.
- [BGTaskSchedulerErrorCodeTooManyPendingTaskRequests](toomanypendingtaskrequests.md) — A task scheduling error that indicates there are too many pending tasks of the type requested.
- [BGTaskSchedulerErrorCodeUnavailable](unavailable.md) — A task scheduling error that indicates the app or extension can’t schedule background work.
