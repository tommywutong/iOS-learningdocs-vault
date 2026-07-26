---
title: availableVideoCodecTypes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturemoviefileoutput/availablevideocodectypes
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/availablevideocodectypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemoviefileoutput/availablevideocodectypes.json'
content_hash: 'sha256:d6137842c420fb67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureMovieFileOutput](../avcapturemoviefileoutput.md)

# availableVideoCodecTypes

<sub>Instance Property</sub>

The video codecs types the output supports for recording movie files.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var availableVideoCodecTypes: [AVVideoCodecType] { get }
```

## Discussion

The first codec in this list is the default for recording movie files. To record using a different codec, call the [- setOutputSettings:forConnection:](<setoutputsettings(__for_).md>) method, passing a video settings dictionary with a value for [AVVideoCodecKey](../avvideocodeckey.md) that matches one of the other values in this list.

## See Also

### Managing output settings

- [- supportedOutputSettingsKeysForConnection:](<supportedoutputsettingskeys(for_).md>) — Returns a list of supported keys to use in the output settings dictionary.
- [- outputSettingsForConnection:](<outputsettings(for_).md>) — Returns the settings the output uses to encode media from the specified connection.
- [- setOutputSettings:forConnection:](<setoutputsettings(__for_).md>) — Sets the options the output uses to encode media from the given connection while recording.
