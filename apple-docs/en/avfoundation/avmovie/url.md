---
title: url
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.10+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmovie/url
source_url: 'https://developer.apple.com/documentation/avfoundation/avmovie/url'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmovie/url.json'
content_hash: 'sha256:bc9247e83808c5bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMovie](../avmovie.md)

# url

<sub>Instance Property</sub>

A URL to a QuickTime or ISO base media file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var url: URL? { get }
```

## Discussion

The value is `nil` if you didn’t initialize the movie with a URL.

## See Also

### Accessing movie information

- [data](data.md) — A data object that contains the movie file’s data.
