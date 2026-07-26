---
title: rate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avdelegatingplaybackcoordinatorplaycommand/rate
source_url: 'https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinatorplaycommand/rate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdelegatingplaybackcoordinatorplaycommand/rate.json'
content_hash: 'sha256:dc10fed75eec7216'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVDelegatingPlaybackCoordinatorPlayCommand](../avdelegatingplaybackcoordinatorplaycommand.md)

# rate

<sub>Instance Property</sub>

A rate to use when starting playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var rate: Float { get }
```

## Discussion

This value is always nonzero.

## See Also

### Accessing command details

- [itemTime](itemtime.md) — A time in the item timeline to use to begin playback.
- [hostClockTime](hostclocktime.md) — A host clock time to use to begin playback.
