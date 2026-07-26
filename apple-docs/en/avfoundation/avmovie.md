---
title: AVMovie
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.10+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmovie
source_url: 'https://developer.apple.com/documentation/avfoundation/avmovie'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmovie.json'
content_hash: 'sha256:de049a0542cae9ea'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMovie

<sub>Class</sub>

An object that represents an audiovisual container that conforms to the QuickTime movie file format or a related format like MPEG-4.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
class AVMovie
```

## Overview

`AVMovie` supports operations involving the format-specific portions of the QuickTime movie model that [AVAsset](avasset.md) doesn’t support. For instance, retrieving the movie header from an existing QuickTime movie file. You can also use `AVMovie` to write a movie header into a new file, thereby creating a reference movie.

## Relationships

- **Inherits From**: [AVAsset](avasset.md)

- **Inherited By**: [AVFragmentedMovie](avfragmentedmovie.md), [AVMutableMovie](avmutablemovie.md)

- **Conforms To**: [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a movie

- [init(url:)](<avmovie/init(url_).md>) — Creates a movie that models the media at the specified URL.
- [- initWithURL:options:](<avmovie/init(url_options_)-1wjrq.md>) — Creates a movie object from a movie header stored in a QuickTime movie file of ISO base media file.
- [- initWithData:options:](<avmovie/init(data_options_).md>) — Creates a movie object from a movie file’s data.
- [Initialization options](initialization-options.md) — Specify options to configure the initialization of a movie.

### Determining supported file types

- [+ movieTypes](<avmovie/movietypes().md>) — Returns the file types that a movie supports.

### Loading tracks

- [tracks](avpartialasyncproperty/tracks-80a83.md) — The tracks that a movie contains.
- [- loadTrackWithTrackID:completionHandler:](<avmovie/loadtrack(withtrackid_completionhandler_).md>) — Loads a track that contains the specified identifier.
- [- loadTracksWithMediaType:completionHandler:](<avmovie/loadtracks(withmediatype_completionhandler_).md>) — Loads tracks that contain media of a specified type.
- [- loadTracksWithMediaCharacteristic:completionHandler:](<avmovie/loadtracks(withmediacharacteristic_completionhandler_).md>) — Loads tracks that contain media of a specified characteristic.

### Creating and writing headers

- [- isCompatibleWithFileType:](<avmovie/is(compatiblewithfiletype_).md>) — Returns a Boolean value that indicates whether the system can create a movie header of the specified type.
- [- movieHeaderWithFileType:error:](<avmovie/makemovieheader(filetype_).md>) — Creates a header for a movie for the specified file type.
- [- writeMovieHeaderToURL:fileType:options:error:](<avmovie/writeheader(to_filetype_options_).md>) — Writes the movie header to the specified URL.
- [AVMovieWritingOptions](avmoviewritingoptions.md) — A structure that defines options to control the writing of a movie header to a destination URL.

### Determining fragment support

- [canContainMovieFragments](avmovie/cancontainmoviefragments.md) — A Boolean value that indicates whether fragments can extend the movie file.
- [containsMovieFragments](avmovie/containsmoviefragments.md) — A Boolean value that indicates whether at least one movie fragment extends the movie file.

### Accessing movie information

- [URL](avmovie/url.md) — A URL to a QuickTime or ISO base media file.
- [data](avmovie/data.md) — A data object that contains the movie file’s data.

### Accessing tracks

- [tracks](avmovie/tracks.md) — The tracks that a movie contains.
- [- trackWithTrackID:](<avmovie/track(withtrackid_).md>) — Retrieves a track in the movie that contains the specified identifier. _(deprecated)_
- [- tracksWithMediaType:](<avmovie/tracks(withmediatype_).md>) — Retrieves tracks in the movie that present media of the specified type. _(deprecated)_
- [- tracksWithMediaCharacteristic:](<avmovie/tracks(withmediacharacteristic_).md>) — Retrieves tracks in the movie that present media of the specified characteristic. _(deprecated)_

### Accessing data storage

- [defaultMediaDataStorage](avmovie/defaultmediadatastorage.md) — The default storage container for media data added to a movie.

### Initializers

- [init(URL:options:)](<avmovie/init(url_options_)-3tgg4.md>)
- [init(URL:options:)](<avmovie/init(url_options_)-9sf6c.md>)

## See Also

### Movies

- [AVMovieTrack](avmovietrack.md) — A track in a movie that conforms to the QuickTime or ISO base media file format.
