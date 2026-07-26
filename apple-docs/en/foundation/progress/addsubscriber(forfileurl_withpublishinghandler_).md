---
title: 'addSubscriber(forFileURL:withPublishingHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.9+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/progress/addsubscriber(forfileurl:withpublishinghandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/progress/addsubscriber(forfileurl:withpublishinghandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/addsubscriber%28forfileurl%3Awithpublishinghandler%3A%29.json'
content_hash: 'sha256:10ba2aa83bb56396'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# addSubscriber(forFileURL:withPublishingHandler:)

<sub>Type Method</sub>

Registers a file URL to hear about the progress of a file operation.

<sub>macOS</sub>

```swift
class func addSubscriber(forFileURL url: URL, withPublishingHandler publishingHandler: @escaping Progress.PublishingHandler) -> Any
```

## Parameters

- `url` — The URL of the file to observe.

- `publishingHandler` — A closure that the system invokes when a progress object that represents a file operation matching the specified URL calls [- publish](<publish().md>).

## Return Value

A proxy of the progress object to observe.

## Discussion

The system invokes the passed-in block when a progress object calls [- publish](<publish().md>) with a [NSProgressFileURLKey](../progressuserinfokey/fileurlkey.md) user info dictionary entry that’s a URL that is the same as this method’s URL, or that is an item that the URL directly contains. The progress object that passes to your block is a proxy of the published progress object. The passed-in block may return another block. If it does, the system invokes the returned block when the observed progress object invokes [- unpublish](<unpublish().md>), the publishing process terminates, or you invoke [+ removeSubscriber:](<removesubscriber(__).md>). The system invokes the blocks you provide on the main thread.

## See Also

### Observing and Controlling File Progress by Other Processes

- [+ removeSubscriber:](<removesubscriber(__).md>) — Removes a proxy progress object that the add subscriber method returns.
- [old](isold.md) — A Boolean value that indicates when the observed progress object invokes the publish method before you subscribe to it.
- [PublishingHandler](publishinghandler.md) — A block that the system calls when an observed progress object matches the subscription.
- [UnpublishingHandler](unpublishinghandler.md) — A block that the system calls when an observed progress object terminates the subscription.
