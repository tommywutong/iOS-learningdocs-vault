---
title: 'init(url:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.10+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmovie/init(url:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmovie/init(url:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmovie/init%28url%3A%29.json'
content_hash: 'sha256:43e18d13e48605f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMovie](../avmovie.md)

# init(url:)

<sub>Initializer</sub>

Creates a movie that models the media at the specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
convenience init(url: URL)
```

## Parameters

- `url` — A URL to a local, remote, or HTTP Live Streaming media resource.

## See Also

### Creating a movie

- [- initWithURL:options:](<init(url_options_)-1wjrq.md>) — Creates a movie object from a movie header stored in a QuickTime movie file of ISO base media file.
- [- initWithData:options:](<init(data_options_).md>) — Creates a movie object from a movie file’s data.
- [Initialization options](../initialization-options.md) — Specify options to configure the initialization of a movie.
