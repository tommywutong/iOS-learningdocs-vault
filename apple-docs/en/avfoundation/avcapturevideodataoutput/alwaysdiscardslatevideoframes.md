---
title: alwaysDiscardsLateVideoFrames
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturevideodataoutput/alwaysdiscardslatevideoframes
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/alwaysdiscardslatevideoframes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideodataoutput/alwaysdiscardslatevideoframes.json'
content_hash: 'sha256:24906d7a9a35e93b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md)

# alwaysDiscardsLateVideoFrames

<sub>Instance Property</sub>

Indicates whether to drop video frames if they arrive late.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var alwaysDiscardsLateVideoFrames: Bool { get set }
```

## Discussion

If this property is [true](../../swift/true.md), the output immediately discard frames that captured while the dispatch queue handling existing frames blocks in the [- captureOutput:didOutputSampleBuffer:fromConnection:](<../avcapturevideodataoutputsamplebufferdelegate/captureoutput(__didoutput_from_).md>) delegate method. When set to [false](../../swift/false.md), the output gives delegates more time to process old frames before it discards new frames, but application memory usage may increase significantly as a result.

The default is [true](../../swift/true.md).

## See Also

### Configuring video capture

- [videoSettings](videosettings.md) — A dictionary that contains the compression settings for the output.
- [Video settings](../video-settings.md) — Configure video processing settings using standard key and value constants.
- [automaticallyConfiguresOutputBufferDimensions](automaticallyconfiguresoutputbufferdimensions.md) — A Boolean value that indicates whether the output automatically configures the size of output buffers.
- [deliversPreviewSizedOutputBuffers](deliverspreviewsizedoutputbuffers.md) — A Boolean value that indicates whether the output is configured to deliver preview-sized buffers.
- [preparesCellularRadioForNetworkConnection](preparescellularradiofornetworkconnection.md) — Indicates whether the receiver should prepare the cellular radio for imminent network activity.
- [preservesDynamicHDRMetadata](preservesdynamichdrmetadata.md) — Indicates whether the receiver should preserve dynamic HDR metadata as an attachment on the output sample buffer’s underlying pixel buffer.
- [recommendedMediaTimeScaleForAssetWriter](recommendedmediatimescaleforassetwriter.md) — Indicates the recommended media timescale for the video track.
- [- recommendedMovieMetadataForVideoCodecType:assetWriterOutputFileType:](<recommendedmoviemetadata(forvideocodectype_assetwriteroutputfiletype_).md>) — Recommends movie-level metadata for a particular video codec type and output file type, to be used with an asset writer input.
- [- recommendedVideoSettingsForVideoCodecType:assetWriterOutputFileType:](<recommendedvideosettings(forvideocodectype_assetwriteroutputfiletype_).md>) — Returns a video settings dictionary appropriate for capturing video to a file with the specified codec and type.
- [- recommendedVideoSettingsForVideoCodecType:assetWriterOutputFileType:outputFileURL:](<recommendedvideosettings(forvideocodectype_assetwriteroutputfiletype_outputfileurl_).md>) — Returns a dictionary of recommended output settings for writing the specified code, file type, and output URL.
- [- recommendedVideoSettingsForAssetWriterWithOutputFileType:](<recommendedvideosettingsforassetwriter(writingto_).md>) — Specifies the recommended settings for use with an AVAssetWriterInput.
