---
title: AVCaptureTimecode.SourceType.realTimeClock
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturetimecode/sourcetype-swift.enum/realtimeclock
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecode/sourcetype-swift.enum/realtimeclock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecode/sourcetype-swift.enum/realtimeclock.json'
content_hash: 'sha256:fe95b509dbe752bf'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureTimecode](../../avcapturetimecode.md) · [SourceType](../sourcetype-swift.enum.md)

# AVCaptureTimecode.SourceType.realTimeClock

<sub>Case</sub>

Synchronizes timecode to the system clock for real-time applications. Useful for live events or scenarios requiring alignment with the actual time of day.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
case realTimeClock
```

## See Also

### Source types

- [AVCaptureTimecodeSourceTypeExternal](external.md) — Synchronizes timecode to an external timecode data stream. Ideal for professional audio and video synchronization with external quarter-frame MIDI or HID timecode hardware.
- [AVCaptureTimecodeSourceTypeFrameCount](framecount.md) — No internal or external source is adopted. Timecodes are zero-based, sequentially generated frame counts.
