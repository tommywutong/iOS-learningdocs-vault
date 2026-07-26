---
title: AVFragmentedMovieMinder
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.10+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avfragmentedmovieminder
source_url: 'https://developer.apple.com/documentation/avfoundation/avfragmentedmovieminder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avfragmentedmovieminder.json'
content_hash: 'sha256:2b97755a33e73086'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVFragmentedMovieMinder

<sub>Class</sub>

An object that checks whether a fragmented movie appends additional movie fragments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
class AVFragmentedMovieMinder
```

## Overview

This class is identical to [AVFragmentedAssetMinder](avfragmentedassetminder.md) except that it’s capable of minding only assets of type [AVFragmentedMovie](avfragmentedmovie.md).

## Relationships

- **Inherits From**: [AVFragmentedAssetMinder](avfragmentedassetminder.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a movie minder

- [- initWithMovie:mindingInterval:](<avfragmentedmovieminder/init(movie_mindinginterval_).md>) — Creates a movie minder and adds a movie with a minding interval.

### Adding and removing movies

- [movies](avfragmentedmovieminder/movies.md) — An array containing the fragmented movie objects being minded.
- [- addFragmentedMovie:](<avfragmentedmovieminder/add(__).md>) — Adds a fragmented movie to the array of movies being minded.
- [- removeFragmentedMovie:](<avfragmentedmovieminder/remove(__).md>) — Removes a fragmented movie from the array of movies being minded.

### Accessing minder information

- [mindingInterval](avfragmentedmovieminder/mindinginterval.md) — The amount of time between checks for additional movie fragments.

## See Also

### Fragmented movies

- [AVFragmentedMovie](avfragmentedmovie.md) — An object that represents a fragmented movie file.
- [AVFragmentedMovieTrack](avfragmentedmovietrack.md) — An object that represents a track in a fragmented movie.
- [AVFragmentMinding](avfragmentminding.md) — A protocol that defines whether an asset supports fragment minding.
