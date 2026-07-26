---
title: BGContinuedProcessingTaskRequest.SubmissionStrategy.fail
framework: Background Tasks
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/submissionstrategy/fail
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/submissionstrategy/fail'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/submissionstrategy/fail.json'
content_hash: 'sha256:faede6ad63661dba'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Background Tasks](../../../backgroundtasks.md) · [BGContinuedProcessingTaskRequest](../../bgcontinuedprocessingtaskrequest.md) · [SubmissionStrategy](../submissionstrategy.md)

# BGContinuedProcessingTaskRequest.SubmissionStrategy.fail

<sub>Case</sub>

An option that fails the submission of a continuous background task if the system can’t run it immediately.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
case fail
```

## Discussion

Task processing might not start right away if the system is currently resource constrainted.

## See Also

### Choosing a strategy

- [BGContinuedProcessingTaskRequestSubmissionStrategyQueue](queue.md) — An option that queues a continuous background task to begin as soon as possible.
