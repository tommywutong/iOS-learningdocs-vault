---
title: BGContinuedProcessingTaskRequest
framework: Background Tasks
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgcontinuedprocessingtaskrequest
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest.json'
content_hash: 'sha256:d64fa7f2863dcb95'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Background Tasks](../backgroundtasks.md)

# BGContinuedProcessingTaskRequest

<sub>Class</sub>

A request for a workload that the system continues processing even if a person backgrounds the app.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class BGContinuedProcessingTaskRequest
```

## Overview

The app submits this request from the foreground. Submission needs to occur as a result of a person’s action, such as tapping a button. The framework begins processing the task immediately, if possible, and the system allows it to continue running even if the app moves to the background.

For more information on Continuous Background Task requests, see [Performing long-running tasks on iOS and iPadOS](performing-long-running-tasks-on-ios-and-ipados.md).

## Relationships

- **Inherits From**: [BGTaskRequest](bgtaskrequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a task request

- [- initWithIdentifier:title:subtitle:](<bgcontinuedprocessingtaskrequest/init(identifier_title_subtitle_).md>) — Creates an instance on behalf of the currently foregrounded app.

### Identifying resource dependencies

- [requiredResources](bgcontinuedprocessingtaskrequest/requiredresources.md) — An option that indicates any special system resources that the task requires.
- [Resources](bgcontinuedprocessingtaskrequest/resources.md) — Options that specify additional system resources a background task needs.

### Choosing a processing strategy

- [strategy](bgcontinuedprocessingtaskrequest/strategy.md) — The submission strategy for the scheduler to abide by.
- [SubmissionStrategy](bgcontinuedprocessingtaskrequest/submissionstrategy.md) — The ways your app suggests the system handle your task’s submission under varying conditions.

### Titling the task

- [subtitle](bgcontinuedprocessingtaskrequest/subtitle.md) — The localized subtitle displayed to a person.
- [title](bgcontinuedprocessingtaskrequest/title.md) — The localized task title displayed to a person.

## See Also

### Task requests

- [BGProcessingTaskRequest](bgprocessingtaskrequest.md) — A request to launch your app in the background to execute a processing task that can take minutes to complete.
- [BGAppRefreshTaskRequest](bgapprefreshtaskrequest.md) — A request to launch your app in the background to execute a short refresh task.
- [BGTaskRequest](bgtaskrequest.md) — An abstract class for representing task requests.
- [BGHealthResearchTaskRequest](bghealthresearchtaskrequest.md) — A request to launch your app in the background to execute processing for a health research study in which a user participates.
