---
title: BGTaskScheduler.Error.Code
framework: Background Tasks
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgtaskscheduler/error/code
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/error/code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgtaskscheduler/error/code.json'
content_hash: 'sha256:b48cbd6e57b32601'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Background Tasks](../../../backgroundtasks.md) · [BGTaskScheduler](../../bgtaskscheduler.md) · [Error](../error.md)

# BGTaskScheduler.Error.Code

<sub>Enumeration</sub>

An enumeration of the task scheduling errors.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum Code
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../../swift/bitwisecopyable.md), [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [RawRepresentable](../../../swift/rawrepresentable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Identifying an error

- [BGTaskSchedulerErrorCodeNotPermitted](code/notpermitted.md) — A task scheduling error that indicates the app isn’t permitted to launch the task.
- [BGTaskSchedulerErrorCodeTooManyPendingTaskRequests](code/toomanypendingtaskrequests.md) — A task scheduling error that indicates there are too many pending tasks of the type requested.
- [BGTaskSchedulerErrorCodeUnavailable](code/unavailable.md) — A task scheduling error that indicates the app or extension can’t schedule background work.
- [BGTaskSchedulerErrorCodeImmediateRunIneligible](code/immediaterunineligible.md) — A task scheduling error that indicates a task request didn’t run immediately due to system conditions.

### Initializers

- [init(rawValue:)](<code/init(rawvalue_).md>)

## See Also

### Handling errors

- [Error](../error.md) — The Errors for the `BGTaskSchedulerError` domain.
- [BGTaskSchedulerErrorDomain](../errordomain.md) — The background tasks error domain as a string.
