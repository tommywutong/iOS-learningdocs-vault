---
title: AVCaptureDepthDataOutputDelegate
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedepthdataoutputdelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedepthdataoutputdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedepthdataoutputdelegate.json'
content_hash: 'sha256:50237dd327dee5d2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureDepthDataOutputDelegate

<sub>Protocol</sub>

Methods for receiving depth data produced by a depth capture output.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
protocol AVCaptureDepthDataOutputDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Receiving depth data

- [- depthDataOutput:didOutputDepthData:timestamp:connection:](<avcapturedepthdataoutputdelegate/depthdataoutput(__didoutput_timestamp_connection_).md>) — Provides newly captured depth data to the delegate.
- [- depthDataOutput:didDropDepthData:timestamp:connection:reason:](<avcapturedepthdataoutputdelegate/depthdataoutput(__diddrop_timestamp_connection_reason_).md>) — Informs the delegate that captured depth data was not processed.
- [DataDroppedReason](avcaptureoutput/datadroppedreason.md) — Constants that define reasons for why the system dropped a frame.

## See Also

### Receiving captured depth data

- [- setDelegate:callbackQueue:](<avcapturedepthdataoutput/setdelegate(__callbackqueue_).md>) — Designates a delegate object to receive depth data and a dispatch queue for delivering that data.
- [delegate](avcapturedepthdataoutput/delegate.md) — A delegate object that receives depth data.
- [delegateCallbackQueue](avcapturedepthdataoutput/delegatecallbackqueue.md) — A dispatch queue for delivering depth data.
