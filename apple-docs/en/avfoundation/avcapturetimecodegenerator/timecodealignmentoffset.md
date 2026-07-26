---
title: timecodeAlignmentOffset
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturetimecodegenerator/timecodealignmentoffset
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/timecodealignmentoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecodegenerator/timecodealignmentoffset.json'
content_hash: 'sha256:10a3d9796209bf06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md)

# timecodeAlignmentOffset

<sub>Instance Property</sub>

The time offset, in seconds, applied to the generated timecode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var timecodeAlignmentOffset: TimeInterval { get set }
```

## Discussion

This offset allows fine-tuning of time alignment for synchronization with external sources or to accommodate any intentional delay. The default value is 0 seconds.

## See Also

### Configuring the generator

- [synchronizationTimeout](synchronizationtimeout.md) — The maximum time interval allowed for source synchronization attempts before timing out.
- [timecodeFrameDuration](timecodeframeduration.md) — The frame duration that the generator will use to generate timecodes.
- [- setDelegate:queue:](<setdelegate(__queue_).md>) — Assigns a delegate to receive real-time timecode updates and specifies a queue for callbacks.
