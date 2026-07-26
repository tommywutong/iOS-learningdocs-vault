---
title: 'outputSettings(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturemoviefileoutput/outputsettings(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/outputsettings(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemoviefileoutput/outputsettings%28for%3A%29.json'
content_hash: 'sha256:f778bddfba8bc429'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureMovieFileOutput](../avcapturemoviefileoutput.md)

# outputSettings(for:)

<sub>Instance Method</sub>

Returns the settings the output uses to encode media from the specified connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func outputSettings(for connection: AVCaptureConnection) -> [String : Any]
```

## Parameters

- `connection` — The connection delivering the media to encode.

## Return Value

A dictionary of output settings.

## Discussion

If the returned value is an empty dictionary, the format of the media from the connection isn’t changed before writing to the file.

If you call [- setOutputSettings:forConnection:](<setoutputsettings(__for_).md>) with a `nil` dictionary, this method returns a non-`nil` dictionary that reflects the settings used by the capture session’s [sessionPreset](../avcapturesession/sessionpreset.md) value.

## See Also

### Managing output settings

- [- supportedOutputSettingsKeysForConnection:](<supportedoutputsettingskeys(for_).md>) — Returns a list of supported keys to use in the output settings dictionary.
- [- setOutputSettings:forConnection:](<setoutputsettings(__for_).md>) — Sets the options the output uses to encode media from the given connection while recording.
- [availableVideoCodecTypes](availablevideocodectypes.md) — The video codecs types the output supports for recording movie files.
