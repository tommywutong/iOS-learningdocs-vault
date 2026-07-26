---
title: 'removeSubscriber(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.9+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/progress/removesubscriber(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/progress/removesubscriber(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/removesubscriber%28_%3A%29.json'
content_hash: 'sha256:05e06b3344592b01'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# removeSubscriber(_:)

<sub>Type Method</sub>

Removes a proxy progress object that the add subscriber method returns.

<sub>macOS</sub>

```swift
class func removeSubscriber(_ subscriber: Any)
```

## Parameters

- `subscriber` — The proxy of the progress object to observe.

## Discussion

If the block for [+ addSubscriberForFileURL:withPublishingHandler:](<addsubscriber(forfileurl_withpublishinghandler_).md>) returns a closure, the system invokes that closure on the main thread when you invoke [+ removeSubscriber:](<removesubscriber(__).md>).

## See Also

### Observing and Controlling File Progress by Other Processes

- [+ addSubscriberForFileURL:withPublishingHandler:](<addsubscriber(forfileurl_withpublishinghandler_).md>) — Registers a file URL to hear about the progress of a file operation.
- [old](isold.md) — A Boolean value that indicates when the observed progress object invokes the publish method before you subscribe to it.
- [PublishingHandler](publishinghandler.md) — A block that the system calls when an observed progress object matches the subscription.
- [UnpublishingHandler](unpublishinghandler.md) — A block that the system calls when an observed progress object terminates the subscription.
