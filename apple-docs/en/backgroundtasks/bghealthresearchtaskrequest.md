---
title: BGHealthResearchTaskRequest
framework: Background Tasks
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bghealthresearchtaskrequest
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bghealthresearchtaskrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bghealthresearchtaskrequest.json'
content_hash: 'sha256:78f1a98ebc67edcf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Background Tasks](../backgroundtasks.md)

# BGHealthResearchTaskRequest

<sub>Class</sub>

A request to launch your app in the background to execute processing for a health research study in which a user participates.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class BGHealthResearchTaskRequest
```

## Relationships

- **Inherits From**: [BGProcessingTaskRequest](bgprocessingtaskrequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Setting file permissions

- [protectionTypeOfRequiredData](bghealthresearchtaskrequest/protectiontypeofrequireddata.md) — The file protection required to access health research data relevant to complete the task.

## See Also

### Task requests

- [BGProcessingTaskRequest](bgprocessingtaskrequest.md) — A request to launch your app in the background to execute a processing task that can take minutes to complete.
- [BGAppRefreshTaskRequest](bgapprefreshtaskrequest.md) — A request to launch your app in the background to execute a short refresh task.
- [BGTaskRequest](bgtaskrequest.md) — An abstract class for representing task requests.
- [BGContinuedProcessingTaskRequest](bgcontinuedprocessingtaskrequest.md) — A request for a workload that the system continues processing even if a person backgrounds the app.
