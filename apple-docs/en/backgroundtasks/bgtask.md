---
title: BGTask
framework: Background Tasks
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgtask
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgtask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgtask.json'
content_hash: 'sha256:0b22b736e1c86467'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Background Tasks](../backgroundtasks.md)

# BGTask

<sub>Class</sub>

An abstract class for the framework’s tasks.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class BGTask
```

## Overview

With the exception of [BGContinuedProcessingTask](bgcontinuedprocessingtask.md), which your app executes in the foreground, the system executes [BGTask](bgtask.md) subclasses on behalf of your app, while your app is in the background.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [BGAppRefreshTask](bgapprefreshtask.md), [BGContinuedProcessingTask](bgcontinuedprocessingtask.md), [BGProcessingTask](bgprocessingtask.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Reading Task Information

- [identifier](bgtask/identifier.md) — The string identifier of the task.

### Configuring a Task

- [expirationHandler](bgtask/expirationhandler.md) — A handler called shortly before the task’s background time expires.
- [- setTaskCompletedWithSuccess:](<bgtask/settaskcompleted(success_).md>) — Informs the background task scheduler that the task is complete.

## See Also

### Essentials

- [Background Tasks updates](../updates/backgroundtasks.md) — Learn about important changes in Background Tasks.
- [BGTaskScheduler](bgtaskscheduler.md) — A class for scheduling tasks that add background support to your app’s most critical work.
