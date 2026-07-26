---
title: 'supportedOutputSettingsKeys(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturemoviefileoutput/supportedoutputsettingskeys(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/supportedoutputsettingskeys(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemoviefileoutput/supportedoutputsettingskeys%28for%3A%29.json'
content_hash: 'sha256:f1597ba4a1cfde30'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureMovieFileOutput](../avcapturemoviefileoutput.md)

# supportedOutputSettingsKeys(for:)

<sub>Instance Method</sub>

Returns a list of supported keys to use in the output settings dictionary.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func supportedOutputSettingsKeys(for connection: AVCaptureConnection) -> [String]
```

## Parameters

- `connection` — The connection that delivers the media to encode.

## Return Value

An array of keys that can be set in the [- setOutputSettings:forConnection:](<setoutputsettings(__for_).md>)method.

## See Also

### Managing output settings

- [- outputSettingsForConnection:](<outputsettings(for_).md>) — Returns the settings the output uses to encode media from the specified connection.
- [- setOutputSettings:forConnection:](<setoutputsettings(__for_).md>) — Sets the options the output uses to encode media from the given connection while recording.
- [availableVideoCodecTypes](availablevideocodectypes.md) — The video codecs types the output supports for recording movie files.
