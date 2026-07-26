---
title: 'movieWithURL:options:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.10+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmovie/moviewithurl:options:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmovie/moviewithurl:options:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmovie/moviewithurl%3Aoptions%3A.json'
content_hash: 'sha256:234c2bd8fe495038'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMovie](../avmovie.md)

# movieWithURL:options:

<sub>Type Method</sub>

Returns a new movie object from a movie header stored in a QuickTime movie file of ISO base media file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) movieWithURL:(NSURL *) URL options:(NSDictionary<NSString *,id> *) options;
```

## Parameters

- `URL` — A URL that points to a file containing a movie header.

- `options` — A dictionary of initialization options with which to create the movie.

## Return Value

A movie object.

## Discussion

Upon creation, the values of the [defaultMediaDataStorage](defaultmediadatastorage.md) property and any associated [mediaDataStorage](../avmovietrack/mediadatastorage.md) properties are `nil`.

## See Also

### Creating a movie

- [- initWithURL:options:](<init(url_options_)-1wjrq.md>) — Creates a movie object from a movie header stored in a QuickTime movie file of ISO base media file.
- [movieWithData:options:](moviewithdata_options_.md) — Returns a new movie object from a movie file’s data.
- [- initWithData:options:](<init(data_options_).md>) — Creates a movie object from a movie file’s data.
- [Initialization options](../initialization-options.md) — Specify options to configure the initialization of a movie.
