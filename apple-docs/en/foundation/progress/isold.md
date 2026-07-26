---
title: isOld
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.9+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progress/isold
source_url: 'https://developer.apple.com/documentation/foundation/progress/isold'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/isold.json'
content_hash: 'sha256:f18b6e6fdb40689c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# isOld

<sub>Instance Property</sub>

A Boolean value that indicates when the observed progress object invokes the publish method before you subscribe to it.

<sub>macOS</sub>

```swift
var isOld: Bool { get }
```

## Discussion

The publish and subscribe mechanism is generally _level-triggered_, in that when you invoke [+ addSubscriberForFileURL:withPublishingHandler:](<addsubscriber(forfileurl_withpublishinghandler_).md>), the system invokes your block for every relevant published and unpublished progress object. Sometimes you need to implement _edge-triggered_ behavior, in which you do something either exactly when new progress begins or not at all.

In the example above, the Dock doesn’t animate file icons when this method returns [true](../../swift/true.md).

There’s no reliable definition of _before_ in this case, which involves multiple processes in a preemptively scheduled system. Don’t use this method for anything more important than best efforts at animating. It can be inaccurate due to processes coming and going from unpredictable user actions.

## See Also

### Observing and Controlling File Progress by Other Processes

- [+ addSubscriberForFileURL:withPublishingHandler:](<addsubscriber(forfileurl_withpublishinghandler_).md>) — Registers a file URL to hear about the progress of a file operation.
- [+ removeSubscriber:](<removesubscriber(__).md>) — Removes a proxy progress object that the add subscriber method returns.
- [PublishingHandler](publishinghandler.md) — A block that the system calls when an observed progress object matches the subscription.
- [UnpublishingHandler](unpublishinghandler.md) — A block that the system calls when an observed progress object terminates the subscription.
