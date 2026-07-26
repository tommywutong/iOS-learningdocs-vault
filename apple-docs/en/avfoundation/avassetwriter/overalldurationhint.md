---
title: overallDurationHint
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriter/overalldurationhint
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/overalldurationhint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/overalldurationhint.json'
content_hash: 'sha256:9461f3ae8c7493a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# overallDurationHint

<sub>Instance Property</sub>

A hint of the final duration of the output file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var overallDurationHint: CMTime { get set }
```

## Discussion

The default value of [invalid](../../coremedia/cmtime/invalid.md) indicates that the asset writer doesn’t write an overall duration hint to the file. The asset writer ignores this value if it doesn’t write movie fragments.

You can’t set this property after writing starts.

## See Also

### Configuring fragment output

- [movieFragmentInterval](moviefragmentinterval.md) — The interval at which to write movie fragments.
- [initialMovieFragmentInterval](initialmoviefragmentinterval.md) — The interval at which to write the initial movie fragment.
- [initialMovieFragmentSequenceNumber](initialmoviefragmentsequencenumber.md) — The sequence number of the initial movie fragment.
- [producesCombinableFragments](producescombinablefragments.md) — A Boolean value that indicates whether the asset writer outputs movie fragments suitable for combining with others.
- [movieTimeScale](movietimescale.md) — The time scale of the movie.
