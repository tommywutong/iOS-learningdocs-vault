---
title: 'inputReceiverRequestingMultiPass(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriter/inputreceiverrequestingmultipass(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/inputreceiverrequestingmultipass(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/inputreceiverrequestingmultipass%28for%3A%29.json'
content_hash: 'sha256:8e30ae88dde4ff1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# inputReceiverRequestingMultiPass(for:)

<sub>Instance Method</sub>

Attaches the input to the writer and returns a tuple with an input receiver for writing sample buffers, and an associated multi pass controller.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func inputReceiverRequestingMultiPass(for input: AVAssetWriterInput) -> sending (AVAssetWriterInput.SampleBufferReceiver, AVAssetWriterInput.MultiPassController)
```

## Parameters

- `input` — The input to be attached to the writer.

## Return Value

A tuple with an input receiver for writing sample buffers, and an associated multi pass controller.

## See Also

### Configuring input receivers

- [inputReceiver(for:)](<inputreceiver(for_).md>) — Attaches the input to the writer and returns an input receiver for writing sample buffers.
- [inputCaptionReceiver(for:)](<inputcaptionreceiver(for_).md>) — Attaches the input to the writer and returns an input receiver for writing caption data.
- [inputCaptionReceiverRequestingMultiPass(for:)](<inputcaptionreceiverrequestingmultipass(for_).md>) — Attaches the input to the writer and returns a tuple with an input receiver for writing caption data, and an associated multi pass controller.
- [inputMetadataReceiver(for:)](<inputmetadatareceiver(for_).md>) — Attaches the input to the writer and returns an input receiver for writing timed metadata group.
- [inputMetadataReceiverRequestingMultiPass(for:)](<inputmetadatareceiverrequestingmultipass(for_).md>) — Attaches the input to the writer and returns a tuple with an input receiver for writing timed metadata group, and an associated multi pass controller.
- [inputPixelBufferReceiver(for:pixelBufferAttributes:)](<inputpixelbufferreceiver(for_pixelbufferattributes_).md>) — Attaches the input to the writer and returns an input receiver for writing pixel buffers.
- [inputPixelBufferReceiverRequestingMultiPass(for:pixelBufferAttributes:)](<inputpixelbufferreceiverrequestingmultipass(for_pixelbufferattributes_).md>) — Attaches the input to the writer and returns a tuple with an input receiver for writing pixel buffers, and an associated multi pass controller.
- [inputTaggedPixelBufferGroupReceiver(for:pixelBufferAttributes:)](<inputtaggedpixelbuffergroupreceiver(for_pixelbufferattributes_).md>) — Attaches the input to the writer and returns an input receiver for writing tagged pixel buffers.
- [inputTaggedPixelBufferGroupReceiverRequestingMultiPass(for:pixelBufferAttributes:)](<inputtaggedpixelbuffergroupreceiverrequestingmultipass(for_pixelbufferattributes_).md>) — Attaches the input to the writer and returns a tuple with an input receiver for writing tagged pixel buffers, and an associated multi pass controller.
