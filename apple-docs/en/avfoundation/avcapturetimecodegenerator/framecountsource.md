---
title: frameCountSource
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturetimecodegenerator/framecountsource
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/framecountsource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecodegenerator/framecountsource.json'
content_hash: 'sha256:bc329d7882c52983'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md)

# frameCountSource

<sub>Type Property</sub>

A frame counter timecode source that operates independently of any internal or external synchronization.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class var frameCountSource: AVCaptureTimecode.Source { get }
```

## Discussion

This class property represents a standalone timecode source that advances based purely on frame count, independent of any real-time or external synchronization. It is ideal for scenarios where a simple, self-contained timing reference is sufficient, without requiring alignment to system clocks or external devices.

## See Also

### Managing sources

- [currentSource](currentsource.md) — The active timecode source used by [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md) to maintain clock synchronization for accurate timecode generation.
- [availableSources](availablesources.md) — An array of available timecode synchronization sources that can be used by the timecode generator.
- [realTimeClockSource](realtimeclocksource.md) — A predefined timecode source synchronized to the real-time system clock.
- [- startSynchronizationWithTimecodeSource:](<startsynchronization(source_).md>) — Synchronizes the generator with the specified timecode source.
