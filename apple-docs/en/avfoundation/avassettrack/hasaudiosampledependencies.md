---
title: hasAudioSampleDependencies
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+（16.0 起废弃）, iPadOS 13.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.15+（13.0 起废弃）, tvOS 13.0+（16.0 起废弃）, watchOS 6.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassettrack/hasaudiosampledependencies
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/hasaudiosampledependencies'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/hasaudiosampledependencies.json'
content_hash: 'sha256:a1b77031700446ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrack](../avassettrack.md)

# hasAudioSampleDependencies

<sub>Instance Property</sub>

A Boolean value that indicates whether the track has sample dependencies.

> [!warning] Deprecated
> Load the value of [hasAudioSampleDependencies](../avpartialasyncproperty/hasaudiosampledependencies.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
var hasAudioSampleDependencies: Bool { get }
```

## Discussion

The value is always [false](../../swift/false.md) for nonaudible media.
