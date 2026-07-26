---
title: preferredVolume
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/preferredvolume-8q2yt
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/preferredvolume-8q2yt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/preferredvolume-8q2yt.json'
content_hash: 'sha256:51eae3f3eba52d34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# preferredVolume

<sub>Type Property</sub>

The track’s volume preference for playing its audible media.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var preferredVolume: AVAsyncProperty<Root, Float> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

The preferred volume for an audio track is typically, but not always, `1.0`. For nonaudible tracks, the value is `0.0`.

## See Also

### Loading audible characteristics

- [hasAudioSampleDependencies](hasaudiosampledependencies.md) — A Boolean value that indicates whether the track has sample dependencies.
