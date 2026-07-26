---
title: feedbackQueue
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4commandqueuedescriptor/feedbackqueue
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandqueuedescriptor/feedbackqueue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandqueuedescriptor/feedbackqueue.json'
content_hash: 'sha256:2e7eb56fe6241300'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandQueueDescriptor](../mtl4commandqueuedescriptor.md)

# feedbackQueue

<sub>Instance Property</sub>

Assigns a dispatch queue to which Metal submits feedback notification blocks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
unowned(unsafe) var feedbackQueue: dispatch_queue_t? { get set }
```

## Discussion

When you assign a dispatch queue via this method, Metal requires that the queue parameter you provide is a serial queue.

If you set the value of property to `nil`, the default, Metal allocates an internal dispatch queue to service feedback notifications.
