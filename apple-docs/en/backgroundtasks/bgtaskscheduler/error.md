---
title: BGTaskScheduler.Error
framework: Background Tasks
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgtaskscheduler/error
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgtaskscheduler/error.json'
content_hash: 'sha256:e62d8350178da564'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Background Tasks](../../backgroundtasks.md) · [BGTaskScheduler](../bgtaskscheduler.md)

# BGTaskScheduler.Error

<sub>Structure</sub>

The Errors for the `BGTaskSchedulerError` domain.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct Error
```

## Relationships

- **Conforms To**: [CustomNSError](../../foundation/customnserror.md), [Equatable](../../swift/equatable.md), [Error](../../swift/error.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting the error codes

- [Code](error/code.md) — An enumeration of the task scheduling errors.
- [notPermitted](error/notpermitted.md) — A task scheduling error that indicates the app isn’t permitted to launch the task.
- [tooManyPendingTaskRequests](error/toomanypendingtaskrequests.md) — A task scheduling error that indicates there are too many pending tasks of the type requested.
- [unavailable](error/unavailable.md) — A task scheduling error that indicates the app or extension can’t schedule background work.

### Getting the error domain

- [errorDomain](error/errordomain.md) — The background tasks error domain as a string.

### Type Properties

- [immediateRunIneligible](error/immediaterunineligible.md)

## See Also

### Handling errors

- [Code](error/code.md) — An enumeration of the task scheduling errors.
- [BGTaskSchedulerErrorDomain](errordomain.md) — The background tasks error domain as a string.
