---
title: 'init(settingsFrom:options:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablemovie/init(settingsfrom:options:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/init(settingsfrom:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/init%28settingsfrom%3Aoptions%3A%29.json'
content_hash: 'sha256:9b7f557584584514'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# init(settingsFrom:options:)

<sub>Initializer</sub>

Creates a mutable movie object without tracks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
init(settingsFrom movie: AVMovie?, options: [String : Any]? = nil) throws
```

## Parameters

- `movie` — A movie object that contains settings from an existing movie.

- `options` — A dictionary that contains key for specifying the movie object initialization. Currently, no keys are defined.

## Return Value

An `AVMutableMovie` object.

## Discussion

On initialization, the [defaultMediaDataStorage](defaultmediadatastorage.md) property and any associated [mediaDataStorage](../avmutablemovietrack/mediadatastorage.md) properties are set to `nil`. To create an `AVMutableMovie` from a file and then append sample buffers to any of its tracks, you must first set one of these properties to indicate where the sample data should be written.

## See Also

### Creating a movie

- [- initWithURL:options:error:](<init(url_options_error_)-8rnnj.md>) — Creates a mutable movie object from a movie header stored in a QuickTime movie file of ISO base media file.
- [- initWithData:options:error:](<init(data_options_error_).md>) — Creates a mutable movie object from a movie stored in a data object.
