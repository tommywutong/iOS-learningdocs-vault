---
title: addMovieHeaderToDestination
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmoviewritingoptions/addmovieheadertodestination
source_url: 'https://developer.apple.com/documentation/avfoundation/avmoviewritingoptions/addmovieheadertodestination'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmoviewritingoptions/addmovieheadertodestination.json'
content_hash: 'sha256:148da4bfcd35510e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMovieWritingOptions](../avmoviewritingoptions.md)

# addMovieHeaderToDestination

<sub>Type Property</sub>

The new movie header overwrites any existing movie header.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
static var addMovieHeaderToDestination: AVMovieWritingOptions { get }
```

## Discussion

Only an existing movie header is overwritten, all other data is preserved. If the destination file is empty, a file type box is created at the beginning of the file.

## See Also

### Writing options

- [AVMovieWritingTruncateDestinationToMovieHeaderOnly](truncatedestinationtomovieheaderonly.md) — The movie header overwrites all existing data and creates a pure reference movie file.
