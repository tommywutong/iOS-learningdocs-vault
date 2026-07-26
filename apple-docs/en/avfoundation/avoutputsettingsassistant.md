---
title: AVOutputSettingsAssistant
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avoutputsettingsassistant
source_url: 'https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avoutputsettingsassistant.json'
content_hash: 'sha256:b6d53cc57bb901c2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVOutputSettingsAssistant

<sub>Class</sub>

An object that builds audio and video output settings dictionaries.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVOutputSettingsAssistant
```

## Overview

Use an output settings assistant to create the audio and video settings that you use to configure instances of [AVAssetWriter](avassetwriter.md) and [AVAssetWriterInput](avassetwriterinput.md). You create an assistant with a specific preset configuration, such as [AVOutputSettingsPresetHEVC3840x2160WithAlpha](avoutputsettingspreset/hevc3840x2160withalpha.md) or [AVOutputSettingsPreset1920x1080](avoutputsettingspreset/preset1920x1080.md). You can accept the settings dictionaries as is to generate a file that conforms to the criteria that the preset implies. You may also use the dictionaries it generates as a base configuration that you can customize as you require.

Providing the assistant additional details about your source media helps it generate more complete results. For example, setting a value for its [sourceVideoFormat](avoutputsettingsassistant/sourcevideoformat.md) property ensures that the assistant generates settings that don’t scale up video frames from a smaller size.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating an assistant

- [+ outputSettingsAssistantWithPreset:](<avoutputsettingsassistant/init(preset_).md>) — Creates an output setting assistant with a preset configuration.
- [AVOutputSettingsPreset](avoutputsettingspreset.md) — A structure that defines preset configurations for an output settings assistant.
- [+ availableOutputSettingsPresets](<avoutputsettingsassistant/availableoutputsettingspresets().md>) — Returns an array of preset values to use to initialize an output settings assistant.

### Configuring output settings

- [outputFileType](avoutputsettingsassistant/outputfiletype.md) — A uniform type identifier (UTI) that indicates the type of file to write.
- [audioSettings](avoutputsettingsassistant/audiosettings.md) — An audio settings dictionary.
- [sourceAudioFormat](avoutputsettingsassistant/sourceaudioformat.md) — The format of the source audio data.
- [videoSettings](avoutputsettingsassistant/videosettings.md) — A video settings dictionary.
- [sourceVideoFormat](avoutputsettingsassistant/sourcevideoformat.md) — The format of the source video data.
- [sourceVideoMinFrameDuration](avoutputsettingsassistant/sourcevideominframeduration.md) — A time value that describes the minimum frame duration of the video data.
- [sourceVideoAverageFrameDuration](avoutputsettingsassistant/sourcevideoaverageframeduration.md) — A time value that describes the average frame duration of the video data.

## See Also

### Media writing

- [Converting projected video to Apple Projected Media Profile](converting-projected-video-to-apple-projected-media-profile.md) — Convert content with equirectangular or half-equirectangular projection to APMP.
- [Converting side-by-side 3D video to multiview HEVC and spatial video](converting-side-by-side-3d-video-to-multiview-hevc-and-spatial-video.md) — Create video content for visionOS by converting an existing 3D HEVC file to a multiview HEVC format, optionally adding spatial metadata to create a spatial video.
- [Adding a display mask rectangle metadata track to a movie file](adding-a-display-mask-rectangle-metadata-track-to-a-movie-file.md) — Show a specific area of a video by using timed display mask rectangle metadata.
- [Writing fragmented MPEG-4 files for HTTP Live Streaming](writing-fragmented-mpeg-4-files-for-http-live-streaming.md) — Create an HTTP Live Streaming presentation by turning a movie file into a sequence of fragmented MPEG-4 files.
- [Creating spatial photos and videos with spatial metadata](../imageio/creating-spatial-photos-and-videos-with-spatial-metadata.md) — Add spatial metadata to stereo photos and videos to create spatial media for viewing on Apple Vision Pro.
- [Tagging media with video color information](tagging-media-with-video-color-information.md) — Inspect and set video color space information when writing and transcoding media.
- [Evaluating an app’s video color](evaluating-an-app-s-video-color.md) — Check color reproduction for a video in your app by using test patterns, video test equipment, and light-measurement instruments.
- [AVAssetWriter](avassetwriter.md) — An object that writes media data to a container file.
- [AVAssetWriterInput](avassetwriterinput.md) — An object that appends media samples to a track in an asset writer’s output file.
- [AVAssetWriterInputPixelBufferAdaptor](avassetwriterinputpixelbufferadaptor.md) — An object that appends video samples to an asset writer input. _(deprecated)_
- [AVAssetWriterInputTaggedPixelBufferGroupAdaptor](avassetwriterinputtaggedpixelbuffergroupadaptor.md) — An object that appends tagged buffer groups to an asset writer input. _(deprecated)_
- [AVAssetWriterInputMetadataAdaptor](avassetwriterinputmetadataadaptor.md) — An object that appends timed metadata groups to an asset writer input. _(deprecated)_
- [AVAssetWriterInputGroup](avassetwriterinputgroup.md) — A group of inputs with tracks that are mutually exclusive to each other for playback or processing.
