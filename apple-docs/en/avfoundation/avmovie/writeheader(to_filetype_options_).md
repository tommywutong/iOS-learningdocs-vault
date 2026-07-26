---
title: 'writeHeader(to:fileType:options:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmovie/writeheader(to:filetype:options:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmovie/writeheader(to:filetype:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmovie/writeheader%28to%3Afiletype%3Aoptions%3A%29.json'
content_hash: 'sha256:421ff85d0d0c1ebd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMovie](../avmovie.md)

# writeHeader(to:fileType:options:)

<sub>Instance Method</sub>

Writes the movie header to the specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func writeHeader(to URL: URL, fileType: AVFileType, options: AVMovieWritingOptions = []) throws
```

## Parameters

- `URL` — The URL indicating where to write the movie header.

- `fileType` — A UTI that indicates the specific file format for the movie header.

- `options` — The [AVMovieWritingOptions](../avmoviewritingoptions.md) constants whose bits specify the options for writing the movie header.

## See Also

### Creating and writing headers

- [- isCompatibleWithFileType:](<is(compatiblewithfiletype_).md>) — Returns a Boolean value that indicates whether the system can create a movie header of the specified type.
- [- movieHeaderWithFileType:error:](<makemovieheader(filetype_).md>) — Creates a header for a movie for the specified file type.
- [AVMovieWritingOptions](../avmoviewritingoptions.md) — A structure that defines options to control the writing of a movie header to a destination URL.
