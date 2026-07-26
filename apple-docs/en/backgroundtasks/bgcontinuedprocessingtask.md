---
title: BGContinuedProcessingTask
framework: Background Tasks
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgcontinuedprocessingtask
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgcontinuedprocessingtask.json'
content_hash: 'sha256:cf479539658fa20c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Background Tasks](../backgroundtasks.md)

# BGContinuedProcessingTask

<sub>Class</sub>

A task that starts in the foreground and can continue running in the background as needed.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class BGContinuedProcessingTask
```

## Overview

This task works with [BGContinuedProcessingTaskRequest](bgcontinuedprocessingtaskrequest.md).

The system displays the progress of this task in a Live Activity and a person can cancel it through the interface if they wish.

The system can terminate a continuous background task abruptly depending on run-time conditions, for example, under resource constraints. Your implementation needs to report progress using the [ProgressReporting](../foundation/progressreporting.md) protocol that this task conforms to. The system prioritizes the termination of tasks that reflect minimal or no progress, when resources become constrained.

For more information on Continuous Background Task requests, see [Performing long-running tasks on iOS and iPadOS](performing-long-running-tasks-on-ios-and-ipados.md).

## Relationships

- **Inherits From**: [BGTask](bgtask.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [ProgressReporting](../foundation/progressreporting.md)

## Topics

### Titling the task

- [title](bgcontinuedprocessingtask/title.md) — The localized title displayed to a person.
- [subtitle](bgcontinuedprocessingtask/subtitle.md) — The localized subtitle displayed to a person.
- [- updateTitle:subtitle:](<bgcontinuedprocessingtask/updatetitle(__subtitle_).md>) — Update the task title and subtitle that the system displays to a person.

## See Also

### Foreground tasks with background support

- [Performing long-running tasks on iOS and iPadOS](performing-long-running-tasks-on-ios-and-ipados.md) — Use a continuous background task to do work that can complete as needed.
- [Background GPU Access](../bundleresources/entitlements/com.apple.developer.background-tasks.continued-processing.gpu.md) — The entitlement the system requires for a continuous background task to use the GPU.
