---
title: AVCaptureMetadataOutputObjectsDelegate
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, macOS 13.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturemetadataoutputobjectsdelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutputobjectsdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemetadataoutputobjectsdelegate.json'
content_hash: 'sha256:7c9c2b0d6a6d7a96'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureMetadataOutputObjectsDelegate

<sub>Protocol</sub>

Methods for receiving metadata produced by a metadata capture output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
protocol AVCaptureMetadataOutputObjectsDelegate : NSObjectProtocol
```

## Overview

The `AVCaptureMetadataOutputObjectsDelegate` protocol must be adopted by the delegate of an [AVCaptureMetadataOutput](avcapturemetadataoutput.md) object. The single method in this protocol is optional. The method allows a delegate to respond when a capture metadata output object receives relevant metadata objects through its connection.

The [AVCaptureMetadataOutput](avcapturemetadataoutput.md) object calls the methods of the delegate object on the dispatch queue associated with its [metadataObjectsCallbackQueue](avcapturemetadataoutput/metadataobjectscallbackqueue.md) property.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Processing emitted metadata objects

- [- captureOutput:didOutputMetadataObjects:fromConnection:](<avcapturemetadataoutputobjectsdelegate/metadataoutput(__didoutput_from_).md>) — Informs the delegate that the capture output object emitted new metadata objects.

## See Also

### Receiving captured metadata objects

- [- setMetadataObjectsDelegate:queue:](<avcapturemetadataoutput/setmetadataobjectsdelegate(__queue_).md>) — Sets the delegate and dispatch queue to use handle callbacks.
- [metadataObjectsDelegate](avcapturemetadataoutput/metadataobjectsdelegate.md) — The delegate of the capture metadata output object.
- [metadataObjectsCallbackQueue](avcapturemetadataoutput/metadataobjectscallbackqueue.md) — The dispatch queue on which to execute the delegate’s methods.
