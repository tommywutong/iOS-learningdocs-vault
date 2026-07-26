---
title: BGContinuedProcessingTaskRequest.SubmissionStrategy.queue
framework: Background Tasks
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/submissionstrategy/queue
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/submissionstrategy/queue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/submissionstrategy/queue.json'
content_hash: 'sha256:5df4077a674ef7d0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Background Tasks](../../../backgroundtasks.md) · [BGContinuedProcessingTaskRequest](../../bgcontinuedprocessingtaskrequest.md) · [SubmissionStrategy](../submissionstrategy.md)

# BGContinuedProcessingTaskRequest.SubmissionStrategy.queue

<sub>Case</sub>

An option that queues a continuous background task to begin as soon as possible.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
case queue
```

## Discussion

This option adds the task request to the back of a queue. The system runs the task as soon as possible. The system might be unable to run a submitted task immediately if the system is currently at the maximum level of concurrent tasks.

> [!important] Important
> The system cancels queued [BGContinuedProcessingTaskRequest](../../bgcontinuedprocessingtaskrequest.md) objects if someone closes your app using the app switcher.

## See Also

### Choosing a strategy

- [BGContinuedProcessingTaskRequestSubmissionStrategyFail](fail.md) — An option that fails the submission of a continuous background task if the system can’t run it immediately.
