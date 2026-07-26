---
title: interleavingPeriod
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovie/interleavingperiod
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/interleavingperiod'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/interleavingperiod.json'
content_hash: 'sha256:dfd981460fe33792'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# interleavingPeriod

<sub>Instance Property</sub>

A time period indicating the duration for interleaving runs of samples for each track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var interleavingPeriod: CMTime { get set }
```

## Discussion

Default value is `0.5` seconds.

## See Also

### Configuring a movie

- [modified](ismodified.md) — A Boolean value that indicates whether the movie is in a modified state.
- [timescale](timescale.md) — The time scale of the movie.
- [defaultMediaDataStorage](defaultmediadatastorage.md) — The default storage container for media data that you add to a movie.
