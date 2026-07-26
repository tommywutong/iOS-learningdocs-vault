---
title: 'is(compatibleWithFileType:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmovie/is(compatiblewithfiletype:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmovie/is(compatiblewithfiletype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmovie/is%28compatiblewithfiletype%3A%29.json'
content_hash: 'sha256:c09a8088caf87db0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMovie](../avmovie.md)

# is(compatibleWithFileType:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the system can create a movie header of the specified type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func `is`(compatibleWithFileType fileType: AVFileType) -> Bool
```

## Parameters

- `fileType` — A file type to test.

## Return Value

[true](../../swift/true.md) if the movie only contains tracks whose media types are allowed by the specified file type; otherwise, [false](../../swift/false.md).

## See Also

### Creating and writing headers

- [- movieHeaderWithFileType:error:](<makemovieheader(filetype_).md>) — Creates a header for a movie for the specified file type.
- [- writeMovieHeaderToURL:fileType:options:error:](<writeheader(to_filetype_options_).md>) — Writes the movie header to the specified URL.
- [AVMovieWritingOptions](../avmoviewritingoptions.md) — A structure that defines options to control the writing of a movie header to a destination URL.
