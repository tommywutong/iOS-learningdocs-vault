---
title: initialMovieFragmentSequenceNumber
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriter/initialmoviefragmentsequencenumber
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/initialmoviefragmentsequencenumber'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/initialmoviefragmentsequencenumber.json'
content_hash: 'sha256:d17d2ef9c1eeb589'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# initialMovieFragmentSequenceNumber

<sub>Instance Property</sub>

The sequence number of the initial movie fragment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var initialMovieFragmentSequenceNumber: Int { get set }
```

## Discussion

If you combine movie fragments that you create from multiple asset writers, movie fragment sequence numbers need to increase monotonically across the entire combined collection, in temporal order. The default value of this property is `1`.

You can’t set this property after writing starts.

## See Also

### Configuring fragment output

- [movieFragmentInterval](moviefragmentinterval.md) — The interval at which to write movie fragments.
- [initialMovieFragmentInterval](initialmoviefragmentinterval.md) — The interval at which to write the initial movie fragment.
- [producesCombinableFragments](producescombinablefragments.md) — A Boolean value that indicates whether the asset writer outputs movie fragments suitable for combining with others.
- [overallDurationHint](overalldurationhint.md) — A hint of the final duration of the output file.
- [movieTimeScale](movietimescale.md) — The time scale of the movie.
