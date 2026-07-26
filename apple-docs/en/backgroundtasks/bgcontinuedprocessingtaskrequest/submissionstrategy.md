---
title: BGContinuedProcessingTaskRequest.SubmissionStrategy
framework: Background Tasks
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/submissionstrategy
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/submissionstrategy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/submissionstrategy.json'
content_hash: 'sha256:987c602abbcecfef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Background Tasks](../../backgroundtasks.md) · [BGContinuedProcessingTaskRequest](../bgcontinuedprocessingtaskrequest.md)

# BGContinuedProcessingTaskRequest.SubmissionStrategy

<sub>Enumeration</sub>

The ways your app suggests the system handle your task’s submission under varying conditions.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
enum SubmissionStrategy
```

## Overview

The Continuous Background Task request ([BGContinuedProcessingTaskRequest](../bgcontinuedprocessingtaskrequest.md)) property [strategy](strategy.md) is of this type.

For more information on submission strategies, see [Performing long-running tasks on iOS and iPadOS](../performing-long-running-tasks-on-ios-and-ipados.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Choosing a strategy

- [BGContinuedProcessingTaskRequestSubmissionStrategyFail](submissionstrategy/fail.md) — An option that fails the submission of a continuous background task if the system can’t run it immediately.
- [BGContinuedProcessingTaskRequestSubmissionStrategyQueue](submissionstrategy/queue.md) — An option that queues a continuous background task to begin as soon as possible.

### Creating a strategy

- [init(rawValue:)](<submissionstrategy/init(rawvalue_).md>) — Creates a submission strategy.

## See Also

### Choosing a processing strategy

- [strategy](strategy.md) — The submission strategy for the scheduler to abide by.
