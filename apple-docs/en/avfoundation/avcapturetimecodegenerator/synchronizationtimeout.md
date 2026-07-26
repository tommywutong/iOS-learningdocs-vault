---
title: synchronizationTimeout
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturetimecodegenerator/synchronizationtimeout
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/synchronizationtimeout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecodegenerator/synchronizationtimeout.json'
content_hash: 'sha256:f88aee34e9874307'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md)

# synchronizationTimeout

<sub>Instance Property</sub>

The maximum time interval allowed for source synchronization attempts before timing out.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var synchronizationTimeout: TimeInterval { get set }
```

## Discussion

This property specifies the duration, in seconds, that the [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md) will attempt to synchronize with a timecode source before timing out if synchronization cannot be achieved. If this threshold is exceeded, the synchronization status updates to reflect a timeout, and your [- timecodeGenerator:transitionedToSynchronizationStatus:forSource:](<../avcapturetimecodegeneratordelegate/timecodegenerator(__transitionedto_for_).md>) delegate method fires, informing you of the event. The default value is 15 seconds.

## See Also

### Configuring the generator

- [timecodeAlignmentOffset](timecodealignmentoffset.md) — The time offset, in seconds, applied to the generated timecode.
- [timecodeFrameDuration](timecodeframeduration.md) — The frame duration that the generator will use to generate timecodes.
- [- setDelegate:queue:](<setdelegate(__queue_).md>) — Assigns a delegate to receive real-time timecode updates and specifies a queue for callbacks.
