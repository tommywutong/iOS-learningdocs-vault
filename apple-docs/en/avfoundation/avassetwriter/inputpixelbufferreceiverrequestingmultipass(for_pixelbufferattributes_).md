---
title: 'inputPixelBufferReceiverRequestingMultiPass(for:pixelBufferAttributes:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriter/inputpixelbufferreceiverrequestingmultipass(for:pixelbufferattributes:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/inputpixelbufferreceiverrequestingmultipass(for:pixelbufferattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/inputpixelbufferreceiverrequestingmultipass%28for%3Apixelbufferattributes%3A%29.json'
content_hash: 'sha256:772107f1f11cb525'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# inputPixelBufferReceiverRequestingMultiPass(for:pixelBufferAttributes:)

<sub>Instance Method</sub>

Attaches the input to the writer and returns a tuple with an input receiver for writing pixel buffers, and an associated multi pass controller.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func inputPixelBufferReceiverRequestingMultiPass(for input: AVAssetWriterInput, pixelBufferAttributes attributes: CVPixelBufferCreationAttributes?) -> sending (AVAssetWriterInput.PixelBufferReceiver, AVAssetWriterInput.MultiPassController)
```

## Parameters

- `input` — The input to be attached to the writer.

- `attributes` — The attributes of pixel buffers that will be vended by the input provider’s pixel buffer pool.

## Return Value

A tuple with an input receiver for writing pixel buffers, and an associated multi pass controller.

## See Also

### Configuring input receivers

- [inputReceiver(for:)](<inputreceiver(for_).md>) — Attaches the input to the writer and returns an input receiver for writing sample buffers.
- [inputCaptionReceiver(for:)](<inputcaptionreceiver(for_).md>) — Attaches the input to the writer and returns an input receiver for writing caption data.
- [inputCaptionReceiverRequestingMultiPass(for:)](<inputcaptionreceiverrequestingmultipass(for_).md>) — Attaches the input to the writer and returns a tuple with an input receiver for writing caption data, and an associated multi pass controller.
- [inputMetadataReceiver(for:)](<inputmetadatareceiver(for_).md>) — Attaches the input to the writer and returns an input receiver for writing timed metadata group.
- [inputMetadataReceiverRequestingMultiPass(for:)](<inputmetadatareceiverrequestingmultipass(for_).md>) — Attaches the input to the writer and returns a tuple with an input receiver for writing timed metadata group, and an associated multi pass controller.
- [inputPixelBufferReceiver(for:pixelBufferAttributes:)](<inputpixelbufferreceiver(for_pixelbufferattributes_).md>) — Attaches the input to the writer and returns an input receiver for writing pixel buffers.
- [inputReceiverRequestingMultiPass(for:)](<inputreceiverrequestingmultipass(for_).md>) — Attaches the input to the writer and returns a tuple with an input receiver for writing sample buffers, and an associated multi pass controller.
- [inputTaggedPixelBufferGroupReceiver(for:pixelBufferAttributes:)](<inputtaggedpixelbuffergroupreceiver(for_pixelbufferattributes_).md>) — Attaches the input to the writer and returns an input receiver for writing tagged pixel buffers.
- [inputTaggedPixelBufferGroupReceiverRequestingMultiPass(for:pixelBufferAttributes:)](<inputtaggedpixelbuffergroupreceiverrequestingmultipass(for_pixelbufferattributes_).md>) — Attaches the input to the writer and returns a tuple with an input receiver for writing tagged pixel buffers, and an associated multi pass controller.
