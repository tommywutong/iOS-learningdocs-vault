---
title: AVCaptureTimecode.SourceType.external
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturetimecode/sourcetype-swift.enum/external
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecode/sourcetype-swift.enum/external'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecode/sourcetype-swift.enum/external.json'
content_hash: 'sha256:9b5cd439583282b6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureTimecode](../../avcapturetimecode.md) · [SourceType](../sourcetype-swift.enum.md)

# AVCaptureTimecode.SourceType.external

<sub>Case</sub>

Synchronizes timecode to an external timecode data stream. Ideal for professional audio and video synchronization with external quarter-frame MIDI or HID timecode hardware.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
case external
```

## See Also

### Source types

- [AVCaptureTimecodeSourceTypeFrameCount](framecount.md) — No internal or external source is adopted. Timecodes are zero-based, sequentially generated frame counts.
- [AVCaptureTimecodeSourceTypeRealTimeClock](realtimeclock.md) — Synchronizes timecode to the system clock for real-time applications. Useful for live events or scenarios requiring alignment with the actual time of day.
