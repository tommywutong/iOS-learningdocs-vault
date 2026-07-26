---
title: BGTaskRequest
framework: Background Tasks
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgtaskrequest
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgtaskrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgtaskrequest.json'
content_hash: 'sha256:d52272cee7a42c1d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Background Tasks](../backgroundtasks.md)

# BGTaskRequest

<sub>Class</sub>

An abstract class for representing task requests.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class BGTaskRequest
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [BGAppRefreshTaskRequest](bgapprefreshtaskrequest.md), [BGContinuedProcessingTaskRequest](bgcontinuedprocessingtaskrequest.md), [BGProcessingTaskRequest](bgprocessingtaskrequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring a Task Request

- [earliestBeginDate](bgtaskrequest/earliestbegindate.md) — The earliest date and time at which to run the task.
- [identifier](bgtaskrequest/identifier.md) — The identifier of the task associated with the request.

## See Also

### Task requests

- [BGProcessingTaskRequest](bgprocessingtaskrequest.md) — A request to launch your app in the background to execute a processing task that can take minutes to complete.
- [BGAppRefreshTaskRequest](bgapprefreshtaskrequest.md) — A request to launch your app in the background to execute a short refresh task.
- [BGHealthResearchTaskRequest](bghealthresearchtaskrequest.md) — A request to launch your app in the background to execute processing for a health research study in which a user participates.
- [BGContinuedProcessingTaskRequest](bgcontinuedprocessingtaskrequest.md) — A request for a workload that the system continues processing even if a person backgrounds the app.
