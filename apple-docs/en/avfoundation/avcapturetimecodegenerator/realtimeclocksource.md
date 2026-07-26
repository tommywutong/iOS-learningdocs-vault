---
title: realTimeClockSource
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturetimecodegenerator/realtimeclocksource
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/realtimeclocksource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecodegenerator/realtimeclocksource.json'
content_hash: 'sha256:4a0851f9f47d5f1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md)

# realTimeClockSource

<sub>Type Property</sub>

A predefined timecode source synchronized to the real-time system clock.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class var realTimeClockSource: AVCaptureTimecode.Source { get }
```

## Discussion

This class property provides a default timecode source based on the real-time system clock, requiring no external device. It is ideal for live events or scenarios where alignment with the current time of day is necessary.

## See Also

### Managing sources

- [currentSource](currentsource.md) — The active timecode source used by [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md) to maintain clock synchronization for accurate timecode generation.
- [availableSources](availablesources.md) — An array of available timecode synchronization sources that can be used by the timecode generator.
- [frameCountSource](framecountsource.md) — A frame counter timecode source that operates independently of any internal or external synchronization.
- [- startSynchronizationWithTimecodeSource:](<startsynchronization(source_).md>) — Synchronizes the generator with the specified timecode source.
