---
title: 'init(mediaType:outputSettings:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriterinput/init(mediatype:outputsettings:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/init(mediatype:outputsettings:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/init%28mediatype%3Aoutputsettings%3A%29.json'
content_hash: 'sha256:103c60db98f9b953'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# init(mediaType:outputSettings:)

<sub>Initializer</sub>

Creates an input to append sample buffers of the specified type to the output file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init(mediaType: AVMediaType, outputSettings: [String : Any]?)
```

## Parameters

- `mediaType` — The media type of the samples the input accepts.

- `outputSettings` — The settings to use for encoding the media you append to the output. Create an output settings dictionary manually, or use [AVOutputSettingsAssistant](../avoutputsettingsassistant.md) to create preset-based settings.

## Discussion

If you’re appending samples that are already in an acceptable compressed format, pass a value of `nil` for the output settings to pass the buffers to the output unaltered. However, if you’re not writing to a QuickTime movie file, an asset writer only supports passing through a restricted set of media types and subtypes. To pass through media data to files with a type other than [AVFileTypeQuickTimeMovie](../avfiletype/mov.md), pass a nonnull format hint using the [- initWithMediaType:outputSettings:sourceFormatHint:](<init(mediatype_outputsettings_sourceformathint_).md>) instead.

### Configuring audio settings

You must fully specify the audio settings dictionary when using this initializer, which means you must provide values for the following keys:

- [AVFormatIDKey](../../avfaudio/avformatidkey.md). The identifier of the audio format. For [kAudioFormatLinearPCM](../../coreaudiotypes/kaudioformatlinearpcm.md) format, you must include values for all relevant keys with a `AVLinearPCM` prefix, and for [kAudioFormatAppleLossless](../../coreaudiotypes/kaudioformatapplelossless.md), you must specify a value for [AVEncoderBitDepthHintKey](../../avfaudio/avencoderbitdepthhintkey.md).
- [AVSampleRateKey](../../avfaudio/avsampleratekey.md). The sample rate of the audio. Common values are `44100` and `48000`.
- [AVNumberOfChannelsKey](../../avfaudio/avnumberofchannelskey.md). If no other channel layout information is available, specifying a value of `1` results in mono output and a value of `2` results in stereo output. If [AVNumberOfChannelsKey](../../avfaudio/avnumberofchannelskey.md) specifies a channel count greater than `2`, the dictionary must also specify a value for [AVChannelLayoutKey](../../avfaudio/avchannellayoutkey.md).

> [!note] Note
> The system doesn’t support specifying a value for [AVSampleRateConverterAudioQualityKey](../../avfaudio/avsamplerateconverteraudioqualitykey.md) in audio output settings.

### Configuring video settings

A video output settings dictionary must request a compressed video format, which means that the value you specify must follow the rules for compressed video output.

You must fully specify the video settings dictionary when using this initializer, which means you must provide values for the following keys [AVVideoCodecKey](../avvideocodeckey.md), [AVVideoWidthKey](../avvideowidthkey.md), [AVVideoHeightKey](../avvideoheightkey.md).

> [!note] Note
> Specifying a [AVVideoScalingModeKey](../avvideoscalingmodekey.md) value of [AVVideoScalingModeFit](../avvideoscalingmodefit.md) results in an error.

## See Also

### Creating an input

- [- initWithMediaType:outputSettings:sourceFormatHint:](<init(mediatype_outputsettings_sourceformathint_).md>) — Creates an input that appends sample buffers of the specified type and format hint to the output file.
