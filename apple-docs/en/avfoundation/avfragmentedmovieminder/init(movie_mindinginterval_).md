---
title: 'init(movie:mindingInterval:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.10+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avfragmentedmovieminder/init(movie:mindinginterval:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avfragmentedmovieminder/init(movie:mindinginterval:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avfragmentedmovieminder/init%28movie%3Amindinginterval%3A%29.json'
content_hash: 'sha256:74a0cca83f297166'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVFragmentedMovieMinder](../avfragmentedmovieminder.md)

# init(movie:mindingInterval:)

<sub>Initializer</sub>

Creates a movie minder and adds a movie with a minding interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
init(movie: AVFragmentedMovie, mindingInterval: TimeInterval)
```

## Parameters

- `movie` — The fragmented movie object added to the movie minder.

- `mindingInterval` — The initial minding interval for the movie minder.

## Return Value

A new `AVFragmentedMovieMinder` instance.
