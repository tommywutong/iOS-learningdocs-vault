---
title: AVMovieWritingOptions
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmoviewritingoptions
source_url: 'https://developer.apple.com/documentation/avfoundation/avmoviewritingoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmoviewritingoptions.json'
content_hash: 'sha256:1e838dc2fda61bcb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMovieWritingOptions

<sub>Structure</sub>

A structure that defines options to control the writing of a movie header to a destination URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
struct AVMovieWritingOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Writing options

- [AVMovieWritingAddMovieHeaderToDestination](avmoviewritingoptions/addmovieheadertodestination.md) — The new movie header overwrites any existing movie header.
- [AVMovieWritingTruncateDestinationToMovieHeaderOnly](avmoviewritingoptions/truncatedestinationtomovieheaderonly.md) — The movie header overwrites all existing data and creates a pure reference movie file.

### Initializers

- [init(rawValue:)](<avmoviewritingoptions/init(rawvalue_).md>) — Creates a movie writing options structure.

## See Also

### Creating and writing headers

- [- isCompatibleWithFileType:](<avmovie/is(compatiblewithfiletype_).md>) — Returns a Boolean value that indicates whether the system can create a movie header of the specified type.
- [- movieHeaderWithFileType:error:](<avmovie/makemovieheader(filetype_).md>) — Creates a header for a movie for the specified file type.
- [- writeMovieHeaderToURL:fileType:options:error:](<avmovie/writeheader(to_filetype_options_).md>) — Writes the movie header to the specified URL.
