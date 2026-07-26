---
title: 'resetForReading(timeRanges:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetreaderoutput/randomaccesscontroller/resetforreading(timeranges:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/randomaccesscontroller/resetforreading(timeranges:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderoutput/randomaccesscontroller/resetforreading%28timeranges%3A%29.json'
content_hash: 'sha256:da803a25e0265095'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetReaderOutput](../../avassetreaderoutput.md) · [RandomAccessController](../randomaccesscontroller.md)

# resetForReading(timeRanges:)

<sub>Instance Method</sub>

Starts reading over with a new set of time ranges.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func resetForReading(timeRanges: [CMTimeRange])
```

## Parameters

- `timeRanges` — The time ranges to read

## See Also

### Configuring a controller

- [markConfigurationAsFinal()](<markconfigurationasfinal().md>) — Informs the provider that no more reconfiguration of time ranges is necessary and allows the attached AVAssetReader to advance to `AVAssetReaderStatus/completed`.
