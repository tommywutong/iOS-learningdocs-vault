---
title: metadata
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureaudiofileoutput/metadata
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureaudiofileoutput/metadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureaudiofileoutput/metadata.json'
content_hash: 'sha256:e10aeab0ae5bf1f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureAudioFileOutput](../avcaptureaudiofileoutput.md)

# metadata

<sub>Instance Property</sub>

A collection of metadata to be written to the receiver’s output files.

<sub>macOS</sub>

```swift
var metadata: [AVMetadataItem] { get set }
```

## Discussion

The value of this property is an array of `AVMetadataItem` objects representing the collection of top-level metadata to be written in each output file. Only ID3 v2.2, v2.3, or v2.4 style metadata items are supported.

## See Also

### Configuring output

- [audioSettings](audiosettings.md) — The settings used to decode or re-encode audio before it is output by the receiver.
