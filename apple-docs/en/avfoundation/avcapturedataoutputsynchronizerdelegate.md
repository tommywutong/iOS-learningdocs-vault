---
title: AVCaptureDataOutputSynchronizerDelegate
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedataoutputsynchronizerdelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedataoutputsynchronizerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedataoutputsynchronizerdelegate.json'
content_hash: 'sha256:2ae68bebab53a4fb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureDataOutputSynchronizerDelegate

<sub>Protocol</sub>

Methods for receiving captured data from multiple capture outputs synchronized to the same timestamp.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
protocol AVCaptureDataOutputSynchronizerDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Receiving synchronized capture data

- [- dataOutputSynchronizer:didOutputSynchronizedDataCollection:](<avcapturedataoutputsynchronizerdelegate/dataoutputsynchronizer(__didoutput_).md>) — Provides a collection of synchronized capture data to the delegate.

## See Also

### Receiving synchronized capture data

- [- setDelegate:queue:](<avcapturedataoutputsynchronizer/setdelegate(__queue_).md>) — Designates a delegate object to receive synchronized data and a dispatch queue for delivering that data.
- [delegate](avcapturedataoutputsynchronizer/delegate.md) — A delegate object that receives synchronized capture data.
- [delegateCallbackQueue](avcapturedataoutputsynchronizer/delegatecallbackqueue.md) — A dispatch queue for delivering synchronized capture data.
