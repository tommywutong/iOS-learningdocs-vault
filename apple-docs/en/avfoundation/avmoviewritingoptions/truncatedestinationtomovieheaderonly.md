---
title: truncateDestinationToMovieHeaderOnly
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmoviewritingoptions/truncatedestinationtomovieheaderonly
source_url: 'https://developer.apple.com/documentation/avfoundation/avmoviewritingoptions/truncatedestinationtomovieheaderonly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmoviewritingoptions/truncatedestinationtomovieheaderonly.json'
content_hash: 'sha256:74ae2729b0737d1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMovieWritingOptions](../avmoviewritingoptions.md)

# truncateDestinationToMovieHeaderOnly

<sub>Type Property</sub>

The movie header overwrites all existing data and creates a pure reference movie file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
static var truncateDestinationToMovieHeaderOnly: AVMovieWritingOptions { get }
```

## Discussion

Creates a file type box at the beginning of the destination file.

## See Also

### Writing options

- [AVMovieWritingAddMovieHeaderToDestination](addmovieheadertodestination.md) — The new movie header overwrites any existing movie header.
