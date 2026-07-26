---
title: strategy
framework: Background Tasks
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/strategy
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/strategy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/strategy.json'
content_hash: 'sha256:7570f460b45504a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Background Tasks](../../backgroundtasks.md) · [BGContinuedProcessingTaskRequest](../bgcontinuedprocessingtaskrequest.md)

# strategy

<sub>Instance Property</sub>

The submission strategy for the scheduler to abide by.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var strategy: BGContinuedProcessingTaskRequest.SubmissionStrategy { get set }
```

## Discussion

The default value is [BGContinuedProcessingTaskRequestSubmissionStrategyQueue](submissionstrategy/queue.md).

## See Also

### Choosing a processing strategy

- [SubmissionStrategy](submissionstrategy.md) — The ways your app suggests the system handle your task’s submission under varying conditions.
