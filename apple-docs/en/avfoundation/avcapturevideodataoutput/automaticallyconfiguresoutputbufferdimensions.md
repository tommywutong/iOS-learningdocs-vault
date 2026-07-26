---
title: automaticallyConfiguresOutputBufferDimensions
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturevideodataoutput/automaticallyconfiguresoutputbufferdimensions
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/automaticallyconfiguresoutputbufferdimensions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideodataoutput/automaticallyconfiguresoutputbufferdimensions.json'
content_hash: 'sha256:137bc71bf684eb49'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md)

# automaticallyConfiguresOutputBufferDimensions

<sub>Instance Property</sub>

A Boolean value that indicates whether the output automatically configures the size of output buffers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var automaticallyConfiguresOutputBufferDimensions: Bool { get set }
```

## Discussion

In most configurations, [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md) delivers full-resolution buffers that match the video dimensions of the capture device’s [activeFormat](../avcapturedevice/activeformat.md) property. When this property is [true](../../swift/true.md), the output is free to scale the buffers delivered to [- captureOutput:didOutputSampleBuffer:fromConnection:](<../avcapturevideodataoutputsamplebufferdelegate/captureoutput(__didoutput_from_).md>) to a size suitable for preview (approximately the size of the screen).

You can query this property to find out whether the automatic configuration of output buffer dimensions is downscaling buffers to a preview size. You can also query the output’s [videoSettings](videosettings.md) dictionary to find the buffer’s exact dimensions.

The default value of this property is [true](../../swift/true.md).

> [!important] Important
> You must set this property to [false](../../swift/false.md) before you can manually set [deliversPreviewSizedOutputBuffers](deliverspreviewsizedoutputbuffers.md) to [true](../../swift/true.md).

## See Also

### Configuring video capture

- [videoSettings](videosettings.md) — A dictionary that contains the compression settings for the output.
- [Video settings](../video-settings.md) — Configure video processing settings using standard key and value constants.
- [alwaysDiscardsLateVideoFrames](alwaysdiscardslatevideoframes.md) — Indicates whether to drop video frames if they arrive late.
- [deliversPreviewSizedOutputBuffers](deliverspreviewsizedoutputbuffers.md) — A Boolean value that indicates whether the output is configured to deliver preview-sized buffers.
- [preparesCellularRadioForNetworkConnection](preparescellularradiofornetworkconnection.md) — Indicates whether the receiver should prepare the cellular radio for imminent network activity.
- [preservesDynamicHDRMetadata](preservesdynamichdrmetadata.md) — Indicates whether the receiver should preserve dynamic HDR metadata as an attachment on the output sample buffer’s underlying pixel buffer.
- [recommendedMediaTimeScaleForAssetWriter](recommendedmediatimescaleforassetwriter.md) — Indicates the recommended media timescale for the video track.
- [- recommendedMovieMetadataForVideoCodecType:assetWriterOutputFileType:](<recommendedmoviemetadata(forvideocodectype_assetwriteroutputfiletype_).md>) — Recommends movie-level metadata for a particular video codec type and output file type, to be used with an asset writer input.
- [- recommendedVideoSettingsForVideoCodecType:assetWriterOutputFileType:](<recommendedvideosettings(forvideocodectype_assetwriteroutputfiletype_).md>) — Returns a video settings dictionary appropriate for capturing video to a file with the specified codec and type.
- [- recommendedVideoSettingsForVideoCodecType:assetWriterOutputFileType:outputFileURL:](<recommendedvideosettings(forvideocodectype_assetwriteroutputfiletype_outputfileurl_).md>) — Returns a dictionary of recommended output settings for writing the specified code, file type, and output URL.
- [- recommendedVideoSettingsForAssetWriterWithOutputFileType:](<recommendedvideosettingsforassetwriter(writingto_).md>) — Specifies the recommended settings for use with an AVAssetWriterInput.
