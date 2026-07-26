---
title: canContainMovieFragments
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.10+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmovie/cancontainmoviefragments
source_url: 'https://developer.apple.com/documentation/avfoundation/avmovie/cancontainmoviefragments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmovie/cancontainmoviefragments.json'
content_hash: 'sha256:16a2810f068a099a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMovie](../avmovie.md)

# canContainMovieFragments

<sub>Instance Property</sub>

A Boolean value that indicates whether fragments can extend the movie file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var canContainMovieFragments: Bool { get }
```

## Discussion

The value of this property is `YES` if an `mvex` box is present in the `moov` box. The `mvex` box is necessary to signal the possible presence of later `moof` boxes.

## See Also

### Determining fragment support

- [containsMovieFragments](containsmoviefragments.md) — A Boolean value that indicates whether at least one movie fragment extends the movie file.
