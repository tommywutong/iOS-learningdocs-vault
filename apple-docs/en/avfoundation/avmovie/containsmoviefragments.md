---
title: containsMovieFragments
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmovie/containsmoviefragments
source_url: 'https://developer.apple.com/documentation/avfoundation/avmovie/containsmoviefragments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmovie/containsmoviefragments.json'
content_hash: 'sha256:6872e825352cac60'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMovie](../avmovie.md)

# containsMovieFragments

<sub>Instance Property</sub>

A Boolean value that indicates whether at least one movie fragment extends the movie file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var containsMovieFragments: Bool { get }
```

## Discussion

This property is `YES` if [canContainMovieFragments](cancontainmoviefragments.md) is `YES` and at least one `moof` box is present after the `moov` box.

## See Also

### Determining fragment support

- [canContainMovieFragments](cancontainmoviefragments.md) — A Boolean value that indicates whether fragments can extend the movie file.
