---
title: AVCaptureVideoDataOutput
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturevideodataoutput
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideodataoutput.json'
content_hash: 'sha256:9321cfcd2066d18b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureVideoDataOutput

<sub>Class</sub>

A capture output that records video and provides access to video frames for processing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVCaptureVideoDataOutput
```

## Overview

Use this output to process compressed or uncompressed frames from the captured video. You can access the frames with the [- captureOutput:didOutputSampleBuffer:fromConnection:](<avcapturevideodataoutputsamplebufferdelegate/captureoutput(__didoutput_from_).md>) delegate method.

This object supports compressed video data output for macOS only. It can output pixel buffers in several pixel formats. Consider the usability and performance characteristics of these formats and choose the best format for your app.

> [!important] Important
> Avoid defaulting to a BGRA format, because BGRA formats aren’t native and require conversion. Additionally, BGRA formats requires significantly more memory than many of the native formats. For more information, see [TN3121: Selecting a pixel format for an AVCaptureVideoDataOutput](../technotes/tn3121-selecting-a-pixel-format-for-an-avcapturevideodataoutput.md).

## Relationships

- **Inherits From**: [AVCaptureOutput](avcaptureoutput.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring video capture

- [videoSettings](avcapturevideodataoutput/videosettings.md) — A dictionary that contains the compression settings for the output.
- [Video settings](video-settings.md) — Configure video processing settings using standard key and value constants.
- [alwaysDiscardsLateVideoFrames](avcapturevideodataoutput/alwaysdiscardslatevideoframes.md) — Indicates whether to drop video frames if they arrive late.
- [automaticallyConfiguresOutputBufferDimensions](avcapturevideodataoutput/automaticallyconfiguresoutputbufferdimensions.md) — A Boolean value that indicates whether the output automatically configures the size of output buffers.
- [deliversPreviewSizedOutputBuffers](avcapturevideodataoutput/deliverspreviewsizedoutputbuffers.md) — A Boolean value that indicates whether the output is configured to deliver preview-sized buffers.
- [preparesCellularRadioForNetworkConnection](avcapturevideodataoutput/preparescellularradiofornetworkconnection.md) — Indicates whether the receiver should prepare the cellular radio for imminent network activity.
- [preservesDynamicHDRMetadata](avcapturevideodataoutput/preservesdynamichdrmetadata.md) — Indicates whether the receiver should preserve dynamic HDR metadata as an attachment on the output sample buffer’s underlying pixel buffer.
- [recommendedMediaTimeScaleForAssetWriter](avcapturevideodataoutput/recommendedmediatimescaleforassetwriter.md) — Indicates the recommended media timescale for the video track.
- [- recommendedMovieMetadataForVideoCodecType:assetWriterOutputFileType:](<avcapturevideodataoutput/recommendedmoviemetadata(forvideocodectype_assetwriteroutputfiletype_).md>) — Recommends movie-level metadata for a particular video codec type and output file type, to be used with an asset writer input.
- [- recommendedVideoSettingsForVideoCodecType:assetWriterOutputFileType:](<avcapturevideodataoutput/recommendedvideosettings(forvideocodectype_assetwriteroutputfiletype_).md>) — Returns a video settings dictionary appropriate for capturing video to a file with the specified codec and type.
- [- recommendedVideoSettingsForVideoCodecType:assetWriterOutputFileType:outputFileURL:](<avcapturevideodataoutput/recommendedvideosettings(forvideocodectype_assetwriteroutputfiletype_outputfileurl_).md>) — Returns a dictionary of recommended output settings for writing the specified code, file type, and output URL.
- [- recommendedVideoSettingsForAssetWriterWithOutputFileType:](<avcapturevideodataoutput/recommendedvideosettingsforassetwriter(writingto_).md>) — Specifies the recommended settings for use with an AVAssetWriterInput.

### Retrieving supported video types

- [availableVideoPixelFormatTypes](avcapturevideodataoutput/availablevideopixelformattypes.md) — The video pixel formats the output supports.
- [availableVideoCodecTypes](avcapturevideodataoutput/availablevideocodectypes.md) — The video codecs that the output supports.
- [- availableVideoCodecTypesForAssetWriterWithOutputFileType:](<avcapturevideodataoutput/availablevideocodectypesforassetwriter(writingto_).md>) — The video codecs that the output supports for writing video to the output file.
- [AVVideoCodecType](avvideocodectype.md) — A set of constants that describe the codecs the system supports for video capture.

### Receiving captured video data

- [- setSampleBufferDelegate:queue:](<avcapturevideodataoutput/setsamplebufferdelegate(__queue_).md>) — Sets the sample buffer delegate and the queue for invoking callbacks.
- [sampleBufferDelegate](avcapturevideodataoutput/samplebufferdelegate.md) — The capture object’s delegate.
- [sampleBufferCallbackQueue](avcapturevideodataoutput/samplebuffercallbackqueue.md) — The queue on which the system invokes delegate callbacks.
- [AVCaptureVideoDataOutputSampleBufferDelegate](avcapturevideodataoutputsamplebufferdelegate.md) — Methods for receiving sample buffers from, and monitoring the status of, a video data output.

### Creating video capture output

- [- init](<avcapturevideodataoutput/init().md>) — Creates a new video file output.

## See Also

### Stream capture

- [Capturing Spatial Audio in your iOS app](capturing-spatial-audio-in-your-ios-app.md) — Enhance your app’s audio recording capabilities by supporting Spatial Audio capture.
- [AVCaptureAudioDataOutput](avcaptureaudiodataoutput.md) — A capture output that records audio and provides access to audio sample buffers as they are recorded.
- [AVCaptureSpatialAudioMetadataSampleGenerator](avcapturespatialaudiometadatasamplegenerator.md) — An interface for generating a spatial audio timed metadata sample.
