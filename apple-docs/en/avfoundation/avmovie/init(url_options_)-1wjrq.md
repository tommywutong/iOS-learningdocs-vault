---
title: 'init(url:options:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.10+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmovie/init(url:options:)-1wjrq'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmovie/init(url:options:)-1wjrq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmovie/init%28url%3Aoptions%3A%29-1wjrq.json'
content_hash: 'sha256:52417efe627c07d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMovie](../avmovie.md)

# init(url:options:)

<sub>Initializer</sub>

Creates a movie object from a movie header stored in a QuickTime movie file of ISO base media file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
init(url URL: URL, options: [String : Any]? = nil)
```

## Parameters

- `URL` — A URL that points to a file containing a movie header.

- `options` — A dictionary of options to use to initialize the movie.

## Discussion

Upon creation, the values of the [defaultMediaDataStorage](defaultmediadatastorage.md) property and any associated [mediaDataStorage](../avmovietrack/mediadatastorage.md) properties are `nil`.

## See Also

### Creating a movie

- [init(url:)](<init(url_).md>) — Creates a movie that models the media at the specified URL.
- [- initWithData:options:](<init(data_options_).md>) — Creates a movie object from a movie file’s data.
- [Initialization options](../initialization-options.md) — Specify options to configure the initialization of a movie.
