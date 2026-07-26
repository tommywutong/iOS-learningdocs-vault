---
title: tooManyPendingTaskRequests
framework: Background Tasks
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgtaskscheduler/error/toomanypendingtaskrequests
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/error/toomanypendingtaskrequests'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgtaskscheduler/error/toomanypendingtaskrequests.json'
content_hash: 'sha256:5567ca9ebdd4c42c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Background Tasks](../../../backgroundtasks.md) · [BGTaskScheduler](../../bgtaskscheduler.md) · [Error](../error.md)

# tooManyPendingTaskRequests

<sub>Type Property</sub>

A task scheduling error that indicates there are too many pending tasks of the type requested.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var tooManyPendingTaskRequests: BGTaskScheduler.Error.Code { get }
```

## Discussion

Try canceling some existing task requests and then resubmit the request that failed.

## See Also

### Getting the error codes

- [Code](code.md) — An enumeration of the task scheduling errors.
- [notPermitted](notpermitted.md) — A task scheduling error that indicates the app isn’t permitted to launch the task.
- [unavailable](unavailable.md) — A task scheduling error that indicates the app or extension can’t schedule background work.
