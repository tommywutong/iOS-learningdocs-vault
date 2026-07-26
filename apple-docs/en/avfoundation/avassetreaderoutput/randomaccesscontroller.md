---
title: AVAssetReaderOutput.RandomAccessController
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreaderoutput/randomaccesscontroller
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/randomaccesscontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderoutput/randomaccesscontroller.json'
content_hash: 'sha256:16e5c4692d52f942'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderOutput](../avassetreaderoutput.md)

# AVAssetReaderOutput.RandomAccessController

<sub>Class</sub>

Object used to reset an output provider to read specified time ranges.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class RandomAccessController
```

## Topics

### Configuring a controller

- [markConfigurationAsFinal()](<randomaccesscontroller/markconfigurationasfinal().md>) — Informs the provider that no more reconfiguration of time ranges is necessary and allows the attached AVAssetReader to advance to `AVAssetReaderStatus/completed`.
- [resetForReading(timeRanges:)](<randomaccesscontroller/resetforreading(timeranges_).md>) — Starts reading over with a new set of time ranges.

## See Also

### Copying sample buffers

- [- copyNextSampleBuffer](<copynextsamplebuffer().md>) — Copies the next sample buffer from the output. _(deprecated)_
- [Provider](provider.md) — An object that reads a collection of samples of a common media type from an asset reader.
- [SupportedPayload](supportedpayload.md)
