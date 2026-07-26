---
title: 'fragmentedMovieMinderWithMovie:mindingInterval:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.10+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avfragmentedmovieminder/fragmentedmovieminderwithmovie:mindinginterval:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avfragmentedmovieminder/fragmentedmovieminderwithmovie:mindinginterval:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avfragmentedmovieminder/fragmentedmovieminderwithmovie%3Amindinginterval%3A.json'
content_hash: 'sha256:81d35b82582b9c60'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVFragmentedMovieMinder](../avfragmentedmovieminder.md)

# fragmentedMovieMinderWithMovie:mindingInterval:

<sub>Type Method</sub>

Creates a movie minder and adds a movie with a minding interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) fragmentedMovieMinderWithMovie:(AVFragmentedMovie *) movie mindingInterval:(NSTimeInterval) mindingInterval;
```

## Parameters

- `movie` — The fragmented movie object added to the movie minder.

- `mindingInterval` — The initial minding interval for the movie minder.

## Return Value

A new `AVFragmentedMovieMinder` instance.

## See Also

### Creating a movie minder

- [- initWithMovie:mindingInterval:](<init(movie_mindinginterval_).md>) — Creates a movie minder and adds a movie with a minding interval.
