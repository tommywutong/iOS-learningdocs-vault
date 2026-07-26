---
title: delegateCallbackQueue
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedepthdataoutput/delegatecallbackqueue
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedepthdataoutput/delegatecallbackqueue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedepthdataoutput/delegatecallbackqueue.json'
content_hash: 'sha256:39519bc2eda3d114'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDepthDataOutput](../avcapturedepthdataoutput.md)

# delegateCallbackQueue

<sub>Instance Property</sub>

A dispatch queue for delivering depth data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var delegateCallbackQueue: dispatch_queue_t? { get }
```

## Discussion

This property is read-only. You set the delegate object and the dispatch queue for calling delegate methods together using the [- setDelegate:callbackQueue:](<setdelegate(__callbackqueue_).md>) method.

## See Also

### Receiving captured depth data

- [- setDelegate:callbackQueue:](<setdelegate(__callbackqueue_).md>) — Designates a delegate object to receive depth data and a dispatch queue for delivering that data.
- [delegate](delegate.md) — A delegate object that receives depth data.
- [AVCaptureDepthDataOutputDelegate](../avcapturedepthdataoutputdelegate.md) — Methods for receiving depth data produced by a depth capture output.
