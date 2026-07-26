---
title: timecodeFrameDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturetimecodegenerator/timecodeframeduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/timecodeframeduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecodegenerator/timecodeframeduration.json'
content_hash: 'sha256:e96839e65de18d32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md)

# timecodeFrameDuration

<sub>Instance Property</sub>

The frame duration that the generator will use to generate timecodes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var timecodeFrameDuration: CMTime { get set }
```

## See Also

### Configuring the generator

- [synchronizationTimeout](synchronizationtimeout.md) — The maximum time interval allowed for source synchronization attempts before timing out.
- [timecodeAlignmentOffset](timecodealignmentoffset.md) — The time offset, in seconds, applied to the generated timecode.
- [- setDelegate:queue:](<setdelegate(__queue_).md>) — Assigns a delegate to receive real-time timecode updates and specifies a queue for callbacks.
