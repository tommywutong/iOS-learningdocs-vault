---
title: movieTimeScale
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriter/movietimescale
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/movietimescale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/movietimescale.json'
content_hash: 'sha256:43bf1c09ccf684d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# movieTimeScale

<sub>Instance Property</sub>

The time scale of the movie.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var movieTimeScale: CMTimeScale { get set }
```

## Discussion

The default value is `0`, which indicates that the asset writer chooses an appropriate value, if applicable.

You can’t set this property value after writing starts.

## See Also

### Configuring fragment output

- [movieFragmentInterval](moviefragmentinterval.md) — The interval at which to write movie fragments.
- [initialMovieFragmentInterval](initialmoviefragmentinterval.md) — The interval at which to write the initial movie fragment.
- [initialMovieFragmentSequenceNumber](initialmoviefragmentsequencenumber.md) — The sequence number of the initial movie fragment.
- [producesCombinableFragments](producescombinablefragments.md) — A Boolean value that indicates whether the asset writer outputs movie fragments suitable for combining with others.
- [overallDurationHint](overalldurationhint.md) — A hint of the final duration of the output file.
