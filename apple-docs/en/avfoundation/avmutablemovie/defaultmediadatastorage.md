---
title: defaultMediaDataStorage
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovie/defaultmediadatastorage
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/defaultmediadatastorage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/defaultmediadatastorage.json'
content_hash: 'sha256:6a32243277472561'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# defaultMediaDataStorage

<sub>Instance Property</sub>

The default storage container for media data that you add to a movie.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@NSCopying var defaultMediaDataStorage: AVMediaDataStorage? { get set }
```

## Discussion

This value specifies a location to write sample data that you add to a movie, for any track for whose [mediaDataStorage](../avmutablemovietrack/mediadatastorage.md) property is `nil`.

## See Also

### Configuring a movie

- [modified](ismodified.md) — A Boolean value that indicates whether the movie is in a modified state.
- [timescale](timescale.md) — The time scale of the movie.
- [interleavingPeriod](interleavingperiod.md) — A time period indicating the duration for interleaving runs of samples for each track.
