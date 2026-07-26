---
title: type
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturetimecode/source/type
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecode/source/type'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecode/source/type.json'
content_hash: 'sha256:d91d5199a5825a34'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureTimecode](../../avcapturetimecode.md) · [Source](../source.md)

# type

<sub>Instance Property</sub>

The type of timecode source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var type: AVCaptureTimecode.SourceType { get }
```

## Discussion

Indicates the type of timecode source, represented as a value from the `AVCaptureTimecodeSynchronizationSourceType` enum. This helps you identify the source for specific synchronization use cases, such as frame counter, real-time clock, MIDI, or HID.

## See Also

### Inspecting the source

- [displayName](displayname.md) — The name of the timecode source.
- [uuid](uuid.md) — A unique identifier for the timecode source.
