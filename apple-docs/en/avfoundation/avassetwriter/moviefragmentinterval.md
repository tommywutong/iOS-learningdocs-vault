---
title: movieFragmentInterval
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriter/moviefragmentinterval
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/moviefragmentinterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/moviefragmentinterval.json'
content_hash: 'sha256:b3bf4c2e507fecf6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# movieFragmentInterval

<sub>Instance Property</sub>

The interval at which to write movie fragments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var movieFragmentInterval: CMTime { get set }
```

## Discussion

Some container formats, such as QuickTime movies, support writing movies in fragments. Using this feature enables you to open and play a partially written movie in the event that an unexpected error or interruption occurs.

An asset writer disables this feature by default and sets this value to [invalid](../../coremedia/cmtime/invalid.md). To enable fragment writing, set a valid [CMTime](../../coremedia/cmtime.md) value. For best performance when writing to external storage devices, set the movie fragment interval to 10 seconds or greater.

You can’t set this value after writing starts.

## See Also

### Configuring fragment output

- [initialMovieFragmentInterval](initialmoviefragmentinterval.md) — The interval at which to write the initial movie fragment.
- [initialMovieFragmentSequenceNumber](initialmoviefragmentsequencenumber.md) — The sequence number of the initial movie fragment.
- [producesCombinableFragments](producescombinablefragments.md) — A Boolean value that indicates whether the asset writer outputs movie fragments suitable for combining with others.
- [overallDurationHint](overalldurationhint.md) — A hint of the final duration of the output file.
- [movieTimeScale](movietimescale.md) — The time scale of the movie.
