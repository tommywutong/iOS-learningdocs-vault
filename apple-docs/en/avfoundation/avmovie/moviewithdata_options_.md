---
title: 'movieWithData:options:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmovie/moviewithdata:options:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmovie/moviewithdata:options:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmovie/moviewithdata%3Aoptions%3A.json'
content_hash: 'sha256:ff64b445601c68f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMovie](../avmovie.md)

# movieWithData:options:

<sub>Type Method</sub>

Returns a new movie object from a movie file’s data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) movieWithData:(NSData *) data options:(NSDictionary<NSString *,id> *) options;
```

## Parameters

- `data` — A data object that contains a movie header.

- `options` — A dictionary of options to use to initialize the movie.

## Return Value

A movie object.

## Discussion

Use this method to create movies from movie headers that aren’t stored in files, which can include movies that the pasteboard contains.

## See Also

### Creating a movie

- [movieWithURL:options:](moviewithurl_options_.md) — Returns a new movie object from a movie header stored in a QuickTime movie file of ISO base media file.
- [- initWithURL:options:](<init(url_options_)-1wjrq.md>) — Creates a movie object from a movie header stored in a QuickTime movie file of ISO base media file.
- [- initWithData:options:](<init(data_options_).md>) — Creates a movie object from a movie file’s data.
- [Initialization options](../initialization-options.md) — Specify options to configure the initialization of a movie.
