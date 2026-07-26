---
title: hasAudioSampleDependencies
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/hasaudiosampledependencies
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/hasaudiosampledependencies'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/hasaudiosampledependencies.json'
content_hash: 'sha256:feb1614b9b8af9c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# hasAudioSampleDependencies

<sub>Type Property</sub>

A Boolean value that indicates whether the track has sample dependencies.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var hasAudioSampleDependencies: AVAsyncProperty<Root, Bool> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

The value is always [false](../../swift/false.md) for nonaudible media.

## See Also

### Loading audible characteristics

- [preferredVolume](preferredvolume-8q2yt.md) — The track’s volume preference for playing its audible media.
