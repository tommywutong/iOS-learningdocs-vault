---
title: delegate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedataoutputsynchronizer/delegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedataoutputsynchronizer/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedataoutputsynchronizer/delegate.json'
content_hash: 'sha256:d3301e9f9163e7f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDataOutputSynchronizer](../avcapturedataoutputsynchronizer.md)

# delegate

<sub>Instance Property</sub>

A delegate object that receives synchronized capture data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var delegate: (any AVCaptureDataOutputSynchronizerDelegate)? { get }
```

## Discussion

This property is read-only. You set the delegate object and the dispatch queue for delegate methods together using the [- setDelegate:queue:](<setdelegate(__queue_).md>) method.

## See Also

### Receiving synchronized capture data

- [- setDelegate:queue:](<setdelegate(__queue_).md>) — Designates a delegate object to receive synchronized data and a dispatch queue for delivering that data.
- [delegateCallbackQueue](delegatecallbackqueue.md) — A dispatch queue for delivering synchronized capture data.
- [AVCaptureDataOutputSynchronizerDelegate](../avcapturedataoutputsynchronizerdelegate.md) — Methods for receiving captured data from multiple capture outputs synchronized to the same timestamp.
