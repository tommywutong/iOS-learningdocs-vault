---
title: 'init(url:options:error:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablemovie/init(url:options:error:)-8rnnj'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/init(url:options:error:)-8rnnj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/init%28url%3Aoptions%3Aerror%3A%29-8rnnj.json'
content_hash: 'sha256:de0981c0e6d4f3ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# init(url:options:error:)

<sub>Initializer</sub>

Creates a mutable movie object from a movie header stored in a QuickTime movie file of ISO base media file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
init(url URL: URL, options: [String : Any]? = nil, error: ()) throws
```

## Parameters

- `URL` — The URL that points to a file containing a movie header.

- `options` — A dictionary that contains key for specifying the movie object initialization. Currently, no keys are defined.

## Return Value

An `AVMutableMovie` object.

## Discussion

On initialization, the [defaultMediaDataStorage](defaultmediadatastorage.md) property and any associated [mediaDataStorage](../avmutablemovietrack/mediadatastorage.md) properties are set to `nil`. To create an `AVMutableMovie` from a file and then append sample buffers to any of its tracks, you must first set one of these properties to indicate where the sample data should be written.

## See Also

### Creating a movie

- [- initWithData:options:error:](<init(data_options_error_).md>) — Creates a mutable movie object from a movie stored in a data object.
- [- initWithSettingsFromMovie:options:error:](<init(settingsfrom_options_).md>) — Creates a mutable movie object without tracks.
