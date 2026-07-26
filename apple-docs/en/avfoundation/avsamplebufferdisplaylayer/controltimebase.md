---
title: controlTimebase
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 10.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferdisplaylayer/controltimebase
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/controltimebase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferdisplaylayer/controltimebase.json'
content_hash: 'sha256:ca86ce4e5a9413ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferDisplayLayer](../avsamplebufferdisplaylayer.md)

# controlTimebase

<sub>Instance Property</sub>

A timebase that determines how the layer interprets timestamps.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var controlTimebase: CMTimebase? { get set }
```

## Discussion

By default, this property is `nil`, which indicates the layer interprets timestamps according the host time clock (`mach_absolute_time` with the appropriate timescale conversion; this is the same as Core Animation’s [CACurrentMediaTime()](<../../quartzcore/cacurrentmediatime().md>)). Without a control timebase, it isn’t possible to change when the layer displays frames after enqueuing them.

Setting a valid time base enables you to control the timing of frame display by setting the rate and time of the control timebase.

If you’re synchronizing video to audio, you should use a timebase whose host clock is a [CMClock](../../coremedia/cmclock.md) for the appropriate audio device to prevent drift. See [CMAudioClock](../../coremedia/cmaudioclock-api.md) for more information.

## See Also

### Configuring the layer

- [readyForDisplay](isreadyfordisplay.md) — A Boolean value that indicates whether the first video frame is ready for display.
- [videoGravity](videogravity.md) — A value that indicates how the layer displays video within its bounds.
- [AVLayerVideoGravity](../avlayervideogravity.md) — A structure that defines how a layer displays a player’s visual content within the layer’s bounds.
