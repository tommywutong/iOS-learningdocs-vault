---
title: isModified
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovie/ismodified
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/ismodified'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/ismodified.json'
content_hash: 'sha256:305deabb6c5b4ff3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# isModified

<sub>Instance Property</sub>

A Boolean value that indicates whether the movie is in a modified state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var isModified: Bool { get set }
```

## Discussion

The value is true if you’ve modified the movie since you created it, saved it, or had its modified state cleared.

## See Also

### Configuring a movie

- [timescale](timescale.md) — The time scale of the movie.
- [interleavingPeriod](interleavingperiod.md) — A time period indicating the duration for interleaving runs of samples for each track.
- [defaultMediaDataStorage](defaultmediadatastorage.md) — The default storage container for media data that you add to a movie.
