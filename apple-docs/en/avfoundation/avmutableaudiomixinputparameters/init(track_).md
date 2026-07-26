---
title: 'init(track:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutableaudiomixinputparameters/init(track:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutableaudiomixinputparameters/init(track:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutableaudiomixinputparameters/init%28track%3A%29.json'
content_hash: 'sha256:0d9adae72173a4ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableAudioMixInputParameters](../avmutableaudiomixinputparameters.md)

# init(track:)

<sub>Initializer</sub>

Creates a mutable input parameters object for a given track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(track: AVAssetTrack?)
```

## Parameters

- `track` — The track to associate with the input parameters object.

## Return Value

A mutable input parameters object with no volume ramps and [trackID](trackid.md) set to `track`’s identifier.
