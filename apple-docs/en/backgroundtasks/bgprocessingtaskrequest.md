---
title: BGProcessingTaskRequest
framework: Background Tasks
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgprocessingtaskrequest
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgprocessingtaskrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgprocessingtaskrequest.json'
content_hash: 'sha256:d10231a7572efb2b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Background Tasks](../backgroundtasks.md)

# BGProcessingTaskRequest

<sub>Class</sub>

A request to launch your app in the background to execute a processing task that can take minutes to complete.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class BGProcessingTaskRequest
```

## Relationships

- **Inherits From**: [BGTaskRequest](bgtaskrequest.md)

- **Inherited By**: [BGHealthResearchTaskRequest](bghealthresearchtaskrequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializing a Processing Task Request

- [- initWithIdentifier:](<bgprocessingtaskrequest/init(identifier_).md>) — Return a new processing task request for the specified identifier.

### Setting Task Request Options

- [requiresExternalPower](bgprocessingtaskrequest/requiresexternalpower.md) — A Boolean specifying if the processing task requires a device connected to power.
- [requiresNetworkConnectivity](bgprocessingtaskrequest/requiresnetworkconnectivity.md) — A Boolean specifying if the processing task requires network connectivity.

## See Also

### Task requests

- [BGAppRefreshTaskRequest](bgapprefreshtaskrequest.md) — A request to launch your app in the background to execute a short refresh task.
- [BGTaskRequest](bgtaskrequest.md) — An abstract class for representing task requests.
- [BGHealthResearchTaskRequest](bghealthresearchtaskrequest.md) — A request to launch your app in the background to execute processing for a health research study in which a user participates.
- [BGContinuedProcessingTaskRequest](bgcontinuedprocessingtaskrequest.md) — A request for a workload that the system continues processing even if a person backgrounds the app.
