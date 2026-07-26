---
title: currentSource
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturetimecodegenerator/currentsource
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/currentsource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecodegenerator/currentsource.json'
content_hash: 'sha256:c7de8b5182bb576a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md)

# currentSource

<sub>Instance Property</sub>

The active timecode source used by [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md) to maintain clock synchronization for accurate timecode generation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var currentSource: AVCaptureTimecode.Source { get }
```

## Discussion

Indicates the active timecode source, as defined in the `AVCaptureTimecodeSynchronizationSourceType` enum. If an [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md) becomes disconnected from its source, it continues generating timecodes using historical data from its ring buffer. This approach allows the generator to maintain synchronization during brief disruptions, as is common in cinema workflows where timecode signals may experience discontinuities.

## See Also

### Managing sources

- [availableSources](availablesources.md) — An array of available timecode synchronization sources that can be used by the timecode generator.
- [frameCountSource](framecountsource.md) — A frame counter timecode source that operates independently of any internal or external synchronization.
- [realTimeClockSource](realtimeclocksource.md) — A predefined timecode source synchronized to the real-time system clock.
- [- startSynchronizationWithTimecodeSource:](<startsynchronization(source_).md>) — Synchronizes the generator with the specified timecode source.
