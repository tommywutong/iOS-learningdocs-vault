---
title: 'init(data:options:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmovie/init(data:options:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmovie/init(data:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmovie/init%28data%3Aoptions%3A%29.json'
content_hash: 'sha256:6316e2e17f74b3e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMovie](../avmovie.md)

# init(data:options:)

<sub>Initializer</sub>

Creates a movie object from a movie file’s data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
init(data: Data, options: [String : Any]? = nil)
```

## Parameters

- `data` — A data object that contains a movie header.

- `options` — A dictionary of options to use to initialize the movie.

## Discussion

Use this method to create movies from movie headers that aren’t stored in files, which can include movies that the pasteboard contains.

## See Also

### Creating a movie

- [init(url:)](<init(url_).md>) — Creates a movie that models the media at the specified URL.
- [- initWithURL:options:](<init(url_options_)-1wjrq.md>) — Creates a movie object from a movie header stored in a QuickTime movie file of ISO base media file.
- [Initialization options](../initialization-options.md) — Specify options to configure the initialization of a movie.
