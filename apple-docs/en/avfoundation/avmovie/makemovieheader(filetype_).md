---
title: 'makeMovieHeader(fileType:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmovie/makemovieheader(filetype:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmovie/makemovieheader(filetype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmovie/makemovieheader%28filetype%3A%29.json'
content_hash: 'sha256:307e7a387113e9ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMovie](../avmovie.md)

# makeMovieHeader(fileType:)

<sub>Instance Method</sub>

Creates a header for a movie for the specified file type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func makeMovieHeader(fileType: AVFileType) throws -> Data
```

## Parameters

- `fileType` — A UTI that indicates the specific file format for the movie header.

## Return Value

An [NSData](../../foundation/nsdata.md) object containing the movie header.

## Discussion

The created movie header is a pure reference movie, with no base URL, suitable for use on the pasteboard.

## See Also

### Creating and writing headers

- [- isCompatibleWithFileType:](<is(compatiblewithfiletype_).md>) — Returns a Boolean value that indicates whether the system can create a movie header of the specified type.
- [- writeMovieHeaderToURL:fileType:options:error:](<writeheader(to_filetype_options_).md>) — Writes the movie header to the specified URL.
- [AVMovieWritingOptions](../avmoviewritingoptions.md) — A structure that defines options to control the writing of a movie header to a destination URL.
