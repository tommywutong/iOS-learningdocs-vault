---
title: 'setOutputSettings(_:for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturemoviefileoutput/setoutputsettings(_:for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/setoutputsettings(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemoviefileoutput/setoutputsettings%28_%3Afor%3A%29.json'
content_hash: 'sha256:dbca0f9740c1b44e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureMovieFileOutput](../avcapturemoviefileoutput.md)

# setOutputSettings(_:for:)

<sub>Instance Method</sub>

Sets the options the output uses to encode media from the given connection while recording.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func setOutputSettings(_ outputSettings: [String : Any]?, for connection: AVCaptureConnection)
```

## Parameters

- `outputSettings` — A dictionary of output settings. Pass an empty dictionary to specify that the format of the media from the connection shouldn’t change before writing to the file. Pass `nil` to specify that the session preset determines output format.

- `connection` — The connection delivering the media to encode.

## Discussion

For details on output settings, see [Video settings](../video-settings.md) for video connections and [Audio settings](../audio-settings.md) for audio connections.

On iOS, your output settings dictionary may only contain keys listed returned from the [- supportedOutputSettingsKeysForConnection:](<supportedoutputsettingskeys(for_).md>) method. If you specify any other key, the system throws an invalid argument exception. Additionally, the value you specify for [AVVideoCodecKey](../avvideocodeckey.md) should be present in the [availableVideoCodecTypes](availablevideocodectypes.md) array. If you specify [AVVideoCompressionPropertiesKey](../avvideocompressionpropertieskey.md), you must also specify a valid value for [AVVideoCodecKey](../avvideocodeckey.md).

On iOS, the [- outputSettingsForConnection:](<outputsettings(for_).md>) method always provides a fully populated dictionary. If you call [- outputSettingsForConnection:](<outputsettings(for_).md>) with the intent of overriding a few of the values, you must exclude keys that aren’t supported before calling [- setOutputSettings:forConnection:](<setoutputsettings(__for_).md>). When providing an [AVVideoCompressionPropertiesKey](../avvideocompressionpropertieskey.md) sub dictionary, you may specify a sparse dictionary. A movie file output object always fills in missing keys with default values for the current capture session configuration.

## See Also

### Managing output settings

- [- supportedOutputSettingsKeysForConnection:](<supportedoutputsettingskeys(for_).md>) — Returns a list of supported keys to use in the output settings dictionary.
- [- outputSettingsForConnection:](<outputsettings(for_).md>) — Returns the settings the output uses to encode media from the specified connection.
- [availableVideoCodecTypes](availablevideocodectypes.md) — The video codecs types the output supports for recording movie files.
