---
title: 'recommendedVideoSettings(forVideoCodecType:assetWriterOutputFileType:outputFileURL:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturevideodataoutput/recommendedvideosettings(forvideocodectype:assetwriteroutputfiletype:outputfileurl:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/recommendedvideosettings(forvideocodectype:assetwriteroutputfiletype:outputfileurl:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideodataoutput/recommendedvideosettings%28forvideocodectype%3Aassetwriteroutputfiletype%3Aoutputfileurl%3A%29.json'
content_hash: 'sha256:bd23d44857d15551'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md)

# recommendedVideoSettings(forVideoCodecType:assetWriterOutputFileType:outputFileURL:)

<sub>Instance Method</sub>

Returns a dictionary of recommended output settings for writing the specified code, file type, and output URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func recommendedVideoSettings(forVideoCodecType videoCodecType: AVVideoCodecType, assetWriterOutputFileType outputFileType: AVFileType, outputFileURL: URL?) -> [String : Any]?
```

## Parameters

- `videoCodecType` — The type of video codec to use.

- `outputFileType` — The type of output file to write.

- `outputFileURL` — The URL of the output file to write.

## Return Value

A fully populated output settings dictionary suitable for configuring an asset writer input.

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
- [- recommendedVideoSettingsForAssetWriterWithOutputFileType:](<recommendedvideosettingsforassetwriter(writingto_).md>) — Specifies the recommended settings for use with an AVAssetWriterInput.
