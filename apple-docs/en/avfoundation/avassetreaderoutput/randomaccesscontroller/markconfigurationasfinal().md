---
title: markConfigurationAsFinal()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreaderoutput/randomaccesscontroller/markconfigurationasfinal()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/randomaccesscontroller/markconfigurationasfinal()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderoutput/randomaccesscontroller/markconfigurationasfinal%28%29.json'
content_hash: 'sha256:aefa26ac673ba2c5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetReaderOutput](../../avassetreaderoutput.md) · [RandomAccessController](../randomaccesscontroller.md)

# markConfigurationAsFinal()

<sub>Instance Method</sub>

Informs the provider that no more reconfiguration of time ranges is necessary and allows the attached AVAssetReader to advance to `AVAssetReaderStatus/completed`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func markConfigurationAsFinal()
```

## See Also

### Configuring a controller

- [resetForReading(timeRanges:)](<resetforreading(timeranges_).md>) — Starts reading over with a new set of time ranges.
