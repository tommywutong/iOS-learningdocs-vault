---
title: timescale
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovie/timescale
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/timescale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/timescale.json'
content_hash: 'sha256:4c3d17cb70637c02'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# timescale

<sub>Instance Property</sub>

The time scale of the movie.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var timescale: CMTimeScale { get set }
```

## Discussion

The default movie time scale is `600`. In certain cases, you may want to set this to a different value. For example, a movie that contains a single audio track should set the movie time scale to the media time scale of that track. Set the value of this property on a new empty movie before you perform any edits on it.

## See Also

### Configuring a movie

- [modified](ismodified.md) — A Boolean value that indicates whether the movie is in a modified state.
- [interleavingPeriod](interleavingperiod.md) — A time period indicating the duration for interleaving runs of samples for each track.
- [defaultMediaDataStorage](defaultmediadatastorage.md) — The default storage container for media data that you add to a movie.
