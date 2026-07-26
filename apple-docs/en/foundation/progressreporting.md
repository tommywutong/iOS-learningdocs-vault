---
title: ProgressReporting
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progressreporting
source_url: 'https://developer.apple.com/documentation/foundation/progressreporting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressreporting.json'
content_hash: 'sha256:6ef71045ea9d6ac0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# ProgressReporting

<sub>Protocol</sub>

An interface for objects that report progress using a single progress instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol ProgressReporting : NSObjectProtocol
```

## Overview

Create the returned progress object using [ProgressReporting](progressreporting.md). The resulting object has no parent allowing the caller to add it to a progress tree using [ProgressReporting](progressreporting.md).

You can return a single progress object or a progress tree. If you are creating a progress tree, add the children to the returned progress object as described in [Reporting Progress for Multiple Operations](progress.md#Reporting-Progress-for-Multiple-Operations).

You are responsible for setting and updating the [ProgressReporting](progressreporting.md) of any [Progress](progress.md) object you create.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [NSBundleResourceRequest](nsbundleresourcerequest.md), [OperationQueue](operationqueue.md), [URLSessionDataTask](urlsessiondatatask.md), [URLSessionDownloadTask](urlsessiondownloadtask.md), [URLSessionStreamTask](urlsessionstreamtask.md), [URLSessionTask](urlsessiontask.md), [URLSessionUploadTask](urlsessionuploadtask.md), [URLSessionWebSocketTask](urlsessionwebsockettask.md)

## Topics

### Custom Class Progress

- [progress](progressreporting/progress.md) — The progress object returned by the class.

## See Also

### Progress

- [Progress](progress.md) — An object that conveys ongoing progress to the user for a specified task.
