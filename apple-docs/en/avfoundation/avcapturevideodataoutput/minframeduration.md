---
title: minFrameDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（5.0 起废弃）, iPadOS 4.0+（5.0 起废弃）, Mac Catalyst 14.0+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturevideodataoutput/minframeduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/minframeduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideodataoutput/minframeduration.json'
content_hash: 'sha256:1541fbfbef0159b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md)

# minFrameDuration

<sub>Instance Property</sub>

The minimum frame duration.

> [!warning] Deprecated
> Use the [AVCaptureConnection](../avcaptureconnection.md) class [videoMinFrameDuration](../avcaptureconnection/videominframeduration.md) property instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic) CMTime minFrameDuration;
```

## Discussion

This property specifies the minimum duration of each video frame produced by the video data output, placing a lower bound on the amount of time that should separate consecutive frames. This is equivalent to the inverse of the maximum frame rate. A value of [zero](../../coremedia/cmtime/zero.md) or [invalid](../../coremedia/cmtime/invalid.md) indicates an unlimited maximum frame rate.

The default value is [invalid](../../coremedia/cmtime/invalid.md).

## See Also

### Configuring video capture

- [videoSettings](videosettings.md) — A dictionary that contains the compression settings for the output.
- [Video settings](../video-settings.md) — Configure video processing settings using standard key and value constants.
- [alwaysDiscardsLateVideoFrames](alwaysdiscardslatevideoframes.md) — Indicates whether to drop video frames if they arrive late.
- [automaticallyConfiguresOutputBufferDimensions](automaticallyconfiguresoutputbufferdimensions.md) — A Boolean value that indicates whether the output automatically configures the size of output buffers.
- [deliversPreviewSizedOutputBuffers](deliverspreviewsizedoutputbuffers.md) — A Boolean value that indicates whether the output is configured to deliver preview-sized buffers.
- [preparesCellularRadioForNetworkConnection](preparescellularradiofornetworkconnection.md) — Indicates whether the receiver should prepare the cellular radio for imminent network activity.
- [preservesDynamicHDRMetadata](preservesdynamichdrmetadata.md) — Indicates whether the receiver should preserve dynamic HDR metadata as an attachment on the output sample buffer’s underlying pixel buffer.
- [recommendedMediaTimeScaleForAssetWriter](recommendedmediatimescaleforassetwriter.md) — Indicates the recommended media timescale for the video track.
- [- recommendedMovieMetadataForVideoCodecType:assetWriterOutputFileType:](<recommendedmoviemetadata(forvideocodectype_assetwriteroutputfiletype_).md>) — Recommends movie-level metadata for a particular video codec type and output file type, to be used with an asset writer input.
- [- recommendedVideoSettingsForVideoCodecType:assetWriterOutputFileType:](<recommendedvideosettings(forvideocodectype_assetwriteroutputfiletype_).md>) — Returns a video settings dictionary appropriate for capturing video to a file with the specified codec and type.
- [- recommendedVideoSettingsForVideoCodecType:assetWriterOutputFileType:outputFileURL:](<recommendedvideosettings(forvideocodectype_assetwriteroutputfiletype_outputfileurl_).md>) — Returns a dictionary of recommended output settings for writing the specified code, file type, and output URL.
- [- recommendedVideoSettingsForAssetWriterWithOutputFileType:](<recommendedvideosettingsforassetwriter(writingto_).md>) — Specifies the recommended settings for use with an AVAssetWriterInput.
