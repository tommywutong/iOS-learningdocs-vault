---
title: 'startSynchronization(source:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturetimecodegenerator/startsynchronization(source:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/startsynchronization(source:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecodegenerator/startsynchronization%28source%3A%29.json'
content_hash: 'sha256:79aa3f6c8afe25eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md)

# startSynchronization(source:)

<sub>Instance Method</sub>

Synchronizes the generator with the specified timecode source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func startSynchronization(source: AVCaptureTimecode.Source)
```

## Parameters

- `source` — The timecode source for synchronization.

## See Also

### Managing sources

- [currentSource](currentsource.md) — The active timecode source used by [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md) to maintain clock synchronization for accurate timecode generation.
- [availableSources](availablesources.md) — An array of available timecode synchronization sources that can be used by the timecode generator.
- [frameCountSource](framecountsource.md) — A frame counter timecode source that operates independently of any internal or external synchronization.
- [realTimeClockSource](realtimeclocksource.md) — A predefined timecode source synchronized to the real-time system clock.
