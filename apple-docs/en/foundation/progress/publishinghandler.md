---
title: Progress.PublishingHandler
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progress/publishinghandler
source_url: 'https://developer.apple.com/documentation/foundation/progress/publishinghandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/publishinghandler.json'
content_hash: 'sha256:d9647f9769f55806'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# Progress.PublishingHandler

<sub>Type Alias</sub>

A block that the system calls when an observed progress object matches the subscription.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias PublishingHandler = @Sendable (Progress) -> Progress.UnpublishingHandler?
```

## Parameters

- `progress` — The proxy to the observed progress object.

## Return Value

An optional block that the system invokes when the observed progress object invokes [- unpublish](<unpublish().md>), the publishing process terminates, or you invoke [+ removeSubscriber:](<removesubscriber(__).md>).

## See Also

### Observing and Controlling File Progress by Other Processes

- [+ addSubscriberForFileURL:withPublishingHandler:](<addsubscriber(forfileurl_withpublishinghandler_).md>) — Registers a file URL to hear about the progress of a file operation.
- [+ removeSubscriber:](<removesubscriber(__).md>) — Removes a proxy progress object that the add subscriber method returns.
- [old](isold.md) — A Boolean value that indicates when the observed progress object invokes the publish method before you subscribe to it.
- [UnpublishingHandler](unpublishinghandler.md) — A block that the system calls when an observed progress object terminates the subscription.
