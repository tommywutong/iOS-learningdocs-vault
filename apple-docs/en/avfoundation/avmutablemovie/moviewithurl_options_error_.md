---
title: 'movieWithURL:options:error:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablemovie/moviewithurl:options:error:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/moviewithurl:options:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/moviewithurl%3Aoptions%3Aerror%3A.json'
content_hash: 'sha256:f34c36654bb8666f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# movieWithURL:options:error:

<sub>Type Method</sub>

Returns a new mutable movie object from a movie header stored in a QuickTime movie file of ISO base media file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) movieWithURL:(NSURL *) URL options:(NSDictionary<NSString *,id> *) options error:(NSError **) outError;
```

## Parameters

- `URL` — The URL that points to a file containing a movie header.

- `options` — A dictionary that contains key for specifying the movie object initialization. Currently, no keys are defined.

- `outError` — A description of the error that occurred. Default value is `nil`.

## Return Value

An `AVMutableMovie` object.

## Discussion

On initialization, the [defaultMediaDataStorage](defaultmediadatastorage.md) property and any associated [mediaDataStorage](../avmutablemovietrack/mediadatastorage.md) properties are set to `nil`. To create an `AVMutableMovie` from a file and then append sample buffers to any of its tracks, you must first set one of these properties to indicate where the sample data should be written.

## See Also

### Creating a movie

- [- initWithURL:options:error:](<init(url_options_error_)-8rnnj.md>) — Creates a mutable movie object from a movie header stored in a QuickTime movie file of ISO base media file.
- [movieWithData:options:error:](moviewithdata_options_error_.md) — Returns a new mutable movie object from a movie stored in a data object.
- [- initWithData:options:error:](<init(data_options_error_).md>) — Creates a mutable movie object from a movie stored in a data object.
- [movieWithSettingsFromMovie:options:error:](moviewithsettingsfrommovie_options_error_.md) — Returns a new mutable movie object without tracks.
- [- initWithSettingsFromMovie:options:error:](<init(settingsfrom_options_).md>) — Creates a mutable movie object without tracks.
