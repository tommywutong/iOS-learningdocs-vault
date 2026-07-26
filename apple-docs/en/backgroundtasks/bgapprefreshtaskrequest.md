---
title: BGAppRefreshTaskRequest
framework: Background Tasks
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgapprefreshtaskrequest
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgapprefreshtaskrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgapprefreshtaskrequest.json'
content_hash: 'sha256:10fcf6d0e1dc8b1f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Background Tasks](../backgroundtasks.md)

# BGAppRefreshTaskRequest

<sub>Class</sub>

A request to launch your app in the background to execute a short refresh task.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class BGAppRefreshTaskRequest
```

## Relationships

- **Inherits From**: [BGTaskRequest](bgtaskrequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializing a refresh task request

- [- initWithIdentifier:](<bgapprefreshtaskrequest/init(identifier_).md>) — Return a new refresh task request for the specified identifier.

## See Also

### Task requests

- [BGProcessingTaskRequest](bgprocessingtaskrequest.md) — A request to launch your app in the background to execute a processing task that can take minutes to complete.
- [BGTaskRequest](bgtaskrequest.md) — An abstract class for representing task requests.
- [BGHealthResearchTaskRequest](bghealthresearchtaskrequest.md) — A request to launch your app in the background to execute processing for a health research study in which a user participates.
- [BGContinuedProcessingTaskRequest](bgcontinuedprocessingtaskrequest.md) — A request for a workload that the system continues processing even if a person backgrounds the app.
