---
title: Progress.UnpublishingHandler
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progress/unpublishinghandler
source_url: 'https://developer.apple.com/documentation/foundation/progress/unpublishinghandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/unpublishinghandler.json'
content_hash: 'sha256:6645e4d1694ca38c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# Progress.UnpublishingHandler

<sub>Type Alias</sub>

A block that the system calls when an observed progress object terminates the subscription.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias UnpublishingHandler = @Sendable () -> Void
```

## See Also

### Observing and Controlling File Progress by Other Processes

- [+ addSubscriberForFileURL:withPublishingHandler:](<addsubscriber(forfileurl_withpublishinghandler_).md>) — Registers a file URL to hear about the progress of a file operation.
- [+ removeSubscriber:](<removesubscriber(__).md>) — Removes a proxy progress object that the add subscriber method returns.
- [old](isold.md) — A Boolean value that indicates when the observed progress object invokes the publish method before you subscribe to it.
- [PublishingHandler](publishinghandler.md) — A block that the system calls when an observed progress object matches the subscription.
