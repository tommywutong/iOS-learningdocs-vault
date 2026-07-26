---
title: availableSources
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturetimecodegenerator/availablesources
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/availablesources'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecodegenerator/availablesources.json'
content_hash: 'sha256:e3926d1d69cbf41b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md)

# availableSources

<sub>Instance Property</sub>

An array of available timecode synchronization sources that can be used by the timecode generator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var availableSources: [AVCaptureTimecode.Source] { get }
```

## Return Value

A read-only array of [Source](../avcapturetimecode/source.md) objects representing the available timecode synchronization sources.

## Discussion

This property provides a list of [Source](../avcapturetimecode/source.md) objects representing the available timecode sources with which the generator can synchronize. The sources may include built-in options such as the frame counter and real-time clock, as well as dynamically detected sources such as connected MIDI or HID devices.

This array is key-value observable, allowing you to monitor changes in real-time. For example, when a new MIDI device is connected, the array is updated to include the corresponding timecode source.

## See Also

### Managing sources

- [currentSource](currentsource.md) — The active timecode source used by [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md) to maintain clock synchronization for accurate timecode generation.
- [frameCountSource](framecountsource.md) — A frame counter timecode source that operates independently of any internal or external synchronization.
- [realTimeClockSource](realtimeclocksource.md) — A predefined timecode source synchronized to the real-time system clock.
- [- startSynchronizationWithTimecodeSource:](<startsynchronization(source_).md>) — Synchronizes the generator with the specified timecode source.
