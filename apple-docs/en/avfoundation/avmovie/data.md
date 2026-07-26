---
title: data
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmovie/data
source_url: 'https://developer.apple.com/documentation/avfoundation/avmovie/data'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmovie/data.json'
content_hash: 'sha256:cd9c5e4752bbf671'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMovie](../avmovie.md)

# data

<sub>Instance Property</sub>

A data object that contains the movie file’s data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var data: Data? { get }
```

## Discussion

The value is `nil` if you didn’t initialize the movie with data.

## See Also

### Accessing movie information

- [URL](url.md) — A URL to a QuickTime or ISO base media file.
