---
title: AVAssetReaderTrackOutput
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreadertrackoutput
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreadertrackoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreadertrackoutput.json'
content_hash: 'sha256:c7996c88d770e5d8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetReaderTrackOutput

<sub>Class</sub>

An object that reads media data from a single track of an asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVAssetReaderTrackOutput
```

## Overview

Read the media data of an asset track by adding a track output to an asset reader. You can read the media samples in their stored format, or you can convert them to an alternative format.

A track output produces uncompressed output. For audio output settings, this means that [AVFormatIDKey](../avfaudio/avformatidkey.md) must be [kAudioFormatLinearPCM](../coreaudiotypes/kaudioformatlinearpcm.md). For video output settings, this means that the dictionary must contain values for uncompressed video output, as defined in `Video Settings`. A track output doesn’t support the [AVSampleRateConverterAudioQualityKey](../avfaudio/avsamplerateconverteraudioqualitykey.md) audio setting key or the following video settings keys: [AVVideoCleanApertureKey](avvideocleanaperturekey.md), [AVVideoPixelAspectRatioKey](avvideopixelaspectratiokey.md), and [AVVideoScalingModeKey](avvideoscalingmodekey.md).

When constructing video output settings, the choice of pixel format affects the performance and quality of the decompression. For optimal performance when decompressing video, the requested pixel format should be one that the decoder supports natively to avoid unnecessary conversions. Below are some recommendations:

- For H.264, use [kCVPixelFormatType_420YpCbCr8BiPlanarVideoRange](../corevideo/kcvpixelformattype_420ypcbcr8biplanarvideorange.md) or [kCVPixelFormatType_420YpCbCr8BiPlanarFullRange](../corevideo/kcvpixelformattype_420ypcbcr8biplanarfullrange.md) when you know the video is full range.
- In iOS, use [kCVPixelFormatType_420YpCbCr8BiPlanarFullRange](../corevideo/kcvpixelformattype_420ypcbcr8biplanarfullrange.md) for JPEG output.
- In macOS, [kCVPixelFormatType_422YpCbCr8](../corevideo/kcvpixelformattype_422ypcbcr8.md) is the preferred pixel format for video and generally provides the best performance when decoding. If you need to work in the RGB domain, use [kCVPixelFormatType_32BGRA](../corevideo/kcvpixelformattype_32bgra.md) in iOS, and [kCVPixelFormatType_32ARGB](../corevideo/kcvpixelformattype_32argb.md) in macOS.
- ProRes-encoded media can contain up to 12 bits per channel. For ProRes-encoded sources that you wish to preserve more than 8 bits per channel during decompression, use one of the following pixel formats: [kCVPixelFormatType_4444AYpCbCr16](../corevideo/kcvpixelformattype_4444aypcbcr16.md), [kCVPixelFormatType_422YpCbCr16](../corevideo/kcvpixelformattype_422ypcbcr16.md), [kCVPixelFormatType_422YpCbCr10](../corevideo/kcvpixelformattype_422ypcbcr10.md), or [kCVPixelFormatType_64ARGB](../corevideo/kcvpixelformattype_64argb.md). [AVAssetReader](avassetreader.md) doesn’t support scaling with any of these high-bit-depth pixel formats. If you use the above pixel formats, don’t specify [kCVPixelBufferWidthKey](../corevideo/kcvpixelbufferwidthkey.md) or [kCVPixelBufferHeightKey](../corevideo/kcvpixelbufferheightkey.md) in the [outputSettings](avassetreadertrackoutput/outputsettings.md) dictionary. Only ProRes encoders support these pixel formats.
- ProRes 4444-encoded media can contain a mathematically lossless alpha channel. To preserve the alpha channel during decompression, use a pixel format with an alpha component such as [kCVPixelFormatType_4444AYpCbCr16](../corevideo/kcvpixelformattype_4444aypcbcr16.md) or [kCVPixelFormatType_64ARGB](../corevideo/kcvpixelformattype_64argb.md). To test whether your source contains an alpha channel, check that the track’s format description has a [kCMFormatDescriptionExtension_Depth](../coremedia/kcmformatdescriptionextension_depth.md) key with a value of `32`.

## Relationships

- **Inherits From**: [AVAssetReaderOutput](avassetreaderoutput.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a track output

- [- initWithTrack:outputSettings:](<avassetreadertrackoutput/init(track_outputsettings_).md>) — Creates an object that reads media data from an asset track.
- [Video settings](video-settings.md) — Configure video processing settings using standard key and value constants.

### Configuring audio settings

- [audioTimePitchAlgorithm](avassetreadertrackoutput/audiotimepitchalgorithm.md) — The processing algorithm to use for scaled audio edits.

### Inspecting an output

- [outputSettings](avassetreadertrackoutput/outputsettings.md) — The output settings for this track output.
- [track](avassetreadertrackoutput/track.md) — The track from which the output reads sample buffers.

## See Also

### Media reading

- [Reading multiview 3D video files](reading-multiview-3d-video-files.md) — Render single images for the left eye and right eye from a multiview High Efficiency Video Coding format file by reading individual video frames.
- [AVAssetReader](avassetreader.md) — An object that reads media data from an asset.
- [AVAssetReaderOutput](avassetreaderoutput.md) — An abstract class that defines the interface to read media samples from an asset reader.
- [AVAssetReaderAudioMixOutput](avassetreaderaudiomixoutput.md) — An object that reads audio samples that result from mixing audio from one or more tracks.
- [AVAssetReaderVideoCompositionOutput](avassetreadervideocompositionoutput.md) — An object that reads composited video frames from one or more tracks of an asset.
- [AVAssetReaderSampleReferenceOutput](avassetreadersamplereferenceoutput.md) — An object that reads sample references from an asset track.
- [AVAssetReaderOutputMetadataAdaptor](avassetreaderoutputmetadataadaptor.md) — An object that creates timed metadata group objects for an asset track. _(deprecated)_
