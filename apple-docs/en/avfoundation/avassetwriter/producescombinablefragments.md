---
title: producesCombinableFragments
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriter/producescombinablefragments
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/producescombinablefragments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/producescombinablefragments.json'
content_hash: 'sha256:0ae6b621beeb379c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# producesCombinableFragments

<sub>Instance Property</sub>

A Boolean value that indicates whether the asset writer outputs movie fragments suitable for combining with others.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var producesCombinableFragments: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md). Set the value to [true](../../swift/true.md) when you use multiple asset writers to produce distinct streams that complement each other, such as HLS encodings or bit rate variants.

You can’t set this property after writing starts.

## See Also

### Configuring fragment output

- [movieFragmentInterval](moviefragmentinterval.md) — The interval at which to write movie fragments.
- [initialMovieFragmentInterval](initialmoviefragmentinterval.md) — The interval at which to write the initial movie fragment.
- [initialMovieFragmentSequenceNumber](initialmoviefragmentsequencenumber.md) — The sequence number of the initial movie fragment.
- [overallDurationHint](overalldurationhint.md) — A hint of the final duration of the output file.
- [movieTimeScale](movietimescale.md) — The time scale of the movie.
